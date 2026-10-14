import datetime
import os

COLORS = {
    "debug": "\033[90m",
    "info": "\033[34m",
    "warning": "\033[33m",
    "error": "\033[31m",
    "critical": "\033[91m"
}

VALID_LEVELS = set(COLORS.keys())
RESET_COLOR = "\033[0m"

log_file_path = ""
logger_initialized = False
log_to_file_enabled = True


class Logger:
    def __init__(self, name: str):
        global log_file_path
        global logger_initialized
        global log_to_file_enabled

        self.name = name

        if logger_initialized:
            return

        logger_initialized = True

        try:
            os.makedirs("logs", exist_ok=True)
        except OSError as e:
            log_to_file_enabled = False
            self._print_internal_error(
                f"Failed to create logs directory: {e}. "
                "Logging to file will be disabled."
            )
            self._log_internal("Logger initialized with console logging only.", "warning")
            return

        log_file_path = os.path.join("logs", self.get_file_name())

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
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_file_name(self) -> str:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"{timestamp}.log"

    def _print_internal_error(self, message: str):
        formatted_message = (
            f"[ERROR] [{self.get_timestamp()}] [Logging] {message}"
        )
        print(f"{COLORS['error']}{formatted_message}{RESET_COLOR}")

    def _log_message(self, name: str, message: str, level: str = "info"):
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
        self._log_message("Logging", message, level)

    def log(self, message: str, level: str = "info"):
        self._log_message(self.name, message, level)

    def debug(self, message: str):
        self.log(message, "debug")

    def info(self, message: str):
        self.log(message, "info")

    def warning(self, message: str):
        self.log(message, "warning")

    def error(self, message: str):
        self.log(message, "error")

    def critical(self, message: str):
        self.log(message, "critical")