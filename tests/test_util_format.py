import unittest

from declusor.util.format import convert_bytes_to_hex, escape_double_quotes, escape_single_quotes, format_bash_arguments, format_bash_function_call


class TestFormatUtil(unittest.TestCase):
    def test_convert_bytes_to_hex(self) -> None:
        """Test converting bytes to hex string representation."""

        self.assertEqual(convert_bytes_to_hex(b"abc"), "\\x61\\x62\\x63")
        self.assertEqual(convert_bytes_to_hex(b""), "")

    def test_format_bash_arguments(self) -> None:
        """Test formatting bash arguments with uppercase keys."""

        args: dict[str, str | int] = {"host": "127.0.0.1", "port": 8080}
        expected: dict[str, str] = {"HOST": "127.0.0.1", "PORT": "8080"}

        self.assertEqual(format_bash_arguments(**args), expected)

    def test_escape_single_quotes(self) -> None:
        """Test escaping single quotes and backslashes."""

        self.assertEqual(escape_single_quotes("foo'bar"), "foo\\'bar")
        self.assertEqual(escape_single_quotes("foo\\bar"), "foo\\\\bar")

    def test_escape_double_quotes(self) -> None:
        """Test escaping double quotes and backslashes."""

        self.assertEqual(escape_double_quotes('foo"bar'), 'foo\\"bar')
        self.assertEqual(escape_double_quotes("foo\\bar"), "foo\\\\bar")

    def test_format_bash_function_call(self) -> None:
        """Test formatting bash function calls with proper quote escaping."""

        # Single quotes (default)
        self.assertEqual(format_bash_function_call("my_func", "arg1", "arg'2"), "my_func 'arg1' 'arg\\'2'")

        # Double quotes
        self.assertEqual(format_bash_function_call("my_func", "arg1", 'arg"2', use_double_quotes=True), 'my_func "arg1" "arg\\"2"')
