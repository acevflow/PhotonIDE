"""Application logging system for PhotonIDE.

Provides colored console output and optional file logging with support
for five severity levels.
"""

import datetime
import os

# ANSI escape codes used to distinguish log levels in the console.
COLORS = {
    "debug": "\033[90m",
    "info": "\033[34m",
    "warning": "\033[33m",
    "error": "\033[31m",
    "critical": "\033[91m",
}

# Valid severity levels are derived from the available color definitions.
VALID_LEVELS = set(COLORS.keys())
RESET_COLOR = "\033[0m"

# Shared state used by all Logger instances.
log_file_path = ""
logger_initialized = False
log_to_file_enabled = True


class Logger:
    """Log application messages to the console and a shared log file.

    The first instance initializes the logging system. Subsequent instances
    reuse the same configuration and log file while retaining their own
    component names.

    Args:
        name: Name of the application component associated with this logger.
    """

    def __init__(self, name: str):
        global log_file_path
        global logger_initialized
        global log_to_file_enabled

        self.name = name

        # Initialize the shared logging system only once.
        if logger_initialized:
            return

        logger_initialized = True

        # Create the directory used to store log files.
        try:
            os.makedirs("logs", exist_ok=True)
        except OSError as e:
            log_to_file_enabled = False
            self._print_internal_error(
                f"Failed to create logs directory: {e}. "
                "Logging to file will be disabled."
            )
            self._log_internal(
                "Logger initialized with console logging only.",
                "warning",
            )
            return

        log_file_path = os.path.join("logs", self.get_file_name())

        # Create the log file before accepting application messages.
        try:
            with open(log_file_path, "w", encoding="utf-8") as log_file:
                log_file.write(
                    f"Log file created at {self.get_timestamp()}\n"
                )
        except OSError as e:
            log_to_file_enabled = False
            self._print_internal_error(
                f"Failed to create log file: {e}. "
                "Logging to file will be disabled."
            )

        self._log_internal("Logger initialized", "info")

    def get_timestamp(self) -> str:
        """Return the current local date and time.

        Returns:
            A timestamp formatted as YYYY-MM-DD HH:MM:SS.
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_file_name(self) -> str:
        """Generate a log filename based on the current local time.

        Returns:
            A filename formatted as YYYY-MM-DD_HH-MM-SS.log.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"{timestamp}.log"

    def _print_internal_error(self, message: str):
        """Print an internal logging error directly to the console.

        This method bypasses file logging to prevent recursive failures
        when the logging system cannot access its output file.

        Args:
            message: Description of the internal logging error.
        """
        formatted_message = (
            f"[ERROR] [{self.get_timestamp()}] [Logging] {message}"
        )
        print(f"{COLORS['error']}{formatted_message}{RESET_COLOR}")

    def _log_message(self, name: str, message: str, level: str = "info"):
        """Format and output a message at the specified severity level.

        Messages are printed to the console and appended to the shared log
        file when file logging is enabled. A file-writing failure disables
        further file logging without interrupting console output.

        Args:
            name: Name of the component producing the message.
            message: Text to record.
            level: Severity level to use.

        Raises:
            ValueError: If the specified severity level is not supported.
        """
        global log_to_file_enabled

        level = level.lower()

        if level not in VALID_LEVELS:
            raise ValueError(f"Invalid log level: {level}")

        formatted_message = (
            f"[{level.upper()}] "
            f"[{self.get_timestamp()}] "
            f"[{name}] {message}"
        )

        print(f"{COLORS[level]}{formatted_message}{RESET_COLOR}")

        if not log_to_file_enabled:
            return

        try:
            with open(log_file_path, "a", encoding="utf-8") as log_file:
                log_file.write(f"{formatted_message}\n")
        except OSError as e:
            log_to_file_enabled = False
            self._print_internal_error(
                f"Failed to write to log file: {e}. "
                "Logging to file will be disabled."
            )

    def _log_internal(self, message: str, level: str = "info"):
        """Record a message generated by the logging system itself.

        Internal messages always use the component name ``Logging``.

        Args:
            message: Internal status or diagnostic message.
            level: Severity level to use.
        """
        self._log_message("Logging", message, level)

    def log(self, message: str, level: str = "info"):
        """Record a message using the current component's name.

        Args:
            message: Text to record.
            level: Severity level to use. Defaults to ``info``.
        """
        self._log_message(self.name, message, level)

    def debug(self, message: str):
        """Record a diagnostic message.

        Args:
            message: Detailed information useful for debugging.
        """
        self.log(message, "debug")

    def info(self, message: str):
        """Record a general informational message.

        Args:
            message: Information about normal application behavior.
        """
        self.log(message, "info")

    def warning(self, message: str):
        """Record a warning about a potentially problematic condition.

        Args:
            message: Description of the condition.
        """
        self.log(message, "warning")

    def error(self, message: str):
        """Record an error encountered during application execution.

        Args:
            message: Description of the error.
        """
        self.log(message, "error")

    def critical(self, message: str):
        """Record a critical error requiring immediate attention.

        Args:
            message: Description of the critical condition.
        """
        self.log(message, "critical")
