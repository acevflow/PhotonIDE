"""Formatting utilities for the PhotonIDE logging system.

Provides timestamp generation, log filename creation, and log message
formatting.
"""

import datetime

def get_timestamp() -> str:
    """Return the current local date and time.

    Returns:
        A timestamp formatted as YYYY-MM-DD HH:MM:SS.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_file_name() -> str:
    """Generate a log filename based on the current local time.

    Returns:
        A filename formatted as YYYY-MM-DD_HH-MM-SS.log.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{timestamp}.log"

def format_message(name: str, message: str, level: str = "info") -> str:
    """Format a log message with its severity, timestamp, and source.

    Args:
        name: Name of the component generating the message.
        message: Message content to record.
        level: Severity level associated with the message. Defaults to
            ``info``.

    Returns:
        The formatted message, including its severity level, timestamp,
        component name, and content.
    """
    return (
        f"[{level.upper()}] "
        f"[{get_timestamp()}] "
        f"[{name}] {message}"
    )