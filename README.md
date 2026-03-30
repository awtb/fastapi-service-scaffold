# 🧱 Python service scaffold

Minimal scaffold for Python services.

This project generates small service templates from explicit building blocks.

It is designed to keep the starting point predictable, easy to understand, and easy to strip down.

## Goals

- small baseline
- explicit composition
- isolated runtime code
- optional integrations
- minimal boilerplate

## Baseline

The baseline generated project is intentionally small. It includes the package layout, CLI entrypoint, shared settings, logging setup, and the common `features`, `models`, `protocols`, and `infra` packages.

With plain `copier copy .`, the default baseline also enables the HTTP runtime. PostgreSQL, the users feature, and pre-commit remain opt-in.

## Current Template

The current template exposes these blocks:

- CLI runtime, included by default
- HTTP runtime with FastAPI, optional in the template and enabled in Copier defaults
- PostgreSQL integration, optional
- users feature package, optional and requires PostgreSQL
- pre-commit setup, optional

The mental model also includes presets and structure rules, but the concrete switches in the current template are the runtime, integration, and feature blocks above.

## Usage

Render a project with Copier:

```bash
copier copy .
```

Or render the example project with the repo `Makefile`:

```bash
make render
```

The generated example is written to `examples/generated/health-service/` by default.
