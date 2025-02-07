import pytest
from unittest.mock import patch, MagicMock
from src.work_with_data.output import OutputsInGameLogics, OutputsInDynamicDisplay


@pytest.fixture
def outputs_in_game_logics() -> OutputsInGameLogics:
    """
    Фикстура для создания объекта OutputsInGameLogics с тестовыми данными.

    Возвращает:
        OutputsInGameLogics: Объект для тестирования логики вывода в игре.
    """
    return OutputsInGameLogics(language=1, word="python", input_y=10)


@pytest.fixture
def outputs_in_dynamic_display() -> OutputsInDynamicDisplay:
    """
    Фикстура для создания объекта OutputsInDynamicDisplay с тестовыми данными.

    Возвращает:
        OutputsInDynamicDisplay: Объект для тестирования динамического отображения информации в игре.
    """
    return OutputsInDynamicDisplay(
        language=1, category="Animals", level=2, attempts=5, input_y=10, has_hint=False, hint='hint'
    )


class TestOutputsInGameLogics:
    """
    Класс для тестирования методов класса OutputsInGameLogics.
    """

    def test_input_letter(self, outputs_in_game_logics: OutputsInGameLogics):
        """
        Тестирует метод input_letter, проверяя правильность ввода буквы пользователем.

        Параметры:
            outputs_in_game_logics (OutputsInGameLogics): Объект для тестирования метода input_letter.
        """
        with patch("builtins.input", return_value="a"):
            result = outputs_in_game_logics.input_letter()
            assert result == "a"

    def test_warning_about_one_letter(self, outputs_in_game_logics: OutputsInGameLogics):
        """
        Тестирует вывод предупреждения о необходимости ввода одной буквы.

        Параметры:
            outputs_in_game_logics (OutputsInGameLogics): Объект для тестирования метода warning_about_one_letter.
        """
        with patch("sys.stdout", new_callable=MagicMock()) as mock_stdout:
            outputs_in_game_logics.warning_about_one_letter()
            mock_stdout.write.assert_called_with("Please, input one letter")

    def test_warning_about_same_letter(self, outputs_in_game_logics: OutputsInGameLogics):
        """
        Тестирует вывод предупреждения о повторном вводе угаданной буквы.

        Параметры:
            outputs_in_game_logics (OutputsInGameLogics): Объект для тестирования метода warning_about_same_letter.
        """
        with patch("sys.stdout", new_callable=MagicMock()) as mock_stdout:
            outputs_in_game_logics.warning_about_same_letter()
            mock_stdout.write.assert_called_with(
                "You have already guessed this letter.\nTry another one."
            )

    def test_warning_about_same_used_letter(self, outputs_in_game_logics: OutputsInGameLogics):
        """
        Тестирует вывод предупреждения о повторном вводе использованной буквы.

        Параметры:
            outputs_in_game_logics (OutputsInGameLogics): Объект для тестирования метода warning_about_same_used_letter.
        """
        with patch("sys.stdout", new_callable=MagicMock()) as mock_stdout:
            outputs_in_game_logics.warning_about_same_used_letter()
            mock_stdout.write.assert_called_with(
                "You have already tried to guess this letter.\nTry another one."
            )

    def test_confirm_actual_yes(self, outputs_in_game_logics: OutputsInGameLogics):
        """
        Тестирует метод confirm_actual при ответе пользователя "yes".

        Параметры:
            outputs_in_game_logics (OutputsInGameLogics): Объект для тестирования метода confirm_actual.
        """
        with patch("builtins.input", return_value="yes"):
            result = outputs_in_game_logics.confirm_actual()
            assert result is True

    def test_confirm_actual_no(self, outputs_in_game_logics: OutputsInGameLogics):
        """
        Тестирует метод confirm_actual при ответе пользователя "no".

        Параметры:
            outputs_in_game_logics (OutputsInGameLogics): Объект для тестирования метода confirm_actual.
        """
        with patch("builtins.input", return_value="no"):
            result = outputs_in_game_logics.confirm_actual()
            assert result is False


class TestOutputsInDynamicDisplay:
    """
    Класс для тестирования методов класса OutputsInDynamicDisplay.
    """

    def test_output_game_info(self, outputs_in_dynamic_display: OutputsInDynamicDisplay):
        """
        Тестирует вывод информации об игре методом output_game_info.

        Параметры:
            outputs_in_dynamic_display (OutputsInDynamicDisplay): Объект для тестирования метода output_game_info.
        """
        with patch("sys.stdout", new_callable=MagicMock()) as mock_stdout:
            outputs_in_dynamic_display.output_game_info()
            mock_stdout.write.assert_any_call("The game has started, go for it!")
            mock_stdout.write.assert_any_call("Your word category: Animals")
            mock_stdout.write.assert_any_call("Selected difficulty level: 2")
            mock_stdout.write.assert_any_call("Attempts left: 5")
            mock_stdout.write.assert_any_call("Language: English")
