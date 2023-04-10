"""
Export an ordered list of all the app initializers.
"""

from typing import List

from hello_full_stack.app.initializers.abstract_initializer import AbstractInitializer
from hello_full_stack.app.initializers.api_initializer import ApiInitializer
from hello_full_stack.app.initializers.container_initializer import ContainerInitializer
from hello_full_stack.app.initializers.logger_initializer import LoggerInitializer
from hello_full_stack.app.initializers.newrelic_initializer import NewrelicInitializer


__all__ = [
    "AbstractInitializer",
    "INITIALIZERS",
]

# Order is important! Initializers are executed in the order defined below.
INITIALIZERS: List[AbstractInitializer] = [
    LoggerInitializer,
    ContainerInitializer,
    ApiInitializer,
    NewrelicInitializer,
]
