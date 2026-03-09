"""
    Undetected Geckodriver
    ======================
    This package provides a sophisticated wrapper around the
    webdriver.Firefox class from the Selenium package. It
    attempts to avoid detection by web services by patching
    certain parts of the Firefox browser.

    Author: Bytexenon (https://github.com/Bytexenon)
"""

# Imports #
import importlib.metadata

from .driver import Firefox as Firefox

# Constants #
try:
    __version__ = importlib.metadata.version("undetected-geckodriver")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["Firefox", "__version__"]
