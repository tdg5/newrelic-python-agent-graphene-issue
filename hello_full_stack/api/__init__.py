from .health_check_router import router as health_check_router
from .nm_router import router as nm_router


ROUTERS = [
    health_check_router,
    nm_router,
]

__all__ = [
    "ROUTERS",
    "health_check_router",
    "nm_router",
]
