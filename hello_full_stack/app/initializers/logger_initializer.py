"""
Initializer that sets up the logger.
"""

from logging.config import dictConfig
from typing import Dict

from hello_full_stack.app import App
from hello_full_stack.app.initializers.abstract_initializer import (  # noqa: E501
    AbstractInitializer,
)


class _LoggerInitializer(AbstractInitializer):
    """
    Initializer that sets up the Logger.
    """

    def describe(self, app: App) -> str:
        return "Initialize Logger."

    def execute(self, app: App) -> Dict[str, str]:
        logging_app_log_level = app.config.logging_app_log_level
        logging_format = app.config.logging_format
        logging_handlers = app.config.logging_handlers
        logging_web_server_log_level = app.config.logging_web_server_log_level
        log_config = {
            "disable_existing_loggers": False,
            "filters": {},
            "formatters": {
                "default": {
                    "format": logging_format,
                    "style": "%",
                    "use_colors": True,
                },
                "json": {
                    "format": logging_format,
                    "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                },
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "filters": [],
                    "formatter": "default",
                    "level": logging_app_log_level,
                },
                "json": {
                    "class": "logging.StreamHandler",
                    "filters": [],
                    "formatter": "json",
                    "level": logging_app_log_level,
                },
                "null": {
                    "class": "logging.NullHandler",
                },
            },
            "loggers": {
                "fastapi": {
                    "handlers": ["null"],
                    "level": logging_web_server_log_level,
                    "propagate": False,
                },
                "hypercorn.access": {
                    "handlers": logging_handlers,
                    "level": logging_web_server_log_level,
                    "propagate": False,
                },
                "hypercorn.error.info": {
                    "handlers": logging_handlers,
                    "level": "ERROR",
                    "propagate": False,
                },
                "root": {
                    "handlers": logging_handlers,
                    "level": logging_app_log_level,
                    "propagate": True,
                },
            },
            "version": 1,
        }

        dictConfig(log_config)

        return {
            "description": self.describe(app),
            "isSuccess": "true",
            "name": self.name,
        }


LoggerInitializer = _LoggerInitializer()
