import sys

from src.WorkWithData.Output import OutputsInDynamicDisplay


class DisplayConsole:
    def __init__(
        self, word, guessed_letters, input_y, category, level, attempts, language
    ):
        self.word = word
        self.guessed_letters = guessed_letters
        self.input_y = input_y
        self.attempts = attempts
        self.category = category
        self.level = level
        self.language = language

        self.display_word_state()

    def display_word_state(self):
        OutputsInDynamicDisplay(
            self.language, self.category, self.level, self.attempts, self.input_y
        ).output_game_info()
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

        sys.stdout.write("\033[12;48H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;49H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;50H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;51H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;52H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;53H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;54H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;55H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[12;56H")
        sys.stdout.write("-" + "")

        sys.stdout.write("\033[13;48H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;49H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;50H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;51H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;52H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;53H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;54H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;55H")
        sys.stdout.write("-" + "")
        sys.stdout.write("\033[13;56H")
        sys.stdout.write("-" + "")

        sys.stdout.write(f"\033[{self.input_y};0H")

        sys.stdout.flush()

    def clear_for_conclusion(self):
        for i in range(0, 300, 1):
            sys.stdout.write(f"\033[{self.input_y + 2};{i}H")
            sys.stdout.write(" ")
        for i in range(0, 300, 1):
            sys.stdout.write(f"\033[{self.input_y + 3};{i}H")
            sys.stdout.write(" ")
