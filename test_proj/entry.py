"""
Example/template implementation of an API microservice.
"""


from test_proj.app import App, AppMode, Config
from test_proj.app.bootloader import boot


config: Config = Config()
app: App = boot(config=config)

if config.app_mode == AppMode.API:
    from test_proj.entry_points.api import webserver

    webserver.run(app.api)
else:
    raise RuntimeError(
        f"'{config.app_mode.value}' is not a currently supported runtime AppMode."
    )
