from src.visualiser.hangman import StaticHangman, DinamicHangman
from src.visualiser.display import DisplayConsole
from src.work_with_data.input import Input
from src.work_with_data.word import Word
from src.work_with_data.output import OutputsInGameLogics
from src.work_with_data.utils import Utils


class Game:

    def __init__(
        self,
        language,
        category_index,
        level_index,
        is_actual,
        attempts,
        max_hints,
    ):
        self.language = language
        self.category_index = category_index
        self.level_index = level_index

        self.new_word = Word(self.language, self.category_index, self.level_index)

        self.word = self.new_word.final_word
        self.category = self.new_word.category
        self.level = self.new_word.level
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

        self.play_game()

    def play_game(self) -> None:
        new_display = DisplayConsole(
            self.word,
            self.guessed_letters,
            self.input_y,
            self.category,
            self.level,
            self.attempts,
            self.language,
        )
        steps_in_play = StaticHangman(
            self.parts_of_hangman, self.attempts
        ).get_steps_in_play()
        new_dinamic_hangman = DinamicHangman(self.incorrect_guesses, steps_in_play)
        game_output = OutputsInGameLogics(self.language, self.word, self.input_y)

        while new_dinamic_hangman.incorrect_guesses < len(steps_in_play) - 1:
            if self.errors_step_by_step == self.max_hints:
                new_display.hint = self.new_word.get_hint()
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

            if guess in self.word:
                self.guessed_letters.add(guess)
                if all(letter in self.guessed_letters for letter in self.word):
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
        self.attempts = 6
        Game.parts_of_hangman = 17
        Game.steps_in_play = ""
        Game.guessed_letters = set()
        Game.used_letters = set()
        Game.incorrect_guesses = 0
        Game.input_y = 11


class Play:
    def __init__(self):
        self.is_actual = True

    def start_game(self) -> None:
        while True:
            _input = Input()
            new_game = Game(
                _input.language,
                _input.category_index,
                _input.level_index,
                self.is_actual,
                _input.attempts,
                _input.hints
            )
            if not new_game.is_actual:
                break
            else:
                new_game.clear()
                del _input
                del new_game
                Utils.clear_console()
