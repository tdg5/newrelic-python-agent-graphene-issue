"""
Dependency injection container bringing all the other containers together for
application use.
"""

from dependency_injector import containers, providers

from hello_full_stack.app.config import Config


class RootContainer(containers.DeclarativeContainer):
    config: providers.Dependency[Config] = providers.Dependency()