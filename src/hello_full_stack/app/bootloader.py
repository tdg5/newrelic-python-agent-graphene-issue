"""
Bootloader module managing the lifetime of the singleton app instance,
including initialization.
"""

from typing import Dict, List
from threading import Lock

from hello_full_stack.app import App
from hello_full_stack.app.initializers import (
    AbstractInitializer,
    INITIALIZERS,
)


_SINGLETON: App = None
_LOCK: Lock = Lock()


def boot() -> App:
    """
    Boot the app by creating an app instance and executing all the initializers.
    Subsequent calls to boot yield the previously constructed App instance.
    """
    global _SINGLETON
    if _SINGLETON is None:
        with _LOCK:
            if _SINGLETON is None:
                _SINGLETON = App()
                _execute_all_initializers(_SINGLETON, INITIALIZERS)
    return _SINGLETON


def _execute_all_initializers(
    app: App,
    initializers: List[AbstractInitializer],
) -> List[Dict[str, str]]:
    """
    Execute all the given initializers.

    :param app: The app instance that should be given to the initializers.
    :param initializers: The initializers that should be executed.
    """
    return [
        initializer.execute(app) for initializer in initializers
    ]
