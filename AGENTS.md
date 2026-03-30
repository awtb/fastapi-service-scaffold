# AGENTS.md

## Project

`python-service-scaffold` is a scaffold for Python services.

It is not a framework and not a platform layer.

Its purpose is to provide:

- a small set of composable runtimes
- a predictable project structure
- a few explicit structuring rules
- minimal boilerplate for starting a new service

## Mental model

Think in terms of **building blocks**, not a single fixed application template.

A generated project is assembled from:

- **runtimes** — ways to run the service (`cli`, `fastapi`, `faststream`, etc.)
- **integrations** — external infrastructure (`postgres`, `redis`, etc.)
- **presets** — opinionated combinations of blocks
- **structure rules** — conventions for where code should live

## Non-goals

This project does **not** aim to:

- enforce one universal architecture for every service
- hide Python/FastAPI/FastStream behind heavy abstractions
- generate large amounts of boilerplate
- behave like a plugin framework at runtime

## Core principles

1. Keep the baseline small.
2. Add only blocks that are explicitly selected.
3. Prefer composition over inheritance and magic.
4. Keep runtime-specific code isolated.
5. Keep the generated project understandable without scaffold internals.

## Structuring rules

- Shared bootstrap and common wiring should stay separated from business code.
- Runtime-specific entrypoints should stay inside their own runtime modules.
- Business logic should not depend directly on a specific runtime when avoidable.
- Integrations should be optional and explicit.
- Generated code should be easy to delete, replace, or simplify.

## Expected outcome

The scaffold should help create a service that is:

- small at start
- predictable in layout
- easy to extend
- easy to strip down
- not locked into one runtime