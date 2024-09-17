import sys


class StaticHangman:
    _hangman_steps = [
        ("|", 11, 55),
        ("|", 10, 55),
        ("|", 9, 55),
        ("|", 8, 55),
        ("|", 7, 55),
        ("|", 6, 55),
        ("+", 5, 55),
        ("-", 5, 54),
        ("-", 5, 53),
        ("-", 5, 52),
        ("+", 5, 51),
        ("|", 6, 51),
        ("O", 7, 51),
        ("|", 8, 51),
        ("/", 8, 49),
        (" \\", 8, 52),
        ("/", 9, 50),
        ("\\", 9, 52),
    ]

    def __init__(self, part_of_hangman, attempts):
        self.part_of_hangman = part_of_hangman
        self.attempts = attempts
        self.res = -1
        self.display_hangman_only()

    def display_hangman_only(self) -> None:
        for i in range(0, self.part_of_hangman - self.attempts + 1):
            sys.stdout.write(
                f"\033[{self._hangman_steps[i][1]};{self._hangman_steps[i][2]}H"
            )
            sys.stdout.write(self._hangman_steps[i][0])

    def get_steps_in_play(self) -> list:
        self.res = len(self._hangman_steps[self.part_of_hangman - self.attempts:])
        return self._hangman_steps[self.part_of_hangman - self.attempts:]

    @classmethod
    def get_hangman_steps(cls):
        return len(StaticHangman._hangman_steps)


class DinamicHangman:
    def __init__(self, incorrect_guesses, steps_in_play):
        self.incorrect_guesses = incorrect_guesses
        self.steps_in_play = steps_in_play

    def update_hangman(self) -> None:
        if self.incorrect_guesses < len(self.steps_in_play):
            step = self.steps_in_play[self.incorrect_guesses]
            sys.stdout.write(f"\033[{step[1]};{step[2]}H")
            sys.stdout.write(step[0])
            sys.stdout.flush()
