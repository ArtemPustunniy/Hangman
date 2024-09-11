import sys


class OutputsInGameLogics:
    def __init__(self, language, word, input_y):
        self.language = language
        self.word = word
        self.input_y = input_y
        self.actual = ""

    def input_letter(self):
        result = input(
            "\nВведите букву: " if self.language == 2 else "\nInput a letter: "
        ).lower()
        return result

    def warning_about_one_letter(self):
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        sys.stdout.write(
            "Пожалуйста, введите одну букву."
            if self.language == 2
            else "Please, input one letter"
        )

    def warning_about_same_letter(self):
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        sys.stdout.write(
            "Вы уже угадали эту букву.\nПопробуйте другую."
            if self.language == 2
            else "You have already guessed this letter.\nTry another one."
        )

    def warning_about_same_used_letter(self):
        sys.stdout.write(f"\033[{self.input_y + 2};0H")
        sys.stdout.write(
            "Вы уже пытались угадать эту букву.\nПопробуйте другую."
            if self.language == 2
            else "You have already tried to guess this letter.\nTry another one."
        )

    def win(self):
        if self.language == 2:
            sys.stdout.write(f"\033[{self.input_y + 2};0H")
            sys.stdout.write(
                f"\033[{self.input_y + 2};0HПоздравляем!\nВы угадали слово: {self.word}"
            )
        else:
            sys.stdout.write(f"\033[{self.input_y + 2};0H")
            sys.stdout.write(
                f"\033[{self.input_y + 2};0HCongratulations!\nYou guessed the word: {self.word}"
            )

    def lose(self):
        if self.language == 2:
            sys.stdout.write(f"\033[{self.input_y + 2};0H")
            sys.stdout.write(
                f"\033[{self.input_y + 2};0HВы проиграли.\nЗагаданное слово было: {self.word}"
            )
        else:
            sys.stdout.write(f"\033[{self.input_y + 2};0H")
            sys.stdout.write(
                f"\033[{self.input_y + 2};0HYou have lost.\nThe hidden word was: {self.word}"
            )

    def confirm_actual(self):
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
    def __init__(self, language, category, level, attempts, input_y):
        self.language = language
        self.category = category
        self.level = level
        self.attempts = attempts
        self.input_y = input_y

    def output_game_info(self):
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
        sys.stdout.write(f"\033[{self.input_y};0H")
        sys.stdout.write(" " * 50)
        sys.stdout.write(f"\033[{self.input_y};0H")
        sys.stdout.write("Слово: " if self.language == 2 else "Word: ")


class InfoForInput:
    def __init__(self, language):
        self.language = language

    def language_info(self):
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

    def warning_unavailable_language_number(self):
        print("Please enter an available language number\n")

    def category_index_info(self):
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

    def warning_unavailable_category_number(self):
        print(
            "Пожалуйста, введите доступный номер категории"
            if self.language == 2
            else "Please enter an available category number"
        )

    def level_info(self):
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

    def warning_unavailable_level_number(self):
        print(
            "Пожалуйста, введите доступный уровень сложности"
            if self.language == 2
            else "Please enter the available difficulty level"
        )

    def attempts_info(self):
        result = int(
            input(
                "Введите максимальное число ошибок (от 2 до 17) "
                if self.language == 2
                else "Enter the maximum number of errors (from 2 to 17) "
            )
        )
        return result

    def warning_unavailable_attempts_number(self):
        print(
            "Пожалуйста введите допустимое число попыток"
            if self.language == 2
            else "Please enter the allowed number of attempts"
        )
