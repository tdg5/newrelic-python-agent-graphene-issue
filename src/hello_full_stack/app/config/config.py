"""
Config for the application.
"""

import os
from typing import Any, Dict, Tuple

import yaml
from pydantic import BaseSettings
from pydantic.env_settings import SettingsSourceCallable


def yaml_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    config = settings.__config__
    yaml_config_path = config.yaml_config_path  # type: ignore[attr-defined]
    if yaml_config_path is None or not os.path.exists(yaml_config_path):
        return {}
    with open(yaml_config_path, mode="r", encoding="utf-8") as stream:
        yaml_config = yaml.safe_load(stream)
    return yaml_config


class Config(BaseSettings):
    """
    Config for the application.
    """

    message: str
    name: str
    version: str

    class Config:
        # Allow env variables to be all uppercase.
        case_sensitive: bool = False
        # Allow for passing nested data in the environment using the delimiter.
        env_nested_delimiter: str = "__"
        # Only consider env variables that start with the given prefix.
        env_prefix: str = "HELLO_FULL_STACK_"

        secrets_dir: str = os.getenv(
            f"{env_prefix}SECRETS_DIR_PATH",
            "/var/run",
        )

        # Load the yaml config file from the env, or use a default.
        yaml_config_path: str = os.getenv(
            f"{env_prefix}YAML_CONFIG_PATH",
            "/tmp/config.yaml",
        )

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
                yaml_config_settings_source,
            )
