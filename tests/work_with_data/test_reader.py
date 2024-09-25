import pytest
from unittest.mock import patch
from src.work_with_data.reader import Reader
from src.work_with_data.output import InfoForInput
from src.work_with_data.word import Language, Category, Level


# Мокируем методы, которые получают данные от пользователя и предупреждают
@pytest.fixture
def mock_info_input():
    return InfoForInput(0)


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_language_number')
@patch('src.work_with_data.output.InfoForInput.language_info', return_value=1)  # Мокаем ввод языка
def test_input_language(mock_input, mock_warning, mock_clear, mock_info_input):
    result = Reader.input_language(mock_info_input)
    assert result == 1  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_category_number')
@patch('src.work_with_data.output.InfoForInput.category_index_info', return_value=1)  # Мокаем ввод категории
def test_input_category(mock_input, mock_warning, mock_clear, mock_info_input):
    result = Reader.input_category(mock_info_input)
    assert result == 1  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_level_number')
@patch('src.work_with_data.output.InfoForInput.level_info', return_value=2)  # Мокаем ввод уровня
def test_input_level(mock_input, mock_warning, mock_clear, mock_info_input):
    result = Reader.input_level(mock_info_input)
    assert result == 2  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_attempts_number')
@patch('src.work_with_data.output.InfoForInput.attempts_info', return_value=5)  # Мокаем ввод количества попыток
def test_input_attempts(mock_input, mock_warning, mock_clear, mock_info_input):
    result = Reader.input_attempts(mock_info_input)
    assert result == 5  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_hints_number')
@patch('src.work_with_data.output.InfoForInput.hints_info', return_value=2)  # Мокаем ввод хинтов
def test_input_hints(mock_input, mock_warning, mock_clear, mock_info_input):
    result = Reader.input_hints(3, mock_info_input)  # attempts = 3, max_value = 3
    assert result == 2  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_language_number')
@patch('src.work_with_data.output.InfoForInput.language_info', side_effect=[-1, 1])  # Мокаем ошибку, а затем корректный ввод
def test_input_value(mock_input, mock_warning, mock_clear):
    result = Reader.input_value('language', Language.ENGLISH.value, Language.RUSSIAN.value,
                                InfoForInput.language_info, InfoForInput.warning_unavailable_language_number)
    assert result == 1  # Проверяем, что значение введено корректно после ошибки
