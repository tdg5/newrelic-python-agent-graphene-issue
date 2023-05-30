import os

from fastapi import FastAPI

from app.graphql.query import schema
from starlette_graphene3 import GraphQLApp


def create_app():
    description = "Thing API"

    if os.getenv("NEW_RELIC_LICENSE_KEY"):
        import newrelic.agent
        newrelic.agent.initialize("./newrelic.ini")

    app = FastAPI(
        title="Thing API",
        openapi_url="/openapi.json",
        docs_url="/docs/",
        description=description,
        redoc_url=None,
    )
    app.mount("/", GraphQLApp(schema))
    return app
