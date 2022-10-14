import asyncio
from os import path

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config


def run(api: FastAPI) -> None:
    config_path = path.join(
        path.dirname(path.realpath(__file__)),
        "hypercorn_conf.py",
    )
    config = Config.from_pyfile(config_path)
    asyncio.run(serve(api, config))  # type: ignore[arg-type]
