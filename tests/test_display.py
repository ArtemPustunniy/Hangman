import pytest
from unittest.mock import patch
from io import StringIO
import re
from Visualiser.Display import Display_Console


def clean_ansi_escape_sequences(text):
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi_escape.sub("", text)


@pytest.fixture
def display_console():
    word = "duck"
    guessed_letters = ["p", "y", "h"]
    input_y = 10
    category = "animals"
    level = 1
    attempts = 3
    language = 1
    return Display_Console(
        word, guessed_letters, input_y, category, level, attempts, language
    )


class TestDisplayConsole:
    def test_clear_for_conclusion(self, display_console):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            display_console.clear_for_conclusion()
            output = clean_ansi_escape_sequences(mock_stdout.getvalue())
            # Проверяем, что вывод очищен (т.е. все заменено на пробелы)
            assert " " * 300 in output
