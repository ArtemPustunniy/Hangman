import pytest
from unittest.mock import patch
from src.work_with_data.reader import Reader
from src.work_with_data.output import InfoForInput
from src.work_with_data.word import Language


@pytest.fixture
def mock_info_input() -> InfoForInput:
    """
    Фикстура для создания объекта InfoForInput с тестовыми данными.

    Возвращает:
        InfoForInput: Объект для тестирования ввода данных.
    """
    return InfoForInput(0)


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_language_number')
@patch('src.work_with_data.output.InfoForInput.language_info', return_value=1)
def test_input_language(mock_input, mock_warning, mock_clear, mock_info_input: InfoForInput):
    """
    Тестирует метод input_language класса Reader, проверяя правильность ввода языка.

    Параметры:
        mock_input: Мок метода language_info для эмуляции ввода языка.
        mock_warning: Мок метода предупреждения о недопустимом вводе.
        mock_clear: Мок метода очистки консоли.
        mock_info_input (InfoForInput): Мок объекта для тестирования ввода.
    """
    result = Reader.input_language(mock_info_input)
    assert result == 1  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_category_number')
@patch('src.work_with_data.output.InfoForInput.category_index_info', return_value=1)
def test_input_category(mock_input, mock_warning, mock_clear, mock_info_input: InfoForInput):
    """
    Тестирует метод input_category класса Reader, проверяя правильность ввода категории.

    Параметры:
        mock_input: Мок метода category_index_info для эмуляции ввода категории.
        mock_warning: Мок метода предупреждения о недопустимом вводе.
        mock_clear: Мок метода очистки консоли.
        mock_info_input (InfoForInput): Мок объекта для тестирования ввода.
    """
    result = Reader.input_category(mock_info_input)
    assert result == 1  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_level_number')
@patch('src.work_with_data.output.InfoForInput.level_info', return_value=2)
def test_input_level(mock_input, mock_warning, mock_clear, mock_info_input: InfoForInput):
    """
    Тестирует метод input_level класса Reader, проверяя правильность ввода уровня.

    Параметры:
        mock_input: Мок метода level_info для эмуляции ввода уровня.
        mock_warning: Мок метода предупреждения о недопустимом вводе.
        mock_clear: Мок метода очистки консоли.
        mock_info_input (InfoForInput): Мок объекта для тестирования ввода.
    """
    result = Reader.input_level(mock_info_input)
    assert result == 2  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_attempts_number')
@patch('src.work_with_data.output.InfoForInput.attempts_info', return_value=5)
def test_input_attempts(mock_input, mock_warning, mock_clear, mock_info_input: InfoForInput):
    """
    Тестирует метод input_attempts класса Reader, проверяя правильность ввода количества попыток.

    Параметры:
        mock_input: Мок метода attempts_info для эмуляции ввода количества попыток.
        mock_warning: Мок метода предупреждения о недопустимом вводе.
        mock_clear: Мок метода очистки консоли.
        mock_info_input (InfoForInput): Мок объекта для тестирования ввода.
    """
    result = Reader.input_attempts(mock_info_input)
    assert result == 5  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_hints_number')
@patch('src.work_with_data.output.InfoForInput.hints_info', return_value=2)
def test_input_hints(mock_input, mock_warning, mock_clear, mock_info_input: InfoForInput):
    """
    Тестирует метод input_hints класса Reader, проверяя правильность ввода количества подсказок.

    Параметры:
        mock_input: Мок метода hints_info для эмуляции ввода количества подсказок.
        mock_warning: Мок метода предупреждения о недопустимом вводе.
        mock_clear: Мок метода очистки консоли.
        mock_info_input (InfoForInput): Мок объекта для тестирования ввода.
    """
    result = Reader.input_hints(3, mock_info_input)  # attempts = 3
    assert result == 2  # Проверяем, что значение введено корректно


@patch('src.work_with_data.utils.Utils.clear_console')
@patch('src.work_with_data.output.InfoForInput.warning_unavailable_language_number')
@patch('src.work_with_data.output.InfoForInput.language_info', side_effect=[-1, 1])
def test_input_value(mock_input, mock_warning, mock_clear):
    """
    Тестирует универсальный метод input_value класса Reader, проверяя ввод с ошибкой и последующим исправлением.

    Параметры:
        mock_input: Мок метода language_info для эмуляции ввода с ошибкой, а затем корректного значения.
        mock_warning: Мок метода предупреждения о недопустимом вводе.
        mock_clear: Мок метода очистки консоли.
    """
    result = Reader.input_value('language', Language.ENGLISH.value, Language.RUSSIAN.value,
                                InfoForInput.language_info, InfoForInput.warning_unavailable_language_number)
    assert result == 1  # Проверяем, что значение введено корректно после ошибки
