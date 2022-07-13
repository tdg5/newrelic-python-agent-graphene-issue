"""
Example/template implementation of an API microservice.
"""


from fastapi import FastAPI
from hello_full_stack.app import App
from hello_full_stack.app.bootloader import boot


app: App = boot()
api: FastAPI = app.api


@api.get("/")
async def hello_full_stack():
    """Minimal example GET endpoint."""
    return {
        "message": app.config.message,
        "name": app.config.name,
        "version": app.config.version,
    }
