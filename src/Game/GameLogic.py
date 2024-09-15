from src.Visualiser.Hangman import Static_Hangman, Dinamic_Hangman
from src.Visualiser.Display import DisplayConsole
from src.WorkWithData.Input import Input
from src.WorkWithData.Word import Word
from src.WorkWithData.Output import OutputsInGameLogics
from src.WorkWithData.Utils import Utils


class Game:
    # attempts = 6
    parts_of_hangman = 17
    steps_in_play = ""
    guessed_letters = set()
    used_letters = set()
    incorrect_guesses = 0
    input_y = 11

    def __init__(
        self,
        language,
        category_index,
        level_index,
        actual,
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
        self.actual = actual
        self.attempts = attempts
        self.errors_step_by_step = 0
        self.max_hints = max_hints

        self.play_game()

    def play_game(self) -> None:
        new_display = DisplayConsole(
            self.word,
            Game.guessed_letters,
            Game.input_y,
            self.category,
            self.level,
            self.attempts,
            self.language,
        )
        steps_in_play = Static_Hangman(
            Game.parts_of_hangman, self.attempts
        ).get_steps_in_play()
        new_dinamic_hangman = Dinamic_Hangman(Game.incorrect_guesses, steps_in_play)
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

            if guess in Game.guessed_letters:
                game_output.warning_about_same_letter()
                continue

            if guess in Game.used_letters:
                game_output.warning_about_same_used_letter()
                continue

            if guess in self.word:
                Game.guessed_letters.add(guess)
                if all(letter in Game.guessed_letters for letter in self.word):
                    new_display.display_word_state()
                    new_display.clear_for_conclusion()
                    game_output.win()
                    break
            else:
                Game.used_letters.add(guess)
                new_dinamic_hangman.incorrect_guesses += 1
                self.attempts -= 1
                self.errors_step_by_step += 1

                new_dinamic_hangman.update_hangman()

        if new_dinamic_hangman.incorrect_guesses == len(steps_in_play) - 1:
            new_display.display_word_state()
            new_display.clear_for_conclusion()
            game_output.lose()

        self.actual = game_output.confirm_actual()
        return

    def clear(self) -> None:
        self.attempts = 6
        Game.parts_of_hangman = 17
        Game.steps_in_play = ""
        Game.guessed_letters = set()
        Game.used_letters = set()
        Game.incorrect_guesses = 0
        Game.input_y = 11
        return


class Play:
    def __init__(self):
        self.actual = True

    def start_game(self) -> None:
        while True:
            _input = Input()
            new_game = Game(
                _input.language,
                _input.category_index,
                _input.level_index,
                self.actual,
                _input.attempts,
                _input.hints
            )
            if not new_game.actual:
                break
            else:
                new_game.clear()
                # del new_word
                del _input
                del new_game
                Utils.clear_console()
        return
