import sys
import logging

# Настройка логирования
logging.basicConfig(filename='src/logs/logs.log',  # Имя файла для записи логов
                    filemode='w',  # Перезаписывать файл каждый раз (можно использовать 'a' для добавления)
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат логов
                    level=logging.INFO)  # Уровень логирования
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class OutputsInGameLogics:
    """
    Класс, который управляет выводом сообщений и логикой ввода в процессе игры.

    Атрибуты:
        language (int): Язык игры (1 - English, 2 - Русский).
        word (str): Загаданное слово.
        input_y (int): Позиция для отображения текста на экране.
        actual (str): Переменная для хранения статуса актуальности игры.
    """

    def __init__(self, language: int, word: str, input_y: int):
        """
        Инициализирует объект для управления выводом и вводом.

        Параметры:
            language (int): Язык игры.
            word (str): Загаданное слово.
            input_y (int): Позиция для отображения текста на экране.
        """
        self.language = language
        self.word = word
        self.input_y = input_y
        self.actual = ""

    def input_letter(self) -> str:
        """
        Ввод буквы пользователем.

        Возвращает:
            str: Введенная буква в нижнем регистре.
        """
        result = input(
            "\nВведите букву: " if self.language == 2 else "\nInput a letter: "
        ).lower()
        return result

    def warning_about_one_letter(self) -> None:
        """
        Вывод предупреждения, если пользователь вводит больше одной буквы.
        """
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        sys.stdout.write(
            "Пожалуйста, введите одну букву."
            if self.language == 2
            else "Please, input one letter"
        )

    def warning_about_same_letter(self) -> None:
        """
        Вывод предупреждения, если пользователь пытается ввести уже угаданную букву.
        """
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        sys.stdout.write(
            "Вы уже угадали эту букву.\nПопробуйте другую."
            if self.language == 2
            else "You have already guessed this letter.\nTry another one."
        )

    def warning_about_same_used_letter(self) -> None:
        """
        Вывод предупреждения, если пользователь пытается ввести букву, которую уже пробовал угадать.
        """
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        sys.stdout.write(
            "Вы уже пытались угадать эту букву.\nПопробуйте другую."
            if self.language == 2
            else "You have already tried to guess this letter.\nTry another one."
        )

    def win(self) -> None:
        """
        Вывод сообщения о победе, если игрок угадал слово.
        """
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        if self.language == 2:
            sys.stdout.write(f"Поздравляем!\nВы угадали слово: {self.word}")
        else:
            sys.stdout.write(f"Congratulations!\nYou guessed the word: {self.word}")

    def lose(self) -> None:
        """
        Вывод сообщения о поражении, если игрок не смог угадать слово.
        """
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        if self.language == 2:
            sys.stdout.write(f"Вы проиграли.\nЗагаданное слово было: {self.word}")
        else:
            sys.stdout.write(f"You have lost.\nThe hidden word was: {self.word}")

    def confirm_actual(self) -> bool:
        """
        Спрашивает у пользователя, хочет ли он начать новую игру.

        Возвращает:
            bool: True, если пользователь хочет продолжить, False — если нет.
        """
        sys.stdout.write(f"\033[{self.input_y + 4};0H")
        vvod = input(
            "Хотите ли вы начать новую игру? Введите Да/Нет "
            if self.language == 2
            else "Do you want to start a new game? Input Yes/No "
        )
        if vvod.lower() == "да" or vvod.lower() == "yes":
            self.actual = True
        else:
            self.actual = False
        return self.actual


class OutputsInDynamicDisplay:
    """
    Класс для вывода информации о ходе игры на динамическом экране.

    Атрибуты:
        language (int): Язык игры.
        category (str): Категория выбранных слов.
        level (str): Уровень сложности игры.
        attempts (int): Количество оставшихся попыток.
        input_y (int): Позиция для отображения текста на экране.
        has_hint (bool): Указатель на то, доступна ли подсказка.
        hint (str): Подсказка для слова.
    """

    def __init__(self, language: int, category: str, level: str, attempts: int, input_y: int, has_hint: bool, hint: str):
        """
        Инициализирует объект для динамического вывода информации.

        Параметры:
            language (int): Язык игры.
            category (str): Категория слов.
            level (str): Уровень сложности.
            attempts (int): Количество оставшихся попыток.
            input_y (int): Позиция для вывода текста на экране.
            has_hint (bool): Доступна ли подсказка.
            hint (str): Подсказка для текущего слова.
        """
        self.language = language
        self.category = category
        self.level = level
        self.attempts = attempts
        self.input_y = input_y
        self.has_hint = has_hint
        self.hint = hint

    def output_game_info(self) -> None:
        """
        Выводит информацию о текущем состоянии игры, включая категорию, уровень сложности и количество попыток.
        """
        sys.stdout.write("\033[1;0H")
        sys.stdout.write(
            "Игра началась, дерзайте!"
            if self.language == 2
            else "The game has started, go for it!"
        )
        sys.stdout.write("\033[3;0H")
        sys.stdout.write(
            f"Ваша категория слов: {self.category}"
            if self.language == 2
            else f"Your word category: {self.category}"
        )
        sys.stdout.write("\033[4;0H")
        sys.stdout.write(
            f"Выбранный уровень сложности: {self.level}"
            if self.language == 2
            else f"Selected difficulty level: {self.level}"
        )
        sys.stdout.write("\033[5;0H")
        sys.stdout.write(
            f"Осталось попыток: {self.attempts}"
            if self.language == 2
            else f"Attempts left: {self.attempts}"
        )
        sys.stdout.write("\033[6;0H")
        sys.stdout.write("Язык: Русский" if self.language == 2 else "Language: English")

        if self.has_hint:
            RED = "\033[33m"
            RESET = "\033[0m"

            sys.stdout.write("\033[8;0H")
            sys.stdout.write(
                RED + (
                    f"Подсказка: {self.hint}"
                    if self.language == 2
                    else f"Hint: {self.hint}"
                ) + RESET
            )

        sys.stdout.write(f"\033[{self.input_y};0H")
        sys.stdout.write(" " * 50)
        sys.stdout.write(f"\033[{self.input_y};0H")
        sys.stdout.write("Слово: " if self.language == 2 else "Word: ")


