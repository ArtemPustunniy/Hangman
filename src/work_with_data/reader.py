from .output import InfoForInput
from .word import Level, Language, Category
from src.visualiser.hangman import StaticHangman
from .utils import Utils
from .input import Input


class Reader:
    @staticmethod
    def fill_input():
        info_input = InfoForInput(0)
        input_data = Input()  # Создаем объект класса Input с начальными значениями

        # Собираем данные от пользователя
        input_data.language = Reader.input_language(info_input)
        input_data.category_index = Reader.input_category(info_input)
        input_data.level_index = Reader.input_level(info_input)
        input_data.attempts = Reader.input_attempts(info_input)
        input_data.hints = Reader.input_hints(input_data.attempts, info_input)

        return input_data

    @staticmethod
    def input_language(info_input):
        return Reader.input_value('language', Language.ENGLISH.value, Language.RUSSIAN.value,
                                  info_input.language_info, info_input.warning_unavailable_language_number)

    @staticmethod
    def input_category(info_input):
        return Reader.input_value('category_index', list(Category)[0].value, list(Category)[-1].value,
                                  info_input.category_index_info, info_input.warning_unavailable_category_number)

    @staticmethod
    def input_level(info_input):
        return Reader.input_value('level_index', list(Level)[0].value, list(Level)[-1].value,
                                  info_input.level_info, info_input.warning_unavailable_level_number)

    @staticmethod
    def input_attempts(info_input):
        return Reader.input_value('attempts', 2, StaticHangman.get_hangman_steps(),
                                  info_input.attempts_info, info_input.warning_unavailable_attempts_number)

    @staticmethod
    def input_hints(attempts, info_input):
        """
        Метод для ввода количества подсказок (хинтов). Здесь учтено специальное условие.
        """
        min_value = 1
        max_value = attempts
        try:
            hints = info_input.hints_info()
        except ValueError:
            InfoForInput.error_log()

        valid_flag = (min_value <= hints < max_value) or (hints == -1)

        while not valid_flag:
            Utils.clear_console()
            info_input.warning_unavailable_hints_number()
            try:
                hints = info_input.hints_info()
            except ValueError:
                InfoForInput.error_log()
                info_input.warning_unavailable_hints_number()

            valid_flag = (min_value <= hints < max_value) or (hints == -1)

        Utils.clear_console()
        return hints

    @staticmethod
    def input_value(attr_name, min_value, max_value, info_method, warning_method) -> int:
        """
        Универсальный метод для ввода данных с валидацией, используется для большинства полей.
        """
        try:
            value = info_method()
        except ValueError:
            InfoForInput.error_log()

        valid_flag = min_value <= value <= max_value

        while not valid_flag:
            Utils.clear_console()
            warning_method()
            try:
                value = info_method()
            except ValueError:
                InfoForInput.error_log()
                warning_method()

            valid_flag = min_value <= value <= max_value

        Utils.clear_console()
        return value
