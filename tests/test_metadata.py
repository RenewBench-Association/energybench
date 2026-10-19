"""PACKAGE METADATA TESTS.

Checks on the package metadata that every release depends on.
"""

import os
import sysconfig
from importlib.metadata import version
from importlib.resources import files
from pathlib import Path

import pytest

import energybench


def test_version_matches_distribution_metadata() -> None:
    """Ensure "__version__" reports the version of the installed distribution."""
    assert energybench.__version__ == version("energybench")


def test_package_is_marked_as_typed() -> None:
    """Ensure the "py.typed" marker ships, so type checkers use the package's hints."""
    assert files("energybench").joinpath("py.typed").is_file()


@pytest.mark.skipif(
    not os.environ.get("ENERGYBENCH_TEST_INSTALLED"),
    reason="only when CI tests a built and installed package",
)
def test_runs_against_installed_package() -> None:
    """Ensure the tests import the installed package, not the repository checkout.

    With a flat layout, a test run started next to the "energybench/" folder would
    import the checkout instead of the built wheel or sdist.
    """
    package_dir = Path(energybench.__file__).resolve().parent
    site_packages = Path(sysconfig.get_path("purelib")).resolve()
    assert package_dir.is_relative_to(site_packages)
