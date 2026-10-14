import os

from . import config
from .formatters import format_message, get_file_name, get_timestamp

def print_internal_error(message: str):
    formatted_message = (
        f"[ERROR] [{get_timestamp()}] [Logging] {message}"
    )
    print(
        f"{config.COLORS['error']}"
        f"{formatted_message}"
        f"{config.RESET_COLOR}"
    )

def initialize_logging(logger):
    try:
        os.makedirs("logs", exist_ok=True)
    except OSError as e:
        config.log_to_file_enabled = False
        print_internal_error(
            f"Failed to create logs directory: {e}. "
            "Logging to file will be disabled."
        )
        logger._log_internal(
            "Logger initialized with console logging only.",
            "warning",
        )
        return

    config.log_file_path = os.path.join("logs", get_file_name())

    try:
        with open(
            config.log_file_path,
            "w",
            encoding="utf-8",
        ) as log_file:
            log_file.write(
                f"Log file created at {get_timestamp()}\n"
            )
    except OSError as e:
        config.log_to_file_enabled = False
        print_internal_error(
            f"Failed to create log file: {e}. "
            "Logging to file will be disabled."
        )

    logger._log_internal("Logger initialized", "info")


def log_message(logger, name: str, message: str, level: str = "info"):
    level = level.lower()

    if level not in config.VALID_LEVELS:
        raise ValueError(f"Invalid log level: {level}")

    formatted_message = format_message(name, message, level)

    print(
        f"{config.COLORS[level]}"
        f"{formatted_message}"
        f"{config.RESET_COLOR}"
    )

    if not config.log_to_file_enabled:
        return

    try:
        with open(
            config.log_file_path,
            "a",
            encoding="utf-8",
        ) as log_file:
            log_file.write(f"{formatted_message}\n")
    except OSError as e:
        config.log_to_file_enabled = False
        logger._print_internal_error(
            f"Failed to write to log file: {e}. "
            "Logging to file will be disabled."
        )