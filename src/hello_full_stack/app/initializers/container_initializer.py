"""
Initializer that sets up the application's root dependency injector container.
"""

from typing import Dict

from hello_full_stack.app import App, RootContainer

from .abstract_initializer import AbstractInitializer


class _ContainerInitializer(AbstractInitializer):
    """
    Initializer that sets up the application's root dependency injector
    container.
    """

    def describe(self, app: App) -> str:
        return "Initialize application dependency injector container."

    def execute(self, app: App) -> Dict[str, str]:
        container = RootContainer(config=app.config)
        container.init_resources()
        container.wire(
            packages=[
                "hello_full_stack.api",
            ]
        )
        app.container = container
        return {
            "description": self.describe(app),
            "isSuccess": "true",
            "name": self.name,
        }


ContainerInitializer = _ContainerInitializer()
