from .app_router import router as app_router
from .nm_router import router as nm_router


ROUTERS = [
    app_router,
    nm_router,
]

__all__ = [
    "ROUTERS",
    "app_router",
    "nm_router",
]
