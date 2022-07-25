"""
Export an ordered list of all the app initializers.
"""

from typing import List

from .abstract_initializer import AbstractInitializer
from .api_initializer import ApiInitializer
from .container_initializer import ContainerInitializer


__all__ = [
    "AbstractInitializer",
    "INITIALIZERS",
]

# Order is important! Initializers are executed in the order defined below.
INITIALIZERS: List[AbstractInitializer] = [
    ContainerInitializer,
    ApiInitializer,
]
