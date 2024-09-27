import sys
from src.work_with_data.output import OutputsInDynamicDisplay


class DisplayConsole:
    """
    Класс для отображения состояния игры "Виселица" в консоли.

    Атрибуты:
        word (str): Загаданное слово.
        guessed_letters (set): Набор угаданных букв.
        input_y (int): Позиция строки ввода на экране.
        attempts (int): Количество оставшихся попыток.
        category (str): Категория слова.
        level (str): Уровень сложности.
        language (int): Язык игры.
        has_hint (bool): Указывает, была ли предоставлена подсказка.
        hint (str): Подсказка к слову (если есть).
    """

    def __init__(
            self, word: str, guessed_letters: set, input_y: int,
            category: str, level: str, attempts: int, language: int):
        """
        Инициализирует объект для отображения состояния игры.

        Параметры:
            word (str): Загаданное слово.
            guessed_letters (set): Набор угаданных букв.
            input_y (int): Позиция строки ввода на экране.
            category (str): Категория слова.
            level (str): Уровень сложности.
            attempts (int): Количество оставшихся попыток.
            language (int): Язык игры.
        """
        self.word = word
        self.guessed_letters = guessed_letters
        self.input_y = input_y
        self.attempts = attempts
        self.category = category
        self.level = level
        self.language = language
        self.has_hint = False
        self.hint = ''

    def display_word_state(self) -> None:
        """
        Отображает текущее состояние игры, включая угаданные буквы, количество оставшихся попыток и другие данные.

        Метод выводит загаданное слово с уже угаданными буквами и подчеркивает оставшиеся буквы. Также
        отображается информация о категории, уровне сложности и количестве оставшихся попыток.
        """
        OutputsInDynamicDisplay(
            self.language, self.category, self.level, self.attempts, self.input_y,
            self.has_hint, self.hint).output_game_info()

        # Отображение загаданного слова, включая угаданные буквы
        for letter in self.word:
            if letter in self.guessed_letters:
                sys.stdout.write(f"{letter} ")
            else:
                sys.stdout.write("_ ")

        # Различное отображение в зависимости от языка
        if self.language == 1:
            for i in range(17, 300, 1):
                sys.stdout.write(f"\033[{self.input_y + 1};{i}H")
                sys.stdout.write(" ")
        else:
            for i in range(16, 300, 1):
                sys.stdout.write(f"\033[{self.input_y + 1};{i}H")
                sys.stdout.write(" ")

        # Отображение основания виселицы
        for i in range(48, 56, 1):
            sys.stdout.write(f"\033[12;{i}H")
            sys.stdout.write("-")

        for i in range(48, 56, 1):
            sys.stdout.write(f"\033[13;{i}H")
            sys.stdout.write("-")

        # Возвращение курсора к начальной позиции ввода
        sys.stdout.write(f"\033[{self.input_y};0H")
        sys.stdout.flush()

    def clear_for_conclusion(self) -> None:
        """
        Очищает область консоли для отображения финальных сообщений, таких как победа или поражение.
        """
        for i in range(0, 300, 1):
            sys.stdout.write(f"\033[{self.input_y + 2};{i}H")
            sys.stdout.write(" ")
        for i in range(0, 300, 1):
            sys.stdout.write(f"\033[{self.input_y + 3};{i}H")
            sys.stdout.write(" ")

    def change_has_hint(self) -> None:
        """
        Активирует флаг наличия подсказки, указывая на то, что подсказка предоставлена.
        """
        self.has_hint = True
