# Contributing

Thank you for helping to improve `energybench`! This guide explains how to get the code, set up a
development environment, and the conventions the project follows.

## Getting the code

**Members of the RenewBench-Association** with write access work in the repository
directly:

```bash
git clone https://github.com/RenewBench-Association/energybench.git
cd energybench
git switch -c feat/short-description
```

**Everyone else contributes from a fork:**

1. Click **Fork** on the [repository page](https://github.com/RenewBench-Association/energybench)
   to copy it to your own account.
2. Clone your fork and register the original repository as `upstream`:

   ```bash
   git clone https://github.com/<your-username>/energybench.git
   cd energybench
   git remote add upstream https://github.com/RenewBench-Association/energybench.git
   git switch -c feat/short-description
   ```

3. Before you start, and again before opening a pull request, bring your branch up to date:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

4. Push the branch to your fork (`git push -u origin feat/short-description`) and open a pull
   request against `main` of `RenewBench-Association/energybench`. Leave **Allow edits by
   maintainers** ticked, so we can make small fixes for you.

For a first-time contributor, a maintainer has to approve the CI run before it starts. Pull
requests from forks skip the coverage upload to Codecov.

Either way, never commit directly to `main` - every change goes through a pull request.

Start your branch name with the Conventional Commit type of the change, followed by a slash: `feat/`,
`fix/`, `docs/`, `perf/`, `refactor/`, `test/`, `build/`, `ci/`, `chore/` or `revert/`. For example,
use `feat/catalog-search` for a pull request titled `feat: add Catalog.search`. The branch name
then matches the pull request title, which is what release-please reads (see
[Commit messages and pull requests](#commit-messages-and-pull-requests)). The branch name itself
has no effect on releases.

## Development setup

You need [uv](https://docs.astral.sh/uv/getting-started/installation/) and git. In your clone, uv
installs the right Python version and every development tool from the lockfile:

```bash
uv sync                  # creates .venv with the package and all dev tools
uv run prek install      # installs the pre-commit and commit-msg hooks
```

[prek](https://prek.j178.dev) reads `.pre-commit-config.yaml`, so plain `pre-commit` works too.

## Everyday commands

| Task | Command |
| --- | --- |
| Run the tests | `uv run pytest` |
| Test on another Python version | `uv run --isolated --python 3.12 pytest` |
| Measure coverage | `uv run coverage run -m pytest && uv run coverage combine && uv run coverage report` |
| Type check (strict) | `uv run pyrefly check` |
| Lint and format | `uv run ruff check --fix && uv run ruff format` |
| Run every hook | `uv run prek run --all-files` |
| Preview the docs | `uv run zensical serve` |
| Add a runtime dependency | `uv add <package>` |
| Add a development tool | `uv add --group <test, typing, lint or docs> <package>` |

Always commit `uv.lock` together with `pyproject.toml` - the `uv-lock` hook checks they agree.

## Code conventions

- Code follows the Black style, applied by `ruff format`, with a line length of 88.
- Use lowercase, subscriptable type hints in every function definition: `list[str]` and
  `str | None`, not `List[str]` or `Optional[str]`. Pyrefly checks types in strict mode, and ruff
  checks that every function is annotated.
- Write comments and docstrings in American English. The spell checker enforces it.
- Use [loguru](https://loguru.readthedocs.io) for logging.
- Use absolute imports (`from energybench.x import y`).
- Tests treat warnings as errors. Fix a deprecation warning when it appears rather than silencing
  it.

### Docstrings

Every function, method and class, tests included, has a docstring in the
[Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
Document every argument, with its type in brackets. The docstrings become the
[API reference](https://energybench.readthedocs.io/en/latest/reference/api/).

```python
def defined_function(param1: type, param2: type = default) -> type:
    """Short description.

    Long description (if needed).

    Args:
        param1 (type): Description of param1.
        param2 (type, optional): Description of param2. Defaults to default.

    Returns:
        type: Description of return value.

    Raises:
        ExceptionType: Description of when and why this exception might be raised.
    """
```

For classes, list the attributes, and document the arguments in `__init__`:

```python
class DefinedClass:
    """Summary of class here.

    Detailed class description (if needed).

    Attributes:
        attribute1 (type): Description of attribute 1.
        attribute2 (type): Description of attribute 2.
    """

    def __init__(self, attribute1: type) -> None:
        """Initialize the instance based on ...

        Args:
            attribute1 (type): Description of attribute 1.
        """
```

Module docstrings are optional. If you write one, start it with the module name in capitals, as in
`"""CONFIGURATION.`.

## Commit messages and pull requests

The project uses [Conventional Commits](https://www.conventionalcommits.org): every pull request
title starts with a type such as `feat:` or `fix:`. The type decides where the change appears in
the changelog and how the version number changes at the next release:

| Type | Use it for | Changelog heading | Example of next release, starting from 0.4.2 |
| --- | --- | --- |----------------------------------------------|
| `feat` | a new feature | Features | 0.5.0                                        |
| `fix` | a bug fix | Bug Fixes | 0.4.3                                        |
| `perf` | a performance improvement | Performance | 0.4.3                                        |
| `docs` | documentation only | Documentation | 0.4.3                                        |
| `revert` | undoing an earlier change | Reverts | 0.4.3                                        |
| `refactor`, `test`, `style`, `build`, `ci`, `chore` | everything else | not shown | no release on its own                        |

Mark a change that breaks existing code with `!` after the type, for example
`feat!: rename Catalog.search`. From 1.0 onwards this raises the first number (1.4.2 → 2.0.0).
Before 1.0 it raises the middle number instead (0.4.2 → 0.5.0).

Pull requests are squash-merged, so **the pull request title becomes the commit message** on
`main`. A check enforces that the title is a Conventional Commit. Individual commits on your branch
are checked by the `commit-msg` hook.

Every pull request must pass the `ci-ok` check. It covers:

- linting, type checking, and the tests on Linux, macOS and Windows with Python 3.12 to 3.15
- tests against the oldest allowed dependency versions, and against a pip-only install
- the docs build
- the coverage floor of 90 %

## Releases

Releases are made by the core release team; see [RELEASE.md](https://github.com/RenewBench-Association/energybench/blob/main/RELEASE.md). As a contributor you
**need a clear and concise pull request title** since this title will determine the changelog entry and the next
version number.

## Dependency updates

Dependabot proposes weekly, grouped updates for Python dependencies, GitHub Actions and the prek
hooks. These updates use the `chore` and `ci` types, so they never cause a release on their own.

## Code of conduct

This project follows the [Contributor Covenant](https://github.com/RenewBench-Association/energybench/blob/main/CODE_OF_CONDUCT.md). Report unacceptable behavior
to renewbench@lists.kit.edu.
