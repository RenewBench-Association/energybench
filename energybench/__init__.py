"""ENERGYBENCH.

Search the EnergyBench catalog and load open energy and weather data.
"""

from importlib.metadata import version

__all__ = ["__version__"]

__version__: str = version(__name__)
"""The installed version of the package."""
