"""
Config for the application.
"""

from typing import List

from nm_toolkit.service_foundation.app_config import AppConfig, AppTargetEnvConfig
from pydantic import validator

from hello_full_stack.app.app_mode import AppMode


class Config(AppConfig):
    """
    Config for the application.
    """

    app_mode: AppMode
    logging_app_log_level: str = "INFO"
    logging_format: str = "%(levelname)-8s %(message)s %(name)s.%(funcName)s"
    logging_handlers: List[str] = ["default"]
    logging_web_server_log_level: str = "INFO"
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
