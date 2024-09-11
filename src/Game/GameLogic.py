from Visualiser.Hangman import Static_Hangman, Dinamic_Hangman
from Visualiser.Display import Display_Console
from WorkWithData.Input import Input
from WorkWithData.Word import Word
from WorkWithData.Output import OutputsInGameLogics
from WorkWithData.Utils import Utils


class Game:
    attempts = 6
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
        word,
        category,
        level,
        actual,
        attempts,
    ):
        self.language = language
        self.category_index = category_index
        self.level_index = level_index
        self.word = word
        self.category = category
        self.level = level
        self.actual = actual
        self.attempts = attempts

        self.play_game()

    def play_game(self):
        new_display = Display_Console(
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

                new_dinamic_hangman.update_hangman()

        if new_dinamic_hangman.incorrect_guesses == len(steps_in_play) - 1:
            new_display.display_word_state()
            new_display.clear_for_conclusion()
            game_output.lose()

        self.actual = game_output.confirm_actual()

    def clear(self):
        self.attempts = 6
        Game.parts_of_hangman = 17
        Game.steps_in_play = ""
        Game.guessed_letters = set()
        Game.used_letters = set()
        Game.incorrect_guesses = 0
        Game.input_y = 11


class Play:
    def __init__(self):
        self.actual = True

    def start_game(self):
        while True:
            _input = Input()
            new_word = Word(_input.language, _input.category_index, _input.level_index)
            new_game = Game(
                _input.language,
                _input.category_index,
                _input.level_index,
                new_word.final_word,
                new_word.category,
                new_word.level,
                self.actual,
                _input.attempts,
            )
            if not new_game.actual:
                break
            else:
                new_game.clear()
                del new_word
                del _input
                del new_game
                Utils.clear_console()
