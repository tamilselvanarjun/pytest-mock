from typing import Union

_mock_module = None


def get_mock_module(config):
    """
    Import and return the actual "mock" module. By default this is
    "unittest.mock", but the user can force to always use "mock" using
    the mock_use_standalone_module ini option.
    """
    global _mock_module
    if _mock_module is None:
        use_standalone_module = parse_ini_boolean(
            config.getini("mock_use_standalone_module")
        )
        if use_standalone_module:
            import mock

            _mock_module = mock
        else:
            import unittest.mock

            _mock_module = unittest.mock

    return _mock_module

from typing import Union

def parse_ini_boolean(value: Union[bool, str]) -> bool:
    """
    Parse a boolean value from an INI file string representation.

    Args:
        value (Union[bool, str]): The value to parse, can be either a boolean or a string.

    Returns:
        bool: The parsed boolean value.

    Raises:
        ValueError: If the input value is not a valid boolean string.
    """
    if isinstance(value, bool):
        return value
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    raise ValueError("unknown string for bool: %r" % value)

