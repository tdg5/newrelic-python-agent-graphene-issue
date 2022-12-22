"""
Router for health, liveness, and readiness check endpoints.
"""


from fastapi import APIRouter as ApiRouter


router: ApiRouter = ApiRouter()


@router.get("/health/healthz")
async def health_check():
    """
    Dummy endpoint for health check.
    """
    return {}


@router.get("/health/livez")
async def liveness_check():
    """
    Dummy endpoint for liveness check.
    """
    return {}


@router.get("/health/readyz")
async def readiness_check():
    """
    Dummy endpoint for readiness check.
    """
    return {}
