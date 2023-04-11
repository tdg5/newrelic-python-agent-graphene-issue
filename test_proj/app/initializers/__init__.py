"""
Export an ordered list of all the app initializers.
"""

from typing import List

from test_proj.app.initializers.abstract_initializer import AbstractInitializer
from test_proj.app.initializers.api_initializer import ApiInitializer
from test_proj.app.initializers.container_initializer import ContainerInitializer
from test_proj.app.initializers.newrelic_initializer import NewrelicInitializer


__all__ = [
    "AbstractInitializer",
    "INITIALIZERS",
]

INITIALIZERS: List[AbstractInitializer] = [
    ContainerInitializer,
    ApiInitializer,
    NewrelicInitializer,
]
