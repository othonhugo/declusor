import unittest

from declusor.config import ArgumentParsingError
from declusor.util.parse import parse_command_arguments


class TestParseUtil(unittest.TestCase):
    def test_parse_simple(self) -> None:
        """Test parsing a simple single argument."""

        line = "arg1"
        definitions = {"arg": str}

        parsed, unknown = parse_command_arguments(line, definitions)

        self.assertEqual(parsed, {"arg": "arg1"})
        self.assertEqual(unknown, [])

    def test_parse_multiple(self) -> None:
        """Test parsing multiple arguments with type conversion."""

        line = "val1 123"
        definitions: dict[str, type] = {"str_arg": str, "int_arg": int}

        parsed, unknown = parse_command_arguments(line, definitions)

        self.assertEqual(parsed, {"str_arg": "val1", "int_arg": 123})

    def test_parse_allow_unknown(self) -> None:
        """Test parsing with unknown arguments allowed."""

        line = "val1 extra1 extra2"
        definitions = {"arg": str}

        parsed, unknown = parse_command_arguments(line, definitions, allow_unknown=True)

        self.assertEqual(parsed, {"arg": "val1"})
        self.assertEqual(unknown, ["extra1", "extra2"])

    def test_parse_error_missing_arg(self) -> None:
        """Test that missing required arguments raise an error."""

        line = ""
        definitions = {"arg": str}

        with self.assertRaises(ArgumentParsingError):
            parse_command_arguments(line, definitions)

    def test_parse_error_unknown_arg_not_allowed(self) -> None:
        """Test that unknown arguments raise an error when not allowed."""

        line = "val1 extra"
        definitions = {"arg": str}

        with self.assertRaises(ArgumentParsingError):
            parse_command_arguments(line, definitions, allow_unknown=False)

    def test_parse_empty_no_defs(self) -> None:
        """Test parsing empty line with no definitions."""

        parsed, unknown = parse_command_arguments("", {})

        self.assertEqual(parsed, {})
        self.assertEqual(unknown, [])
