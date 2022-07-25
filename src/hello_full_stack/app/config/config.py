"""
Config for the application.
"""

import os
from typing import Optional, Tuple

from pydantic import BaseSettings, validator
from pydantic.env_settings import SettingsSourceCallable

from nm_toolkit.deploy_env import DeployEnv, Stage, Vendor  # type: ignore[import]
from nm_toolkit.pydantic import YamlConfigSettingsSource  # type: ignore[import]


class Config(BaseSettings):
    """
    Config for the application.
    """

    _deploy_env: DeployEnv

    git_sha: str
    message: str
    name: str
    region: str
    stage: Stage
    vendor: Vendor
    version: str

    yaml_config_path: Optional[str]

    def __init__(self, *args, **kwargs):
        # Allow the secrets dir to be provided as an environment var
        if "_secrets_dir" not in kwargs:
            secrets_dir_from_env = os.getenv(
                f"{self.__config__.env_prefix}SECRETS_DIR_PATH",
                None,
            )
            if secrets_dir_from_env:
                kwargs["_secrets_dir"] = secrets_dir_from_env

        # Allow the yaml config path to be provided as an environment var
        if "yaml_config_path" not in kwargs:
            yaml_config_path_from_env = os.getenv(
                f"{self.__config__.env_prefix}YAML_CONFIG_PATH",
                None,
            )
            if yaml_config_path_from_env:
                kwargs["yaml_config_path"] = yaml_config_path_from_env

        super().__init__(*args, **kwargs)

        deploy_env = DeployEnv(
            region=self.region,
            stage=self.stage,
            vendor=self.vendor,
        )
        object.__setattr__(self, "_deploy_env", deploy_env)

    @validator("stage", pre=True)
    def _validate_stage(cls, value: str) -> Stage:
        """
        Try to convert a stage value into a Stage enum.
        """
        return Stage(value)

    @validator("vendor", pre=True)
    def _validate_vendor(cls, value: str) -> Vendor:
        """
        Try to convert a vendor value into a Vendor enum.
        """
        return Vendor(value)

    @property
    def deploy_env(self) -> DeployEnv:
        return self._deploy_env

    class Config:
        # Allow env variables to be all uppercase.
        case_sensitive: bool = False
        # Allow for passing nested data in the environment using the delimiter.
        env_nested_delimiter: str = "__"
        # Only consider env variables that start with the given prefix.
        env_prefix: str = "HELLO_FULL_STACK_"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> Tuple[SettingsSourceCallable, ...]:
            return (
                init_settings,
                env_settings,
                file_secret_settings,
                YamlConfigSettingsSource(init_settings=init_settings),
            )
