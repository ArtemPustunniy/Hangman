from src.visualiser.hangman import StaticHangman, DynamicHangman
from src.visualiser.display import DisplayConsole
from src.work_with_data.word import Word
from src.work_with_data.output import OutputsInGameLogics
from src.work_with_data.utils import Utils
from src.work_with_data.reader import Reader


class Game:
    """
    Класс, который управляет логикой игры в виселицу.

    Атрибуты:
        language (str): Язык игры.
        category_index (int): Индекс категории для выбора слов.
        level_index (int): Уровень сложности игры.
        is_actual (bool): Статус текущей игры (активная или завершенная).
        attempts (int): Количество оставшихся попыток.
        max_hints (int): Максимальное количество подсказок.
        errors_step_by_step (int): Количество ошибок по ходу игры.
        parts_of_hangman (int): Количество частей изображения виселицы.
        steps_in_play (str): Строка, представляющая шаги игры.
        guessed_letters (set): Набор угаданных букв.
        used_letters (set): Набор использованных букв.
        incorrect_guesses (int): Количество неправильных попыток.
        input_y (int): Позиция строки ввода на экране.
    """

    def __init__(
            self,
            language: str,
            category_index: int,
            level_index: int,
            is_actual: bool,
            attempts: int,
            max_hints: int,
    ):
        """
        Инициализация игры с заданными параметрами.

        Параметры:
            language (str): Язык игры.
            category_index (int): Индекс категории для выбора слов.
            level_index (int): Уровень сложности.
            is_actual (bool): Статус актуальности игры.
            attempts (int): Начальное количество попыток.
            max_hints (int): Максимальное количество подсказок.
        """
        self.language = language
        self.category_index = category_index
        self.level_index = level_index
        self.is_actual = is_actual
        self.attempts = attempts
        self.errors_step_by_step = 0
        self.max_hints = max_hints

        self.parts_of_hangman = 17
        self.steps_in_play = ""
        self.guessed_letters = set()
        self.used_letters = set()
        self.incorrect_guesses = 0
        self.input_y = 11

    def render_game_board(self) -> None:
        """
        Отображает игровое поле и управляет основной логикой игры.

        Метод создает слово, отображает его текущее состояние, управляет процессом
        угадывания букв и выводом результатов игры (победа или поражение).
        """
        new_word = Word(self.language, self.category_index, self.level_index)
        new_display = DisplayConsole(
            new_word.final_word,
            self.guessed_letters,
            self.input_y,
            new_word.category,
            new_word.level,
            self.attempts,
            self.language,
        )
        new_display.display_word_state()
        new_static_hangman = StaticHangman(
            self.parts_of_hangman, self.attempts
        )
        new_static_hangman.display_hangman_only()
        steps_in_play = new_static_hangman.get_steps_in_play()
        new_dinamic_hangman = DynamicHangman(self.incorrect_guesses, steps_in_play)
        game_output = OutputsInGameLogics(self.language, new_word.final_word, self.input_y)

        while new_dinamic_hangman.incorrect_guesses < len(steps_in_play) - 1:
            if self.errors_step_by_step == self.max_hints:
                new_display.hint = new_word.get_hint()
                new_display.change_has_hint()
            new_display.display_word_state()
            guess = game_output.input_letter()
            new_display.clear_for_conclusion()

            if len(guess) != 1 or not guess.isalpha():
                game_output.warning_about_one_letter()
                continue

            if guess in self.guessed_letters:
                game_output.warning_about_same_letter()
                continue

            if guess in self.used_letters:
                game_output.warning_about_same_used_letter()
                continue

            if guess in new_word.final_word:
                self.guessed_letters.add(guess)
                if all(letter in self.guessed_letters for letter in new_word.final_word):
                    new_display.display_word_state()
                    new_display.clear_for_conclusion()
                    game_output.win()
                    break
            else:
                self.used_letters.add(guess)
                new_dinamic_hangman.incorrect_guesses += 1
                self.attempts -= 1
                self.errors_step_by_step += 1

                new_dinamic_hangman.update_hangman()

        if new_dinamic_hangman.incorrect_guesses == len(steps_in_play) - 1:
            new_display.display_word_state()
            new_display.clear_for_conclusion()
            game_output.lose()

        self.is_actual = game_output.confirm_actual()

    def clear(self) -> None:
        """
        Сбрасывает состояние игры до начальных значений для начала новой игры.
        """
        self.attempts = 6
        Game.parts_of_hangman = 17
        Game.steps_in_play = ""
        Game.guessed_letters = set()
        Game.used_letters = set()
        Game.incorrect_guesses = 0
        Game.input_y = 11


class Play:
    """
    Класс, управляющий процессом запуска и перезапуска игры.

    Атрибуты:
        is_actual (bool): Определяет, должна ли игра быть активной.
    """

    def __init__(self):
        """
        Инициализирует объект класса Play с актуальным состоянием игры.
        """
        self.is_actual = True

    def start_game(self) -> None:
        """
        Запускает новый цикл игры, инициируя создание новых игровых объектов
        и управление процессом игры до завершения.
        """
        while True:
            _input = Reader.fill_input()
            new_game = Game(
                _input.language,
                _input.category_index,
                _input.level_index,
                self.is_actual,
                _input.attempts,
                _input.hints
            )
            new_game.render_game_board()
            if not new_game.is_actual:
                break
            else:
                new_game.clear()
                del _input
                del new_game
                Utils.clear_console()
