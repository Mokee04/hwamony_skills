#!/usr/bin/env python3
"""Search GitHub for installable agent skills."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

try:
    import certifi
except ImportError:  # pragma: no cover - optional dependency
    certifi = None

API_ROOT = "https://api.github.com"
USER_AGENT = "hwamony-search-skills"
IGNORE_DIRS = {
    ".git",
    ".github",
    ".idea",
    ".next",
    ".turbo",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
}


class SearchError(Exception):
    pass


def request_json(url: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    ssl_context = build_ssl_context()
    try:
        with urllib.request.urlopen(req, context=ssl_context) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        try:
            parsed_detail = json.loads(detail)
        except json.JSONDecodeError:
            parsed_detail = None
        if isinstance(parsed_detail, dict):
            message = parsed_detail.get("message")
            if isinstance(message, str) and "rate limit exceeded" in message.lower():
                raise SearchError(
                    "GitHub API rate limit exceeded. Set GITHUB_TOKEN or GH_TOKEN and rerun the search."
                ) from exc
        raise SearchError(f"GitHub API request failed: HTTP {exc.code} for {url}\n{detail}") from exc
    except urllib.error.URLError as exc:
        raise SearchError(f"GitHub API request failed for {url}: {exc.reason}") from exc


def build_ssl_context() -> ssl.SSLContext:
    if certifi is not None:
        return ssl.create_default_context(cafile=certifi.where())
    return ssl.create_default_context()


def search_repositories(query: str, per_page: int) -> list[dict]:
    search_query = f"{query} skill skills agent archived:false"
    params = urllib.parse.urlencode(
        {
            "q": search_query,
            "sort": "stars",
            "order": "desc",
            "per_page": str(per_page),
        }
    )
    payload = request_json(f"{API_ROOT}/search/repositories?{params}")
    if not isinstance(payload, dict):
        raise SearchError("Unexpected search response from GitHub.")
    items = payload.get("items", [])
    if not isinstance(items, list):
        raise SearchError("GitHub search response did not include repository items.")
    return [item for item in items if isinstance(item, dict)]


def contents_url(owner: str, repo: str, ref: str, path: str) -> str:
    base = f"{API_ROOT}/repos/{owner}/{repo}/contents"
    if path:
        return f"{base}/{urllib.parse.quote(path, safe='/')}?ref={urllib.parse.quote(ref)}"
    return f"{base}?ref={urllib.parse.quote(ref)}"


def discover_skill_paths(owner: str, repo: str, ref: str, max_dirs: int = 200) -> list[str]:
    queue = [""]
    seen = set()
    skill_paths: list[str] = []
    visited_dirs = 0

    while queue and visited_dirs < max_dirs:
        current = queue.pop(0)
        if current in seen:
            continue
        seen.add(current)
        visited_dirs += 1
        payload = request_json(contents_url(owner, repo, ref, current))
        if not isinstance(payload, list):
            continue

        for entry in payload:
            if not isinstance(entry, dict):
                continue
            entry_type = entry.get("type")
            name = entry.get("name")
            path = entry.get("path")
            if not isinstance(name, str) or not isinstance(path, str):
                continue
            if entry_type == "file" and name == "SKILL.md":
                skill_paths.append(path.rsplit("/", 1)[0] if "/" in path else ".")
            elif entry_type == "dir" and name not in IGNORE_DIRS:
                queue.append(path)

        time.sleep(0.05)

    return sorted(set(skill_paths))


def tokenize(text: str) -> list[str]:
    return [part for part in re.split(r"[^a-z0-9]+", text.lower()) if len(part) >= 2]


def score_candidate(repo: dict, skill_path: str, query_terms: list[str]) -> tuple[float, str]:
    text_parts = [
        repo.get("full_name", ""),
        repo.get("name", ""),
        repo.get("description") or "",
        skill_path,
    ]
    haystack = " ".join(part.lower() for part in text_parts if isinstance(part, str))
    matches = [term for term in query_terms if term in haystack]
    keyword_score = float(len(matches) * 4)
    if skill_path != ".":
        keyword_score += 1.0
    stars = repo.get("stargazers_count", 0)
    if isinstance(stars, int) and stars > 0:
        keyword_score += min(4.0, math.log10(stars + 1))
    reason = ", ".join(matches[:4]) if matches else "broad skill match"
    return keyword_score, reason


def build_candidate(repo: dict, skill_path: str, query_terms: list[str]) -> dict:
    score, reason = score_candidate(repo, skill_path, query_terms)
    full_name = repo["full_name"]
    default_branch = repo.get("default_branch", "main")
    skill_name = full_name.split("/")[-1] if skill_path == "." else skill_path.rstrip("/").split("/")[-1]
    html_url = f"https://github.com/{full_name}/tree/{default_branch}"
    if skill_path != ".":
        html_url = f"{html_url}/{skill_path}"

    return {
        "repo": full_name,
        "skill_name": skill_name,
        "path": skill_path,
        "url": html_url,
        "default_branch": default_branch,
        "stars": repo.get("stargazers_count", 0),
        "updated_at": repo.get("updated_at"),
        "description": repo.get("description"),
        "score": round(score, 3),
        "match_reason": reason,
    }


def render_text(results: list[dict]) -> str:
    lines: list[str] = []
    for index, item in enumerate(results, start=1):
        updated = (item.get("updated_at") or "").split("T", 1)[0]
        description = item.get("description") or "No repository description."
        lines.append(f"{index}. {item['repo']} :: {item['skill_name']}")
        lines.append(f"   stars: {item['stars']} | updated: {updated or 'unknown'} | path: {item['path']}")
        lines.append(f"   why: {item['match_reason']}")
        lines.append(f"   about: {description}")
        lines.append(
            "   install: "
            f"python3 scripts/install_github_skill.py --repo {item['repo']} --path {item['path']}"
        )
        lines.append(f"   url: {item['url']}")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search GitHub for agent skills.")
    parser.add_argument("query", help="Short natural-language search query")
    parser.add_argument("--limit", type=int, default=8, help="Maximum number of results to print")
    parser.add_argument(
        "--max-repos",
        type=int,
        default=6,
        help="Number of repositories to inspect deeply for SKILL.md files",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    query_terms = tokenize(args.query)
    if not query_terms:
        print("Search query must include at least one word or number.", file=sys.stderr)
        return 1

    try:
        repos = search_repositories(args.query, max(args.max_repos, args.limit))
        candidates: list[dict] = []
        for repo in repos[: args.max_repos]:
            full_name = repo.get("full_name")
            default_branch = repo.get("default_branch")
            if not isinstance(full_name, str) or "/" not in full_name or not isinstance(default_branch, str):
                continue
            owner, repo_name = full_name.split("/", 1)
            for skill_path in discover_skill_paths(owner, repo_name, default_branch):
                candidates.append(build_candidate(repo, skill_path, query_terms))

        candidates.sort(
            key=lambda item: (
                float(item["score"]),
                int(item.get("stars") or 0),
                item.get("updated_at") or "",
            ),
            reverse=True,
        )
        results = candidates[: args.limit]
        if args.format == "json":
            print(json.dumps(results, indent=2, ensure_ascii=True))
        else:
            if not results:
                print("No installable skills found for that query.")
            else:
                print(render_text(results))
        return 0
    except SearchError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
