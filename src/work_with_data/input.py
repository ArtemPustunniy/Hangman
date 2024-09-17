from .output import InfoForInput
from .utils import Utils
from .word import LevelIndex, LanguageIndex, CategoryIndex
from src.visualiser.hangman import StaticHangman


class Input:
    def __init__(self):
        self.language = -1
        self.category_index = -1
        self.level_index = -1
        self.attempts = -1
        self.hints = 0
        self.info_input = InfoForInput(0)

        self.input_value('language', LanguageIndex.ENGLISH.value, LanguageIndex.RUSSIAN.value, self.info_input.language_info, self.info_input.warning_unavailable_language_number)
        self.input_value('category_index', list(CategoryIndex)[0].value, list(CategoryIndex)[-1].value, self.info_input.category_index_info, self.info_input.warning_unavailable_category_number)
        self.input_value('level_index', list(LevelIndex)[0].value, list(LevelIndex)[-1].value, self.info_input.level_info, self.info_input.warning_unavailable_level_number)
        self.input_value('attempts', 2, StaticHangman.get_hangman_steps(), self.info_input.attempts_info, self.info_input.warning_unavailable_attempts_number)
        self.input_value('hints', 1, self.attempts, self.info_input.hints_info, self.info_input.warning_unavailable_hints_number, special_condition=True)

    def input_value(self, attr_name, min_value, max_value, info_method, warning_method, special_condition=False) -> None:
        """
        Универсальный метод для ввода данных с валидацией.

        :param attr_name: Название атрибута для хранения значения.
        :param min_value: Минимально допустимое значение.
        :param max_value: Максимально допустимое значение.
        :param info_method: Метод для получения данных от пользователя.
        :param warning_method: Метод для вывода предупреждения при ошибке.
        :param special_condition: Дополнительное условие для проверки подсказок (хинтов).
        """
        try:
            setattr(self, attr_name, info_method())
        except ValueError:
            InfoForInput.error_log()

        if special_condition:
            valid_flag = (min_value <= getattr(self, attr_name) < max_value) or (getattr(self, attr_name) == -1)
        else:
            valid_flag = min_value <= getattr(self, attr_name) <= max_value

        while not valid_flag:
            Utils.clear_console()
            warning_method()
            try:
                setattr(self, attr_name, info_method())
            except ValueError:
                InfoForInput.error_log()
                warning_method()

            if special_condition:
                valid_flag = (min_value <= getattr(self, attr_name) < max_value) or (getattr(self, attr_name) == -1)
            else:
                valid_flag = min_value <= getattr(self, attr_name) <= max_value

        Utils.clear_console()
