# AGENTS.md

Guidance for AI coding agents working in this repository. `CLAUDE.md` is a symlink to this file.

## What this is

`energybench` is the Python client for [EnergyBench](https://energybench.org). It is planned as a
thin layer over `pystac-client` and `xarray`/`zarr`/Icechunk:

- search the EnergyBench STAC API (`eb.Catalog().search(...)`)
- load assets lazily as xarray objects
- an optional `[mcp]` extra exposing an `energybench-mcp` server

The user-facing API is described in the backend's site docs (`site/src/pages/docs/` in
RenewBench-Association/energybench-backend). The package is pre-alpha; only the skeleton exists.

## Layout

- `energybench/`: the package (flat layout, no `src/`), shipped with `py.typed`
- `tests/`: pytest suite
- `docs/`: Zensical site; the API reference is generated from docstrings
- `.github/workflows/`: CI, release automation and security scanning

## Commands

```bash
uv sync                        # environment with every dev tool
uv run pytest                  # tests (warnings are errors)
uv run pyrefly check           # strict type checking
uv run ruff check --fix && uv run ruff format
uv run prek run --all-files    # every hook, as CI runs them
uv run zensical build --strict # docs
```

## Conventions

- Code conventions (details in CONTRIBUTING.md, "Code conventions"):
  - Python >= 3.12; Black style via `ruff format`, line length 88.
  - Lowercase type hints (`list[str]`, `str | None`) on every function. Pyrefly runs in strict
    mode, and ruff runs the rule set in `pyproject.toml`.
  - Google-style docstrings on every function, method and class, tests included. Every argument
    goes in `Args:` with its type in brackets, plus `Returns:`/`Raises:`, and `Attributes:` for
    classes.
  - American English; loguru for logging; absolute imports only.
  - Branch prefixes are the Conventional Commit types (`feat/`, `fix/`, `docs/`, `chore/`, …), so a
    branch matches its PR title.
- Add runtime dependencies with `uv add` and dev tools with `uv add --group <group>`. Always keep
  `uv.lock` in sync.
- Commit messages and PR titles are Conventional Commits. They drive release-please, so never edit
  the version or `CHANGELOG.md` by hand.
- Releases:
  - Merging to `main` never releases.
  - The core release team pushes `main` to `release-test` (TestPyPI dry run) and `release`
    (release-please release PR, then tag and PyPI). A release is only published if release-test
    passed on the same commit. See RELEASE.md.
  - Never push to those branches unless asked.
- Workflows:
  - Pin every action to a full commit SHA with a `# vX.Y.Z` comment.
  - Grant permissions per job, with `permissions: {}` at the top.
  - zizmor and actionlint must pass.
