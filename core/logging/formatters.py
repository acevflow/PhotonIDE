import datetime

def get_timestamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_file_name() -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{timestamp}.log"

def format_message(name: str, message: str, level: str = "info") -> str:
    return (
        f"[{level.upper()}] "
        f"[{get_timestamp()}] "
        f"[{name}] {message}"
    )