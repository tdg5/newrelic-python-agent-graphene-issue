"""
Export an ordered list of all the app initializers.
"""

from typing import Dict, List

from hello_full_stack.app import App

from .abstract_initializer import AbstractInitializer
from .config_initializer import ConfigInitializer
from .api_initializer import ApiInitializer


__all__ = [
    "AbstractInitializer",
    "INITIALIZERS",
]

# Order is important! Initializers are executed in the order defined below.
INITIALIZERS: List[AbstractInitializer] = [
    ConfigInitializer,
    ApiInitializer,
]
