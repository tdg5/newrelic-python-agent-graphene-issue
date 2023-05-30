import os

from fastapi import FastAPI

from app.core.config import settings
from app.graphql.query import schema
from starlette_graphene3 import GraphQLApp


def create_app():
    description = f"{settings.PROJECT_NAME} API"

    if os.getenv("NEW_RELIC_LICENSE_KEY"):
        import newrelic.agent
        newrelic.agent.initialize("./newrelic.ini")

    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_PATH}/openapi.json",
        docs_url="/docs/",
        description=description,
        redoc_url=None,
    )
    app.mount("/", GraphQLApp(schema))
    return app