class InfoForInput:
    """
    Класс для обработки пользовательского ввода и информации о настройках игры.

    Атрибуты:
        language (int): Язык игры.
    """

    def __init__(self, language: int):
        """
        Инициализирует объект с информацией о выбранном языке игры.

        Параметры:
            language (int): Язык игры.
        """
        self.language = language

    def language_info(self) -> int:
        """
        Выводит запрос на выбор языка и возвращает выбор пользователя.

        Возвращает:
            int: Выбранный язык (1 - English, 2 - Русский).
        """
        result = int(
            input(
                "Choose your language:\n"
                " 1 - English\n"
                " 2 - Russian\n"
                " Your choice - № "
            )
        )
        self.language = result
        return result

    def warning_unavailable_language_number(self) -> None:
        """
        Выводит предупреждение о необходимости ввода допустимого номера языка.
        """
        print("Please enter an available language number\n")

    def category_index_info(self) -> int:
        """
        Запрашивает выбор категории слов и возвращает индекс выбранной категории.

        Возвращает:
            int: Индекс выбранной категории.
        """
        result = int(
            input(
                "Доступные категории слов: \n"
                " 1 - Животные\n"
                " 2 - Игрушки\n"
                " 3 - Овощи\n"
                " 4 - Фрукты\n"
                " 5 - Рандомная\n"
                "Ваш выбор - № "
                if self.language == 2
                else "Available word categories: \n"
                " 1 - Animals\n"
                " 2 - Toys\n"
                " 3 - Vegetables\n"
                " 4 - Fruit\n"
                " 5 - Random\n"
                "Your choice - №"
            )
        )
        return result

    def warning_unavailable_category_number(self) -> None:
        """
        Выводит предупреждение о необходимости ввода допустимого номера категории.
        """
        print(
            "Пожалуйста, введите доступный номер категории"
            if self.language == 2
            else "Please enter an available category number"
        )

    def level_info(self) -> int:
        """
        Запрашивает выбор уровня сложности и возвращает индекс выбранного уровня.

        Возвращает:
            int: Индекс выбранного уровня сложности.
        """
        result = int(
            input(
                "Доступные уровни сложности: \n"
                " 1 - лёгкий\n"
                " 2- средний\n"
                " 3 - сложный\n"
                " 4 - Рандомный\n"
                "Ваш выбор - "
                if self.language == 2
                else "Available difficulty levels: \n"
                " 1 - easy\n"
                " 2- medium\n"
                " 3 - hard\n"
                " 4 - Random\n"
                "Your choice - "
            )
        )
        return result

    def warning_unavailable_level_number(self) -> None:
        """
        Выводит предупреждение о необходимости ввода допустимого уровня сложности.
        """
        print(
            "Пожалуйста, введите доступный уровень сложности"
            if self.language == 2
            else "Please enter the available difficulty level"
        )

    def attempts_info(self) -> int:
        """
        Запрашивает максимальное количество ошибок и возвращает введенное значение.

        Возвращает:
            int: Максимальное количество ошибок.
        """
        result = int(
            input(
                "Введите максимальное число ошибок (от 2 до 17) "
                if self.language == 2
                else "Enter the maximum number of errors (from 2 to 17) "
            )
        )
        return result

    def warning_unavailable_attempts_number(self) -> None:
        """
        Выводит предупреждение о необходимости ввода допустимого количества ошибок.
        """
        print(
            "Пожалуйста введите допустимое число попыток"
            if self.language == 2
            else "Please enter the allowed number of attempts"
        )

    def hints_info(self) -> int:
        """
        Запрашивает количество ошибок для отображения подсказки и возвращает введенное значение.

        Возвращает:
            int: Количество ошибок для отображения подсказки.
        """
        result = int(
            input(
                "Введите число ошибок, совершённых подряд, после которого нужно вывести подсказку:\n"
                "Если подсказки нужны, то введите число от единицы до выбранного Вами числа попыток)\n"
                "Если подсказки не нужны, введите -1\n"
                if self.language == 2
                else "Enter the number of errors made in a row after which you want to display a hint:\n"
                "If you need hints, then enter a number from one to the number of attempts you have chosen)\n"
                "If prompts are not needed, enter -1\n"
            )
        )
        return result

    def warning_unavailable_hints_number(self) -> None:
        """
        Выводит предупреждение о необходимости ввода допустимого числа ошибок для отображения подсказки.
        """
        print(
            "Пожалуйста введите допустимое число ошибок"
            if self.language == 2
            else "Please enter the allowed number of errors"
        )

    @classmethod
    def error_log(cls) -> None:
        """
        Логирует ошибку неверного ввода через логгер.
        """
        logger.exception('Invalid input')
