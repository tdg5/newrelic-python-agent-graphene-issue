"""
Initializer that sets up the API.
"""

from typing import Dict

from fastapi import FastAPI

from test_proj.api import ROUTERS
from test_proj.app import App

from .abstract_initializer import AbstractInitializer


class _ApiInitializer(AbstractInitializer):
    """
    Initializer that sets up the API.
    """

    def describe(self, app: App) -> str:
        return "Initialize FastAPI."

    def execute(self, app: App) -> Dict[str, str]:
        api = FastAPI(
            container=app.container,
            description="Example/template implementation of an API microservice.",
            title="test_proj",
        )
        for router in ROUTERS:
            api.include_router(router)
        app.api = api
        return {
            "description": self.describe(app),
            "isSuccess": "true",
            "name": self.name,
        }


ApiInitializer = _ApiInitializer()
