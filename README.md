# Python service scaffold

Minimal scaffold for Python services.

This project generates small service templates from explicit building blocks:

- runtimes
- integrations
- presets
- structure rules

It is designed to keep the starting point predictable, easy to understand, and easy to strip down.

## Goals

- small baseline
- explicit composition
- isolated runtime code
- optional integrations
- minimal boilerplate

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
