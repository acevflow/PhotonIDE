COLORS = {
    "debug": "\033[90m",
    "info": "\033[34m",
    "warning": "\033[33m",
    "error": "\033[31m",
    "critical": "\033[91m",
}

VALID_LEVELS = set(COLORS.keys())
RESET_COLOR = "\033[0m"

log_file_path = ""
logger_initialized = False
log_to_file_enabled = True