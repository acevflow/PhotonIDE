COLORS = {
    "debug": "\033[90m",
    "info": "\033[34m",
    "warning": "\033[33m",
    "error": "\033[31m",
    "critical": "\033[91m"
}

class Logger:
    def __init__(self, name: str):
        self.name = name
        
    def log(self, message: str, level: str = "info"):
        color = COLORS.get(level, "")
        print(f"{color}[{level.upper()}] [{self.name}] {message}\033[0m")
        
        
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