"""
A class to handle fairly broad, application-wide concerns like configuration,
initialization, and other application lifetime concerns.

Typically, a singleton is used, but other instances can be created for testing
purposes.
"""

from fastapi import FastAPI
from typing import Optional
from hello_full_stack.app.config import Config

class App:
    """
    An instance of the App.
    """

    _api: FastAPI = None
    _config: Config = None

    def __init__(self):
        self._api = None
        self._config = None

    @property
    def api(self) -> FastAPI:
        """
        Return the API instance for the app.
        """
        return self._api

    @api.setter
    def api(self, api: FastAPI) -> None:
        self._api = api

    @property
    def config(self) -> Config:
        """
        Return the Config instance for the app.
        """
        return self._config

    @config.setter
    def config(self, config: Config) -> None:
        self._config = config

