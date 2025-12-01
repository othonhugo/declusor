import shlex
import unittest

from hypothesis import given
from hypothesis import strategies as st

from declusor.config import ArgumentParsingError
from declusor.util.parse import parse_command_arguments


class TestParserProperties(unittest.TestCase):
    strategies_text = st.text()

    @given(strategies_text)
    def test_parse_never_crashes_on_random_input(self, input_str: str) -> None:
        """
        Property: parse_command_arguments should never raise an unexpected exception (crash)
        for any string input. It should either return a result or raise ArgumentParsingError.
        """

        definitions = {"arg": str}

        try:
            parse_command_arguments(input_str, definitions)
        except ArgumentParsingError:
            # Expected failure for invalid inputs
            pass
        except Exception as e:
            self.fail(f"Parser crashed with {type(e).__name__}: {e}")

    strategies_keys = st.text(min_size=1, max_size=10, alphabet=st.characters(whitelist_categories=("L", "N")))
    strategies_values = st.text(min_size=1, max_size=20).filter(lambda x: not x.startswith("-"))
    strategies_dictionaries = st.dictionaries(keys=strategies_keys, values=strategies_values)

    @given(strategies_dictionaries)
    def test_parse_valid_input(self, args_dict: dict[str, str]) -> None:
        """
        Property: If we construct a valid command string from a dictionary,
        parsing it back should yield the same dictionary (mostly).
        """

        definitions = {k: str for k in args_dict.keys()}

        # Construct the command string using shlex.quote to handle spaces/special chars safely
        cmd_parts: list[str] = []

        for v in args_dict.values():
            cmd_parts.append(shlex.quote(v))

        cmd_line = " ".join(cmd_parts)

        parsed, unknown = parse_command_arguments(cmd_line, definitions)

        self.assertEqual(parsed, args_dict)
        self.assertEqual(unknown, [])
