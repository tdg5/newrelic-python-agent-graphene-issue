"""
Example/template implementation of an API microservice.
"""


from fastapi import FastAPI

from hello_full_stack.app import App, Config
from hello_full_stack.app.bootloader import boot


config: Config = Config()
app: App = boot(config=config)
api: FastAPI = app.api
