"""
Config for the application.
"""

from nm_toolkit.app_config import AppConfig, AppTargetEnvConfig  # type: ignore[import]


class Config(AppConfig):
    """
    Config for the application.
    """

    message: str
    name: str

    class Config:
        at_least_one_target_env_spec_required = False
        env_prefix: str = "HELLO_FULL_STACK_"

    class TargetEnvConfig(AppTargetEnvConfig):
        """
        Config for the application for a specific environment that the
        application targets.
        """

        pass
