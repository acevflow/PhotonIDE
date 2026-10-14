import datetime
import os

COLORS = {
    "info": "\033[34m",
    "warning": "\033[33m",
    "debug": "\033[90m",
    "error": "\033[31m",
    "critical": "\033[91m"
}

log_file_path = ""

logger_initialized = False
log_to_file_enabled = True

class Logger:
    def get_timestamp(self) -> str:
            return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    
    def get_file_name(self) -> str:
        return self.get_timestamp().replace("/", "-").replace(":", "-").replace(" ", "_") + ".log"

    def __init__(self, name: str):
        global log_file_path
        global logger_initialized
        global log_to_file_enabled
        
        self.name = name
        
        if not logger_initialized:
            try:
                os.makedirs("logs", exist_ok=True)
            except Exception as e:
                print(f"Failed to create logs directory: {e}")
                log_to_file_enabled = False
                
            log_file_path = os.path.join("logs", self.get_file_name())
            
            try:
                with open(log_file_path, "w") as f:
                    f.write(f"Log file created at {self.get_timestamp()}\n")
            except Exception as e:
                print(f"Failed to create log file: {e}")
                log_to_file_enabled = False
                
            logger_initialized = True
        
    def log(self, message: str, level: str = "info"):
        global log_to_file_enabled
        
        message = f"[{level.upper()}] [{self.get_timestamp()}] [{self.name}] {message}"
        
        color = COLORS.get(level, "")
        print(f"{color}{message}\033[0m")
        
        if log_to_file_enabled:
            try:
                with open(log_file_path, "a") as f:
                    f.write(f"{message}\n")
            except Exception as e:
                print(f"Failed to write to log file: {e}")
                log_to_file_enabled = False

    def info(self, message: str):
        self.log(message, "info")
        
    def debug(self, message: str):
        self.log(message, "debug")
        
    def warning(self, message: str):
        self.log(message, "warning")
        
    def error(self, message: str):
        self.log(message, "error")
        
    def critical(self, message: str):
        self.log(message, "critical")