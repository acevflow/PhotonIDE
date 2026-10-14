from . import config
from . import handlers
from .formatters import get_file_name, get_timestamp

class Logger:
    def __init__(self, name: str):
        self.name = name

        if config.logger_initialized:
            return

        config.logger_initialized = True
        handlers.initialize_logging(self)

    def get_timestamp(self) -> str:
        return get_timestamp()

    def get_file_name(self) -> str:
        return get_file_name()

    def _print_internal_error(self, message: str):
        handlers.print_internal_error(message)

    def _log_message(
        self,
        name: str,
        message: str,
        level: str = "info",
    ):
        handlers.log_message(self, name, message, level)

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