from .health_check_router import router as health_check_router
from .graphql_router import router as graphql_router

ROUTERS = [
    health_check_router,
    graphql_router,
]

__all__ = [
    "ROUTERS",
]
