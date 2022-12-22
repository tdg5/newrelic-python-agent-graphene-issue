"""
Example/template implementation of an API microservice.
"""


from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter as ApiRouter
from fastapi import Depends

from hello_full_stack.app import Config, RootContainer


router: ApiRouter = ApiRouter()


@router.get("/.nm/info")
@inject
async def hello_full_stack(
    config: Config = Depends(Provide[RootContainer.config]),
):
    """Minimal example GET endpoint."""
    return {
        "gitSha": config.git_sha,
        "message": config.message,
        "name": config.name,
        "region": config.region,
        "stage": config.stage.value,
        "vendor": config.vendor.value,
        "version": config.version,
    }
