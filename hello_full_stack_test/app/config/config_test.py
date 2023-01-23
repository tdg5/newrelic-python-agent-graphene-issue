"""
Test the application config.
"""

import os
import shutil
import textwrap
from tempfile import NamedTemporaryFile
from typing import List, Optional

import pytest
import yaml
from nm_toolkit.service_foundation.deploy_env import DeployEnv, Stage, Vendor
from pydantic import ValidationError

from hello_full_stack.app.app_mode import AppMode
from hello_full_stack.app.config import Config
from hello_full_stack_test.test_helpers.locks import env_mutator


DEFAULT_APP_MODE = AppMode.API.value
DEFAULT_GIT_SHA = "some-git-sha"
DEFAULT_NAME = "some-name"
DEFAULT_LOGGING_APP_LOG_LEVEL = "logging-app-log-level"
DEFAULT_LOGGING_FORMAT = "logging-format"
DEFAULT_LOGGING_HANDLERS = ["logging-handlers"]
DEFAULT_LOGGING_WEB_SERVER_LOG_LEVEL = "web-server-log-level"
DEFAULT_MESSAGE = "some-message"
DEFAULT_REGION = "us-east-1"
DEFAULT_STAGE = Stage.DEV.value
DEFAULT_VENDOR = Vendor.AWS.value
DEFAULT_VERSION = "1.0.0"
DEFAULT_YAML_CONFIG_PATH = "/tmp/default_config.yaml"
DEFAULT_DEPLOY_ENV = DeployEnv(
    region=DEFAULT_REGION,
    stage=Stage(DEFAULT_STAGE),
    vendor=Vendor(DEFAULT_VENDOR),
)

YAML_TEMPLATE = """
app_mode: {app_mode}
git_sha: {git_sha}
message: {message}
logging_app_log_level: {logging_app_log_level}
logging_format: {logging_format}
logging_handlers:
{logging_handlers}
logging_web_server_log_level: {logging_web_server_log_level}
name: {name}
region: {region}
stage: {stage}
vendor: {vendor}
version: {version}
"""


def test_app_mode_is_accessible():
    app_mode = "api"
    subject = make_config(app_mode=app_mode)
    assert subject.app_mode == AppMode(app_mode)


def test_app_mode_is_required():
    with pytest.raises(ValueError) as exinfo:
        make_config(app_mode=None)
    ex_str = str(exinfo.value)
    assert ValueError == exinfo.type
    assert "AppMode" in ex_str
    assert "None is not a valid AppMode" in ex_str


def test_logging_app_log_level_is_accessible():
    logging_app_log_level = "logging_app_log_level_other"
    subject = make_config(logging_app_log_level=logging_app_log_level)
    assert subject.logging_app_log_level == logging_app_log_level


def test_logging_app_log_level_is_required():
    with pytest.raises(ValidationError) as exinfo:
        make_config(logging_app_log_level=None)
    ex_str = str(exinfo.value)
    assert ValidationError == exinfo.type
    assert "logging_app_log_level" in ex_str
    assert "none is not an allowed value" in ex_str


def test_logging_format_is_accessible():
    logging_format = "logging_format_other"
    subject = make_config(logging_format=logging_format)
    assert subject.logging_format == logging_format


def test_logging_format_is_required():
    with pytest.raises(ValidationError) as exinfo:
        make_config(logging_format=None)
    ex_str = str(exinfo.value)
    assert ValidationError == exinfo.type
    assert "logging_format" in ex_str
    assert "none is not an allowed value" in ex_str


def test_logging_handlers_is_accessible():
    logging_handlers = ["logging_handlers_other"]
    subject = make_config(logging_handlers=logging_handlers)
    assert subject.logging_handlers == logging_handlers


def test_logging_handlers_is_required():
    with pytest.raises(ValidationError) as exinfo:
        make_config(logging_handlers=None)
    ex_str = str(exinfo.value)
    assert ValidationError == exinfo.type
    assert "logging_handlers" in ex_str
    assert "none is not an allowed value" in ex_str


def test_logging_web_server_log_level_is_accessible():
    logging_web_server_log_level = "logging_web_server_log_level_other"
    subject = make_config(logging_web_server_log_level=logging_web_server_log_level)
    assert subject.logging_web_server_log_level == logging_web_server_log_level


def test_logging_web_server_log_level_is_required():
    with pytest.raises(ValidationError) as exinfo:
        make_config(logging_web_server_log_level=None)
    ex_str = str(exinfo.value)
    assert ValidationError == exinfo.type
    assert "logging_web_server_log_level" in ex_str
    assert "none is not an allowed value" in ex_str


def test_message_is_accessible():
    message = "message_other"
    subject = make_config(message=message)
    assert subject.message == message


def test_message_is_required():
    with pytest.raises(ValidationError) as exinfo:
        make_config(message=None)
    ex_str = str(exinfo.value)
    assert ValidationError == exinfo.type
    assert "message" in ex_str
    assert "none is not an allowed value" in ex_str


def test_name_is_accessible():
    name = "name_other"
    subject = make_config(name=name)
    assert subject.name == name


