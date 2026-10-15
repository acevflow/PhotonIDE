import tkinter

from core import Logger

def main() -> None:
    logger = Logger("PhotonIDE")

    logger.info("Starting PhotonIDE application")
    logger.debug("Entering main()")

    try:
        logger.debug("Creating the main Tkinter window")
        root = tkinter.Tk()
        logger.debug("Main Tkinter window created successfully")

        logger.debug("Setting application window title")
        root.title("PhotonIDE")
        logger.info("Application window title set to 'PhotonIDE'")

        window_width = 1000
        window_height = 600

        logger.debug(
            f"Configured initial window dimensions: "
            f"{window_width}x{window_height}"
        )

        logger.debug("Retrieving screen dimensions")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        logger.debug(
            f"Screen dimensions retrieved: "
            f"{screen_width}x{screen_height}"
        )

        logger.debug("Calculating window position")
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        logger.debug(
            f"Calculated window position: x={x}, y={y}"
        )

        logger.debug("Applying window geometry")
        root.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )
        logger.info(
            f"Window geometry configured: "
            f"{window_width}x{window_height} at ({x}, {y})"
        )

        min_width = 800
        min_height = 500

        logger.debug(
            f"Setting minimum window dimensions: "
            f"{min_width}x{min_height}"
        )
        root.minsize(min_width, min_height)

        logger.debug("Registering window close event handler")
        root.protocol(
            "WM_DELETE_WINDOW",
            lambda: on_close(root, logger),
        )
        logger.debug("Window close event handler registered")

        logger.info("PhotonIDE window initialized successfully")
        logger.debug("Entering Tkinter main event loop")

        root.mainloop()

        logger.debug("Tkinter main event loop terminated")
        logger.info("PhotonIDE application terminated normally")

    except tkinter.TclError:
        logger.exception if False else None
        logger.critical(
            "A Tkinter error occurred while initializing or running "
            "the application"
        )
        raise

    except Exception as error:
        logger.critical(
            f"An unexpected error occurred in PhotonIDE: "
            f"{type(error).__name__}: {error}"
        )
        raise

def on_close(root: tkinter.Tk, logger: Logger) -> None:
    logger.info("Window close event received")
    logger.debug("Preparing to destroy the main window")

    try:
        root.destroy()
        logger.info("Main window destroyed successfully")
        logger.info("PhotonIDE window closed")

    except tkinter.TclError as error:
        logger.error(
            f"Tkinter error while closing the main window: {error}"
        )
        raise

    except Exception as error:
        logger.critical(
            f"Unexpected error while closing PhotonIDE: "
            f"{type(error).__name__}: {error}"
        )
        raise

if __name__ == "__main__":
    main()