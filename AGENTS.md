# AGENTS.md

This repository is a Copier template for a minimal FastAPI service scaffold.

The generated project is intentionally small:
- one internal endpoint: `GET /internal/healthcheck`
- FastAPI app factory in `runtimes/http/app.py`
- HTTP middleware in `runtimes/http/middleware.py`
- HTTP routers under `runtimes/http/routers/`
- shared logging bootstrap in `infra/logging/config.py`
- Typer-based CLI entrypoint in `__main__.py`
- settings in `settings.py` via `pydantic-settings`
- `uv` for dependency and runtime workflow
- optional container run path through `Dockerfile` and `compose.yaml`

## Working Model

Treat this repository as a template product, not as an application.

That means:
- edit files in `template/` to change the generated project
- edit `copier.yml` to change template inputs
- use `examples/generated/` only as local render output for verification
- do not manually maintain files under `examples/generated/` as source of truth

## Startup Conventions

The generated app starts through `__main__.py`.

Expected behavior:
- CLI is implemented with `typer`
- `--reload` is a CLI flag
- host and port come from `Settings`
- uvicorn runs `"<package_name>.runtimes.http.app:build_app"` with `factory=True`

If startup behavior changes, update all of these together:
- `template/__main__.py.jinja`
- `template/Makefile.jinja`
- `template/Dockerfile.jinja`
- `template/README.md.jinja`

## Package Conventions

Generated code separates business capabilities from transport concerns.

- keep business capabilities under `<package_name>/features/`
- keep shared technical support under `<package_name>/infra/`
- keep transport adapters under `<package_name>/runtimes/<runtime_name>/`
- runtime code may import feature use cases
- feature code must not import runtime code

Recommended feature structure:

- `features/{name}/use_cases/` is the default required part
- `features/{name}/domain/` is optional and only for real business rules/entities
- `features/{name}/infra/` is optional and only for persistence or external integrations
- `features/{name}/ports.py` is optional for feature-owned interfaces
- `features/{name}/contracts.py` is optional for feature input/output models

Trivial endpoints may stay directly in a runtime handler when extracting a feature would add ceremony without value.

## Dependency Conventions

Use `uv` as the package manager everywhere.

That applies to:
- local developer commands
- generated `Makefile`
- Docker image build path

Avoid mixing package managers unless there is a concrete need.

Current important generated dependencies:
- `fastapi`
- `uvicorn[standard]`
- `typer`
- `pydantic-settings`
- `pytest`
- `httpx`

## Template Inputs

Keep the input set small. Add new questions only when they materially affect the baseline scaffold.

## Validation Workflow

Use the root `Makefile` to validate scaffold changes.

Primary commands:
- `make render`
- `make test-rendered`
- `make compose-config-rendered`
- `make check-template`
- `make clean-generated`

Expected workflow for template changes:
1. Edit `template/` and/or `copier.yml`
2. Run `make test-rendered`
3. If container-related files changed, run `make compose-config-rendered` or `make check-template`

## Minimalism Rules

This scaffold should remain a baseline, not a kitchen-sink starter.

Prefer:
- one obvious way to run the app
- one obvious place for routers
- one obvious settings module
- minimal dependencies
- small files with direct intent

Avoid adding:
- database integration by default
- workers, telemetry, auth, or migrations by default
- extra endpoints beyond healthcheck unless the scaffold direction changes
- multiple startup paths that do the same thing
- extra abstractions without immediate value

## Commit Style

Prefer small commits with conventional-style messages when making focused changes.
Default rule: one commit per changed file.

Only group multiple files into one commit when they are tightly coupled and splitting them would leave the history misleading or broken.

Examples:
- `feat(template): add settings module`
- `build(template): update dockerfile`
- `test(template): adjust healthcheck test`
- `docs(template): update generated readme`
- `chore(repo): update scaffold makefile`

## Practical Rule

If unsure whether to add something, bias toward keeping the scaffold smaller.
