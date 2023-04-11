"""
Defines the interface that must be implemented by all initializers.
"""

from abc import ABCMeta, abstractmethod
from typing import Dict

from test_proj.app import App


class AbstractInitializer(metaclass=ABCMeta):
    """
    Defines the interface that must be implemented by all initializers.
    """

    @abstractmethod
    def describe(self, app: App) -> str:
        """
        Yields a description of what the initializer will accomplish when
        executed.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self, app: App) -> Dict[str, str]:
        """
        Perform whatever actions are necessary for the initializer to
        accomplish its goals. Side effects are expected.

        Concrete subclasses are expected to handle errors. Any raised errors
        will be treated as a fatal.
        """
        raise NotImplementedError

    @property
    def name(self) -> str:
        """
        Yields a name for the initializer.
        """
        return type(self).__name__