def test_name_is_required():
    with pytest.raises(ValidationError) as exinfo:
        make_config(name=None)
    ex_str = str(exinfo.value)
    assert ValidationError == exinfo.type
    assert "name" in ex_str
    assert "none is not an allowed value" in ex_str


def test_yaml_config_path_is_optional():
    subject = make_config(yaml_config_path=None)
    assert subject.yaml_config_path is None


@env_mutator
def test_sources_all_work_and_override_as_expected():
    stage_env_var = "HELLO_FULL_STACK_STAGE"
    expected_region = "us-west-1"
    expected_stage = Stage.PROD.value
    expected_vendor = Vendor.AZURE.value
    expected_version = "100.100.100"
    secrets_dir_path = "/tmp/hello_full_stack_app_config_sources_test"
    yaml = make_config_yaml(version=expected_version)

    original_env_stage = os.environ.get(stage_env_var)
    if not os.path.exists(secrets_dir_path):
        os.mkdir(secrets_dir_path)
    secret_file_path = os.path.join(secrets_dir_path, "hello_full_stack_vendor")
    with open(secret_file_path, mode="w", encoding="utf-8") as file:
        file.write(expected_vendor)

    try:
        os.environ[stage_env_var] = expected_stage
        with NamedTemporaryFile(mode="w+") as tmp_file:
            tmp_file.write(textwrap.dedent(yaml))
            # Need to rewind the temp file or it starts reading after the yaml
            tmp_file.file.seek(0)
            config = Config(
                # Init values should have highest priority.
                # Region (most importantly for this test) should come from init values.
                region=expected_region,
                # Env settings should have second highest priority
                # stage should come from env settings.
                # File secrets should have third highest priority
                # vendor should come from file secrets.
                _secrets_dir=secrets_dir_path,
                # Yaml config should have fourth highest priority (lowest priority).
                # version should come from yaml config.
                yaml_config_path=tmp_file.name,
            )
            assert expected_region == config.region
            assert expected_stage == config.stage.value
            assert expected_vendor == config.vendor.value
            assert expected_version == config.version
    finally:
        if os.path.exists(secrets_dir_path):
            shutil.rmtree(secrets_dir_path)
        if original_env_stage:
            os.environ[stage_env_var] = original_env_stage
        else:
            del os.environ[stage_env_var]


def make_config(
    app_mode: Optional[str] = DEFAULT_APP_MODE,
    git_sha: Optional[str] = DEFAULT_GIT_SHA,
    logging_app_log_level: Optional[str] = DEFAULT_LOGGING_APP_LOG_LEVEL,
    logging_format: Optional[str] = DEFAULT_LOGGING_FORMAT,
    logging_handlers: Optional[List[str]] = DEFAULT_LOGGING_HANDLERS,
    logging_web_server_log_level: Optional[str] = DEFAULT_LOGGING_WEB_SERVER_LOG_LEVEL,
    message: Optional[str] = DEFAULT_MESSAGE,
    name: Optional[str] = DEFAULT_NAME,
    region: Optional[str] = DEFAULT_REGION,
    stage: Optional[str] = DEFAULT_STAGE,
    vendor: Optional[str] = DEFAULT_VENDOR,
    version: Optional[str] = DEFAULT_VERSION,
    yaml_config_path: Optional[str] = DEFAULT_YAML_CONFIG_PATH,
) -> Config:
    return Config(
        app_mode=AppMode(app_mode),
        git_sha=git_sha,
        logging_app_log_level=logging_app_log_level,
        logging_format=logging_format,
        logging_handlers=logging_handlers,
        logging_web_server_log_level=logging_web_server_log_level,
        message=message,
        name=name,
        region=region,
        stage=stage,
        vendor=vendor,
        version=version,
        yaml_config_path=yaml_config_path,
    )


def make_config_yaml(
    app_mode: str = DEFAULT_APP_MODE,
    git_sha: str = DEFAULT_GIT_SHA,
    logging_app_log_level: str = DEFAULT_LOGGING_APP_LOG_LEVEL,
    logging_format: str = DEFAULT_LOGGING_FORMAT,
    logging_handlers: List[str] = DEFAULT_LOGGING_HANDLERS,
    logging_web_server_log_level: str = DEFAULT_LOGGING_WEB_SERVER_LOG_LEVEL,
    message: str = DEFAULT_MESSAGE,
    name: str = DEFAULT_NAME,
    region: str = DEFAULT_REGION,
    stage: str = DEFAULT_STAGE,
    vendor: str = DEFAULT_VENDOR,
    version: str = DEFAULT_VERSION,
) -> str:
    logging_handlers_yaml = yaml.safe_dump(logging_handlers)
    return YAML_TEMPLATE.format(
        app_mode=app_mode,
        git_sha=git_sha,
        name=name,
        logging_app_log_level=logging_app_log_level,
        logging_format=logging_format,
        logging_handlers=logging_handlers_yaml,
        logging_web_server_log_level=logging_web_server_log_level,
        message=message,
        region=region,
        stage=stage,
        vendor=vendor,
        version=version,
    )
