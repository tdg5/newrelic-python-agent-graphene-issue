"""
Example/template implementation of an API microservice.
"""


from hello_full_stack.app import App, AppMode, Config
from hello_full_stack.app.bootloader import boot


config: Config = Config()
app: App = boot(config=config)

if config.app_mode == AppMode.API:
    from hello_full_stack.entry_points.api import webserver

    webserver.run(app.api)
else:
    raise RuntimeError(
        f"'{config.app_mode.value}' is not a currently supported runtime AppMode."
    )
