"""
Bootloader module managing the lifetime of the singleton app instance,
including initialization.
"""

from threading import Lock
from typing import Dict, List, Optional

from hello_full_stack.app import App
from hello_full_stack.app.config import Config
from hello_full_stack.app.initializers import INITIALIZERS, AbstractInitializer


_SINGLETON: Optional[App] = None
_LOCK: Lock = Lock()


def boot(config: Config) -> App:
    """
    Boot the app by creating an app instance and executing all the initializers.
    Subsequent calls to boot yield the previously constructed App instance.
    """
    global _SINGLETON
    if _SINGLETON is None:
        with _LOCK:
            if _SINGLETON is None:
                _SINGLETON = App(config=config)
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
    return [initializer.execute(app) for initializer in initializers]
