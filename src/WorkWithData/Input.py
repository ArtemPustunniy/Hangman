from .Output import InfoForInput
from .Utils import Utils


class Input:
    def __init__(self):
        self.language = -1
        self.categoty_index = -1
        self.level_index = -1
        self.attempts = -1
        self.hints = 0
        self.info_input = InfoForInput(0)

        self.input_language()
        self.input_category_index()
        self.input_level()
        self.input_attempts()
        self.input_about_hints()

    def input_language(self) -> None:
        language_flag = False
        try:
            self.language = self.info_input.language_info()
            if 1 <= self.language <= 2:
                language_flag = True
                Utils.clear_console()
            else:
                language_flag = False
        except ValueError:
            InfoForInput.error_log()
        while not language_flag:
            Utils.clear_console()
            try:
                self.info_input.warning_unavailable_language_number()
                self.language = self.info_input.language_info()
                if 1 <= self.language <= 2:
                    language_flag = True
                    Utils.clear_console()
                else:
                    language_flag = False
            except ValueError:
                InfoForInput.error_log()
                self.info_input.warning_unavailable_language_number()
        return

    def input_category_index(self) -> None:
        category_flag = False
        try:
            self.category_index = self.info_input.category_index_info()
            if 1 <= self.category_index <= 5:
                category_flag = True
                Utils.clear_console()
            else:
                category_flag = False
        except ValueError:
            InfoForInput.error_log()

        while not category_flag:
            Utils.clear_console()
            try:
                self.info_input.warning_unavailable_category_number()
                self.category_index = self.info_input.category_index_info()
                if 1 <= self.category_index <= 5:
                    category_flag = True
                    Utils.clear_console()
                else:
                    category_flag = False
            except ValueError:
                InfoForInput.error_log()
                self.info_input.warning_unavailable_category_number()
        return

    def input_level(self) -> None:
        level_flag = False
        try:
            self.level_index = self.info_input.level_info()
            if 1 <= self.level_index <= 4:
                level_flag = True
                Utils.clear_console()
            else:
                level_flag = False
        except ValueError:
            InfoForInput.error_log()

        while not level_flag:
            Utils.clear_console()
            try:
                self.info_input.warning_unavailable_level_number()
                self.level_index = self.info_input.level_info()
                if 1 <= self.level_index <= 4:
                    level_flag = True
                    Utils.clear_console()
                else:
                    level_flag = False
            except ValueError:
                InfoForInput.error_log()
                self.info_input.warning_unavailable_level_number()
        return

    def input_attempts(self) -> None:
        attempts_flag = False
        try:
            self.attempts = self.info_input.attempts_info()
            if 2 <= self.attempts <= 17:
                attempts_flag = True
                Utils.clear_console()
            else:
                attempts_flag = False
        except ValueError:
            InfoForInput.error_log()

        while not attempts_flag:
            Utils.clear_console()
            try:
                self.info_input.warning_unavailable_attempts_number()
                self.attempts = self.info_input.attempts_info()
                if 2 <= self.attempts <= 17:
                    attempts_flag = True
                    Utils.clear_console()
                else:
                    attempts_flag = False
            except ValueError:
                self.info_input.error_log()
                self.info_input.warning_unavailable_attempts_number()
        return

    def input_about_hints(self):
        hints_flag = False
        try:
            self.hints = self.info_input.hints_info()
            if (1 <= self.hints < self.attempts) or (self.hints == -1):
                hints_flag = True
                Utils.clear_console()
            else:
                hints_flag = False
        except ValueError:
            InfoForInput.error_log()

        while not hints_flag:
            Utils.clear_console()
            try:
                self.info_input.warning_unavailable_hints_number()
                self.attempts = self.info_input.hints_info()
                if (1 <= self.hints < self.attempts) or (self.hints == -1):
                    hints_flag = True
                    Utils.clear_console()
                else:
                    hints_flag = False
            except ValueError:
                self.info_input.error_log()
                self.info_input.warning_unavailable_hints_number()
        return
