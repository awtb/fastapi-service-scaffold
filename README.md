# 🧱 Python service scaffold

Minimal scaffold for Python services.

This repository generates small projects from explicit building blocks instead of one large fixed template.

## What This Scaffold Is

Use this scaffold when you want a Python service that starts small, stays readable, and can grow by adding only the parts you actually need.

The generated project is meant to be:

- small at the start
- explicit in structure
- easy to strip down
- easy to extend
- understandable without scaffold internals

## Mental Model

A generated project is assembled from a few kinds of generation-time blocks:

- runtimes: ways to run the service, such as CLI, HTTP, or stream
- integrations: infrastructure such as PostgreSQL or Redis
- components: optional adapters such as Telegram bot support or templating
- features: ready-to-use business slices, such as the sample users package
- tooling: project-level setup such as pre-commit

The main rule is composition over magic. If a block is not selected, it should not appear in the generated codebase.

## Blocks vs Packages

There are two different views of the scaffold:

1. The block view answers: what was selected when the project was generated?
2. The package view answers: where does code live inside the generated project?

These are related, but they are not the same thing.

Examples:

- the HTTP runtime is a block, and its code lives under `runtimes/http/`
- the Redis integration is a block, and its code usually lives under `infra/redis/` plus `protocols/redis/`
- the templating component is a block, and its code usually lives under `infra/templating/` plus `protocols/templating/`
- the users feature is a block, and its code lives under `features/users/`

So:

- blocks describe what is included
- packages describe where the included code is placed

## Current Blocks

The current scaffold supports:

- CLI runtime, included by default
- HTTP runtime with FastAPI
- Telegram bot webhook component with aiogram, requires HTTP runtime
- stream runtime with FastStream, requires Redis
- Redis integration
- PostgreSQL integration
- users feature package, requires PostgreSQL
- templating component with an async Jinja adapter
- pre-commit setup

## Generated Structure

Generated projects use a small, predictable layout:

- `runtimes/` for entrypoints and transport-specific wiring
- `features/` for business capabilities
- `infra/` for technical adapters and integration code
- `protocols/` for interfaces between layers
- `models/` for shared business models
- `tests/` for checks covering rendered blocks

These packages are not separate scaffold block types.
They are the fixed project structure used to place whatever blocks were enabled.

The placement rule is:

- runtime-specific code stays in `runtimes/`
- business logic stays in `features/`
- infrastructure code stays in `infra/`
- shared contracts stay in `protocols/`
- shared business models stay in `models/`

Typical mappings:

- runtime blocks mostly add code under `runtimes/`
- integration and component blocks mostly add code under `infra/` and `protocols/`
- feature blocks mostly add code under `features/`, and sometimes `models/`

## Quick Start

Generate a project directly from GitHub with Copier:

```bash
copier copy gh:awtb/python-service-scaffold my-service
```

If you prefer a full Git URL, use:

```bash
copier copy https://github.com/awtb/python-service-scaffold.git my-service
```

Then move into the generated project:

```bash
cd my-service
```

## Useful Render Variants

Render a minimal CLI-only service:

```bash
copier copy \
  -d project_slug='cli-service' \
  -d package_name='cli_service' \
  -d include_http_runtime=false \
  -d include_tg_bot_runtime=false \
  -d include_stream_runtime=false \
  -d include_redis_plugin=false \
  -d include_postgresql_plugin=false \
  -d include_users_plugin=false \
  -d include_templating_component=false \
  gh:awtb/python-service-scaffold \
  cli-service
```

Render an HTTP service with PostgreSQL:

```bash
copier copy \
  -d project_slug='http-service' \
  -d package_name='http_service' \
  -d include_http_runtime=true \
  -d include_postgresql_plugin=true \
  -d include_users_plugin=false \
  -d include_templating_component=false \
  gh:awtb/python-service-scaffold \
  http-service
```

Render an HTTP service with Telegram bot support:

```bash
copier copy \
  -d project_slug='bot-service' \
  -d package_name='bot_service' \
  -d include_http_runtime=true \
  -d include_tg_bot_runtime=true \
  -d include_postgresql_plugin=false \
  -d include_redis_plugin=false \
  -d include_templating_component=false \
  gh:awtb/python-service-scaffold \
  bot-service
```

Render a service with only the templating component:

```bash
copier copy \
  -d project_slug='templating-service' \
  -d package_name='templating_service' \
  -d include_http_runtime=false \
  -d include_tg_bot_runtime=false \
  -d include_stream_runtime=false \
  -d include_redis_plugin=false \
  -d include_postgresql_plugin=false \
  -d include_users_plugin=false \
  -d include_templating_component=true \
  gh:awtb/python-service-scaffold \
  templating-service
```

## Template Defaults

The default Copier flow currently enables:

- CLI runtime
- HTTP runtime

And leaves these opt-in:

- Telegram bot
- stream runtime
- Redis
- PostgreSQL
- users feature
- templating
- pre-commit

## Design Intent

The scaffold tries to keep a generated service easy to reason about:

- shared bootstrap is small
- runtime code is isolated
- integrations are explicit
- scaffolded code is easy to delete or replace
- no hidden architecture is required to understand the project
