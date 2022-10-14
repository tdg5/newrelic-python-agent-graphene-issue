"""
Config for the application.
"""

from pydantic import validator

from hello_full_stack.app.app_mode import AppMode
from nm_toolkit.app_config import AppConfig, AppTargetEnvConfig  # type: ignore[import]


class Config(AppConfig):
    """
    Config for the application.
    """

    app_mode: AppMode
    message: str
    name: str

    @validator("app_mode", pre=True)
    def _validate_app_mode(cls, value: str) -> AppMode:
        return AppMode(value)

    class Config:
        at_least_one_target_env_spec_required = False
        env_prefix: str = "HELLO_FULL_STACK_"

    class TargetEnvConfig(AppTargetEnvConfig):
        """
        Config for the application for a specific environment that the
        application targets.
        """

        pass
