"""
Example/template implementation of an API microservice.
"""


from fastapi import APIRouter as ApiRouter


router: ApiRouter = ApiRouter()


@router.get("/")
async def root():
    """
    Dummy root endpoint for readiness and liveness checks.
    """
    return {}
