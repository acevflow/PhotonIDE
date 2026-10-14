# Logging Configuration

## Overview

The `config.py` module defines the configuration constants and shared state used by the PhotonIDE logging system. It centralizes severity levels, ANSI terminal colors, and the variables that control logging initialization and file output.

## Responsibilities

- Define the supported log severity levels.
- Associate each severity level with a console color.
- Provide the ANSI escape code used to reset terminal formatting.
- Maintain the shared state required by all `Logger` instances.
- Track the current log file and whether file logging is enabled.

## Configuration Reference

### `COLORS`

```python
COLORS = {
    "debug": "\033[90m",
    "info": "\033[34m",
    "warning": "\033[33m",
    "error": "\033[31m",
    "critical": "\033[91m",
}
```

A dictionary mapping each supported severity level to its ANSI color code.

| Level | Color |
|---|---|
| `debug` | Gray |
| `info` | Blue |
| `warning` | Yellow |
| `error` | Red |
| `critical` | Bright red |

These codes are used to distinguish log messages in terminal output.

### `VALID_LEVELS`

```python
VALID_LEVELS = set(COLORS.keys())
```

A set containing the supported severity levels. It is derived from `COLORS` to keep the available levels consistent with their color definitions.

### `RESET_COLOR`

```python
RESET_COLOR = "\033[0m"
```

The ANSI escape code that resets terminal text formatting after a colored message has been printed.

### `log_file_path`

```python
log_file_path = ""
```

Stores the path to the log file shared by all logger instances. It is assigned during logging initialization.

### `logger_initialized`

```python
logger_initialized = False
```

Indicates whether the logging system has started its initialization process. It prevents subsequent `Logger` instances from repeating the initial setup.

### `log_to_file_enabled`

```python
log_to_file_enabled = True
```

Controls whether messages are written to the log file. If file creation or writing fails, the logging system disables file output while retaining console logging.

## Shared State

The module-level variables are shared across imports of this module within the same Python process. They allow separate `Logger` instances to use the same configuration and output destination.

The state variables have the following roles:

| Variable | Purpose |
|---|---|
| `log_file_path` | Identifies the shared log file. |
| `logger_initialized` | Tracks whether initialization has started. |
| `log_to_file_enabled` | Controls file output availability. |

These variables are managed by the logging implementation and should not normally need to be modified directly by application components.

## Design Considerations

- **Centralized configuration:** Severity levels and their associated colors are defined in one place.
- **Shared state:** All logger instances use the same initialization status and file output configuration.
- **Console fallback:** Disabling file logging does not disable console output.
- **No external dependencies:** The module uses standard Python values and ANSI escape sequences.

## Related Modules

- [`formatters.py`](formatters.md) — Formats timestamps, filenames, and log messages.
- [`handlers.py`](handlers.md) — Manages console output, file writing, and initialization.
- [`logger.py`](logger.md) — Provides the `Logger` interface used by application components.
