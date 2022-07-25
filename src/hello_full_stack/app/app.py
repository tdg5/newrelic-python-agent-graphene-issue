"""
A class to handle fairly broad, application-wide concerns like configuration,
initialization, and other application lifetime concerns.

Typically, a singleton is used, but other instances can be created for testing
purposes.
"""

from typing import Optional, cast

from fastapi import FastAPI

from hello_full_stack.app.config import Config
from hello_full_stack.app.containers import RootContainer


class App:
    """
    An instance of the App.
    """

    _api: Optional[FastAPI]
    _container: Optional[RootContainer]
    config: Config

    def __init__(self, config: Config):
        self._api = None
        self.config = config

    @property
    def api(self) -> FastAPI:
        """
        Return the API instance for the app.
        """
        return cast(FastAPI, self._api)

    @api.setter
    def api(self, api: FastAPI) -> None:
        self._api = api

    @property
    def container(self) -> Optional[RootContainer]:
        """
        Return the RootContainer instance for the app.
        """
        return self._container

    @container.setter
    def container(self, root_container: RootContainer) -> None:
        self._container = root_container
