"""Application entry point for PhotonIDE.

Initializes the logging system, configures the main application window,
and starts the Tkinter event loop.
"""

import tkinter

from core import Logger

def main() -> None:
    """Initialize and run the PhotonIDE application."""
    logger = Logger("PhotonIDE")

    logger.info("Starting PhotonIDE application")
    logger.debug("Entering main()")

    try:
        # Create the main application window.
        logger.debug("Creating the main Tkinter window")
        root = tkinter.Tk()
        logger.debug("Main Tkinter window created successfully")

        # Configure the application window title.
        logger.debug("Setting application window title")
        root.title("PhotonIDE")
        logger.info("Application window title set to 'PhotonIDE'")

        # Define the initial window dimensions.
        window_width = 1000
        window_height = 600

        logger.debug(
            f"Configured initial window dimensions: "
            f"{window_width}x{window_height}"
        )

        # Retrieve screen dimensions to calculate the window position.
        logger.debug("Retrieving screen dimensions")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        logger.debug(
            f"Screen dimensions retrieved: "
            f"{screen_width}x{screen_height}"
        )

        logger.debug("Calculating window position")
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        logger.debug(f"Calculated window position: x={x}, y={y}")

        # Position the window at the center of the primary screen.
        logger.debug("Applying window geometry")
        root.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )
        logger.info(
            f"Window geometry configured: "
            f"{window_width}x{window_height} at ({x}, {y})"
        )

        # Set the minimum dimensions allowed when resizing the window.
        min_width = 800
        min_height = 500

        logger.debug(
            f"Setting minimum window dimensions: "
            f"{min_width}x{min_height}"
        )
        root.minsize(min_width, min_height)

        # Register the callback for the window's close event.
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

    except tkinter.TclError as error:
        logger.critical(
            f"A Tkinter error occurred during application execution: "
            f"{error}"
        )
        raise

    except Exception as error:
        logger.critical(
            f"An unexpected error occurred in PhotonIDE: "
            f"{type(error).__name__}: {error}"
        )
        raise

def on_close(root: tkinter.Tk, logger: Logger) -> None:
    """Handle the main window's close event.

    Args:
        root: The main Tkinter application window.
        logger: Logger instance used to record shutdown events.
    """
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