from core import Logger

if __name__ == "__main__":
    logger = Logger("TestLogger")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    exit(0)