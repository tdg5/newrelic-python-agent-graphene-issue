"""
Initializer that sets up the API.
"""

import logging
import os
from typing import Dict

import newrelic.agent  # type: ignore

from test_proj.app import App
from test_proj.app.initializers.abstract_initializer import AbstractInitializer


logger = logging.getLogger(__name__)


class _NewrelicInitializer(AbstractInitializer):
    """
    Initializer that sets up the API.
    """

    def describe(self, app: App) -> str:
        return "Initialize Newrelic agent."

    def execute(self, app: App) -> Dict[str, str]:
        if os.getenv("NEW_RELIC_LICENSE_KEY") and os.getenv("NEW_RELIC_APP_NAME"):
            newrelic.agent.initialize("./newrelic.ini")

        return {
            "description": self.describe(app),
            "isSuccess": "true",
            "name": self.name,
        }


NewrelicInitializer = _NewrelicInitializer()
