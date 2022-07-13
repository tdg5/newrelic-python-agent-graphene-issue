"""
Initializer that sets up the application config.
"""

from typing import Dict

from hello_full_stack.app import App
from hello_full_stack.app.config import Config

from .abstract_initializer import AbstractInitializer


class _ConfigInitializer(AbstractInitializer):
    """
    Initializer that sets up the application config.
    """

    def describe(self, app: App) -> str:
        return "Initialize application config."

    def execute(self, app: App) -> Dict[str, str]:
        app.config = Config()
        return {
            "description": self.describe(app),
            "isSuccess": "true",
            "name": self.name,
        }


ConfigInitializer = _ConfigInitializer()
