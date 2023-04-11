"""
Config for the application.
"""

from test_proj.app.app_mode import AppMode
from pydantic import BaseSettings, validator


class Config(BaseSettings):
    """
    Config for the application.
    """

    app_mode: AppMode

    @validator("app_mode", pre=True)
    def _validate_app_mode(cls, value: str) -> AppMode:
        return AppMode(value)

    class Config:
        env_prefix: str = "TEST_PROJ_"

