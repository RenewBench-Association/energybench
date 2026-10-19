<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RenewBench-Association/energybench/main/docs/assets/logo/energybench-dark.svg">
    <img alt="EnergyBench" src="https://raw.githubusercontent.com/RenewBench-Association/energybench/main/docs/assets/logo/energybench-light.svg" width="420">
  </picture>
</h1>

[![CI](https://github.com/RenewBench-Association/energybench/actions/workflows/ci.yml/badge.svg)](https://github.com/RenewBench-Association/energybench/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/energybench)](https://pypi.org/project/energybench/)
[![Python versions](https://img.shields.io/pypi/pyversions/energybench)](https://pypi.org/project/energybench/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/RenewBench-Association/energybench/blob/main/LICENSE)
[![Documentation](https://readthedocs.org/projects/energybench/badge/?version=latest)](https://energybench.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/RenewBench-Association/energybench/graph/badge.svg)](https://codecov.io/gh/RenewBench-Association/energybench)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/RenewBench-Association/energybench/badge)](https://scorecard.dev/viewer/?uri=github.com/RenewBench-Association/energybench)
[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Contact](https://img.shields.io/badge/Contact-renewbench%40lists.kit.edu-orange)](mailto:renewbench@lists.kit.edu)

The Python client for [EnergyBench](https://energybench.org): one open, versioned catalog that
pairs real-world electricity **generation** with high-resolution **weather** data.

> [!WARNING]
> `energybench` is pre-alpha. The public API is being built and may change between releases until
> version 1.0.

## Install

```bash
pip install energybench
```

or, in a [uv](https://docs.astral.sh/uv/) project, `uv add energybench`.

## What it will do

- **Search** the EnergyBench STAC API, with filtering evaluated on the server.
- **Load** matching data lazily as `xarray` objects, streaming only the chunks you use straight from
  object storage.
- **Pin** an exact, versioned query so collaborators can reproduce your slice.

The [EnergyBench documentation](https://energybench.org/docs/getting-started) describes the planned
workflow; the [package documentation](https://energybench.readthedocs.io) covers what exists today.

## Contributing

Contributions are welcome. [CONTRIBUTING.md](CONTRIBUTING.md) explains the development setup, the
commit conventions that drive releases, and how to run the checks. Please report security issues
privately as described in [SECURITY.md](SECURITY.md).

## Citation

If you use EnergyBench, please cite it as described in [CITATION.cff](CITATION.cff) or on the
[EnergyBench website](https://energybench.org/cite).

## License

[MIT](LICENSE) © 2026 RenewBench Association
