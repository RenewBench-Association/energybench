---
title: energybench
---

# ![EnergyBench](assets/logo/energybench-light.svg#only-light){ .eb-wordmark } ![EnergyBench](assets/logo/energybench-dark.svg#only-dark){ .eb-wordmark }

**energybench** is the Python client for [EnergyBench](https://energybench.org), the open,
versioned catalog that pairs real-world electricity generation with high-resolution weather
data.

!!! warning "Pre-alpha"

    The package is at an early stage. Its public API is being built and may change between
    releases until version 1.0.

## Install

```bash
pip install energybench
```

or, in a [uv](https://docs.astral.sh/uv/) project:

```bash
uv add energybench
```

## What it will do

- **Search** the EnergyBench STAC API, with filtering evaluated on the server.
- **Load** matching data lazily as `xarray` objects, streaming only the chunks you use straight from
  object storage.
- **Pin** an exact, versioned query so collaborators can reproduce your slice.

See the [EnergyBench website](https://energybench.org/docs/getting-started) for the planned
workflow, and the [API reference](reference/api.md) for what exists today.
