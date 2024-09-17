import sys

from src.work_with_data.output import OutputsInDynamicDisplay


class DisplayConsole:
    def __init__(
            self, word, guessed_letters, input_y, category, level, attempts, language):
        self.word = word
        self.guessed_letters = guessed_letters
        self.input_y = input_y
        self.attempts = attempts
        self.category = category
        self.level = level
        self.language = language
        self.has_hint = False
        self.hint = ''

        self.display_word_state()

    def display_word_state(self) -> None:
        OutputsInDynamicDisplay(
            self.language, self.category, self.level, self.attempts, self.input_y,
            self.has_hint, self.hint).output_game_info()
        for letter in self.word:
            if letter in self.guessed_letters:
                sys.stdout.write(f"{letter} ")
            else:
                sys.stdout.write("_ ")
        if self.language == 1:
            for i in range(17, 300, 1):
                sys.stdout.write(f"\033[{self.input_y + 1};{i}H")
                sys.stdout.write(" ")
        else:
            for i in range(16, 300, 1):
                sys.stdout.write(f"\033[{self.input_y + 1};{i}H")
                sys.stdout.write(" ")

        # Вывод основания виселицы
        for i in range(48, 56, 1):
            sys.stdout.write(f"\033[12;{i}H")
            sys.stdout.write("-" + "")

        for i in range(48, 56, 1):
            sys.stdout.write(f"\033[13;{i}H")
            sys.stdout.write("-" + "")

        sys.stdout.write(f"\033[{self.input_y};0H")

        sys.stdout.flush()

    def clear_for_conclusion(self) -> None:
        for i in range(0, 300, 1):
            sys.stdout.write(f"\033[{self.input_y + 2};{i}H")
            sys.stdout.write(" ")
        for i in range(0, 300, 1):
            sys.stdout.write(f"\033[{self.input_y + 3};{i}H")
            sys.stdout.write(" ")

    def change_has_hint(self) -> None:
        self.has_hint = True
