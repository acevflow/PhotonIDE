"""Configuration constants and shared state for the logging system."""

COLORS = {
    "debug": "\033[90m",
    "info": "\033[34m",
    "warning": "\033[33m",
    "error": "\033[31m",
    "critical": "\033[91m",
}
"""ANSI color codes associated with each supported log level."""

VALID_LEVELS = set(COLORS.keys())
"""Set of supported log severity levels."""

RESET_COLOR = "\033[0m"
"""ANSI escape code that resets terminal text formatting."""

log_file_path = ""
"""Path to the log file shared by all logger instances."""

logger_initialized = False
"""Indicates whether the logging system has completed its initial setup."""

log_to_file_enabled = True
"""Indicates whether file logging is enabled."""