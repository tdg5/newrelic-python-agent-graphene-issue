"""
Router for graphQL operations.
"""

from typing import Dict

from fastapi import APIRouter as ApiRouter
from starlette.background import BackgroundTasks
from starlette.requests import HTTPConnection
from starlette_graphene3 import (  # type: ignore[import]
    GraphQLApp,
    make_graphiql_handler,
)
import graphene


class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    me = graphene.Field(User)

    def resolve_me(root, info):
        return {"id": "john", "name": "John"}


SCHEMA = graphene.Schema(query=Query)


async def _context_factory(
    request: HTTPConnection,
) -> Dict:
    return {
        "background": BackgroundTasks(),
        "request": request,
    }


router: ApiRouter = ApiRouter()

graphql_app = GraphQLApp(
    context_value=_context_factory,
    on_get=make_graphiql_handler(),
    schema=SCHEMA,
)

router.add_route("/v1/graphql", graphql_app)
