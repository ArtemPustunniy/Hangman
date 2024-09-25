import pytest
from unittest.mock import patch
from io import StringIO
import re
from src.visualiser.display import DisplayConsole


def clean_ansi_escape_sequences(text: str) -> str:
    """
    Удаляет ANSI escape-последовательности из текста, чтобы проверить вывод консоли без спецсимволов.

    Параметры:
        text (str): Текст с возможными ANSI escape-последовательностями.

    Возвращает:
        str: Текст без ANSI escape-последовательностей.
    """
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi_escape.sub("", text)


@pytest.fixture
def display_console() -> DisplayConsole:
    """
    Фикстура для создания объекта DisplayConsole для тестов.

    Возвращает:
        DisplayConsole: Объект для отображения состояния игры.
    """
    word = "duck"
    guessed_letters = ["p", "y", "h"]
    input_y = 10
    category = "animals"
    level = 1
    attempts = 3
    language = 1
    return DisplayConsole(
        word, guessed_letters, input_y, category, level, attempts, language
    )


class TestDisplayConsole:
    """
    Класс для тестирования методов класса DisplayConsole.
    """

    def test_clear_for_conclusion(self, display_console: DisplayConsole):
        """
        Тестирует метод clear_for_conclusion класса DisplayConsole, проверяя, что консоль очищается.

        Параметры:
            display_console (DisplayConsole): Объект для тестирования метода clear_for_conclusion.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            display_console.clear_for_conclusion()
            output = clean_ansi_escape_sequences(mock_stdout.getvalue())
            # Проверяем, что вывод очищен (т.е. все заменено на пробелы)
            assert " " * 300 in output
