# Logging Formatters

## Overview

The `formatters.py` module provides utility functions for generating timestamps, creating log filenames, and formatting log messages. It keeps formatting logic separate from the logging interface and output handlers.

## Responsibilities

- Generate timestamps using the local system date and time.
- Create filenames for log files.
- Format log messages consistently before they are sent to the configured output destinations.

## API Reference

### `get_timestamp()`

```python
get_timestamp() -> str
```

Returns the current local date and time as a string.

**Return format:**

```text
YYYY-MM-DD HH:MM:SS
```

**Example:**

```python
timestamp = get_timestamp()
print(timestamp)
```

Example output:

```text
2026-10-14 14:30:25
```

The output depends on the local system clock.

### `get_file_name()`

```python
get_file_name() -> str
```

Generates a log filename based on the current local date and time.

**Return format:**

```text
YYYY-MM-DD_HH-MM-SS.log
```

**Example:**

```python
filename = get_file_name()
print(filename)
```

Example output:

```text
2026-10-14_14-30-25.log
```

The function returns only the filename, not its directory path.

### `format_message(name, message, level="info")`

```python
format_message(
    name: str,
    message: str,
    level: str = "info",
) -> str
```

Formats a log message using its severity level, timestamp, component name, and content.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `name` | `str` | Name of the component generating the message. |
| `message` | `str` | Content of the message. |
| `level` | `str` | Severity level. Defaults to `info`. |

**Return format:**

```text
[LEVEL] [YYYY-MM-DD HH:MM:SS] [COMPONENT] Message content
```

**Example:**

```python
message = format_message(
    name="Editor",
    message="Document saved successfully.",
    level="info",
)

print(message)
```

Example output:

```text
[INFO] [2026-10-14 14:30:25] [Editor] Document saved successfully.
```

The severity level is converted to uppercase in the formatted output. Level validation is handled by the output handler rather than by this function.

## Dependencies

The module uses Python's standard `datetime` library to obtain the current local date and time.

It also relies on the logging configuration and handlers indirectly through the functions that consume its output. The module itself does not write to the console or log files.

## Design Considerations

- **Single responsibility:** Formatting operations remain independent of output handling.
- **Consistent output:** Log messages follow a predictable structure.
- **Standard library only:** No external dependencies are required.
- **Reusable functions:** Each function can be used independently by other logging modules.

## Limitations

- Timestamps use the local system clock and do not include timezone information.
- Filenames have one-second precision, so two filename-generation calls within the same second can return the same name.
- `format_message()` does not validate severity levels or sanitize message content.

## Related Modules

- [`config.py`](config.md) — Defines supported severity levels and terminal colors.
- [`handlers.py`](handlers.md) — Sends formatted messages to the console and log file.
- [`logger.py`](logger.md) — Exposes the logging interface for application components.
