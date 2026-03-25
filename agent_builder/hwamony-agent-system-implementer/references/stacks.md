# Implementation Stacks

## Direct Vendor API

Best for:

- single-vendor systems
- clean production code
- precise control over API features

Strengths:

- lowest abstraction overhead
- easiest access to vendor-specific features
- clearest debugging

Weaknesses:

- weaker portability
- more vendor-specific code

## LangChain

Best for:

- chain composition
- tool orchestration
- teams already invested in LangChain

Strengths:

- reusable abstractions
- ecosystem integrations
- easier multi-step graph-style composition

Weaknesses:

- abstraction leakage
- extra debugging surface
- vendor features may lag behind raw APIs

## Lightweight Multi-Vendor Wrapper

Best for:

- vendor comparison experiments
- portability-sensitive prototypes

Strengths:

- common internal interface
- easier A/B testing across vendors

Weaknesses:

- least access to unique vendor features
- often needs adapter maintenance

## Default Choice

Prefer direct vendor APIs unless there is a clear need for framework abstractions or multi-vendor switching.
