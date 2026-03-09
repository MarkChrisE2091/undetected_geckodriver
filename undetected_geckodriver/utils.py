# Imports #
import platform
import random
import string
from pathlib import Path

from selenium import webdriver

from .constants import PLATFORM_DEPENDENT_PARAMS


# Functions #
def get_webdriver_instance() -> webdriver.Firefox:
    return webdriver.Firefox.__new__(webdriver.Firefox)


def get_platform_dependent_params() -> dict:
    system = platform.system()
    if system not in PLATFORM_DEPENDENT_PARAMS:
        raise OSError(f"Unsupported system: {system}")

    return PLATFORM_DEPENDENT_PARAMS[system]


def generate_random_string(length: int) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def get_platform_cache_path() -> str:
    params = get_platform_dependent_params()
    return str(Path.home() / params["undetected_path"])

