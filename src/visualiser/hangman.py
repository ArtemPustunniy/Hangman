import sys


class StaticHangman:
    """
    Класс для отображения статической части виселицы.

    Атрибуты:
        _hangman_steps (list): Список шагов для построения виселицы, где каждый шаг представлен символом и его координатами.
        part_of_hangman (int): Общее количество частей виселицы.
        attempts (int): Количество оставшихся попыток.
        res (int): Переменная для хранения длины оставшихся шагов виселицы.
    """

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

    def __init__(self, part_of_hangman: int, attempts: int):
        """
        Инициализирует объект StaticHangman с заданным количеством частей виселицы и оставшимися попытками.

        Параметры:
            part_of_hangman (int): Общее количество частей виселицы.
            attempts (int): Количество оставшихся попыток.
        """
        self.part_of_hangman = part_of_hangman
        self.attempts = attempts
        self.res = -1

    def display_hangman_only(self) -> None:
        """
        Отображает текущую статическую часть виселицы в консоли в зависимости от количества оставшихся попыток.
        """
        for i in range(0, self.part_of_hangman - self.attempts + 1):
            sys.stdout.write(
                f"\033[{self._hangman_steps[i][1]};{self._hangman_steps[i][2]}H"
            )
            sys.stdout.write(self._hangman_steps[i][0])

    def get_steps_in_play(self) -> list:
        """
        Возвращает оставшиеся шаги построения виселицы, которые еще не были выполнены.

        Возвращает:
            list: Список шагов виселицы для выполнения.
        """
        self.res = len(self._hangman_steps[self.part_of_hangman - self.attempts:])
        return self._hangman_steps[self.part_of_hangman - self.attempts:]

    @classmethod
    def get_hangman_steps(cls) -> int:
        """
        Возвращает общее количество шагов для построения виселицы.

        Возвращает:
            int: Количество шагов виселицы.
        """
        return len(StaticHangman._hangman_steps)


class DynamicHangman:
    """
    Класс для динамического обновления состояния виселицы во время игры.

    Атрибуты:
        incorrect_guesses (int): Количество неправильных попыток игрока.
        steps_in_play (list): Список шагов для динамического отображения виселицы.
    """

    def __init__(self, incorrect_guesses: int, steps_in_play: list):
        """
        Инициализирует объект DynamicHangman с количеством неправильных попыток и оставшимися шагами виселицы.

        Параметры:
            incorrect_guesses (int): Количество неправильных попыток.
            steps_in_play (list): Оставшиеся шаги для динамического отображения виселицы.
        """
        self.incorrect_guesses = incorrect_guesses
        self.steps_in_play = steps_in_play

    def update_hangman(self) -> None:
        """
        Обновляет состояние виселицы на экране, добавляя новую часть виселицы при каждой неправильной попытке.
        """
        if self.incorrect_guesses < len(self.steps_in_play):
            step = self.steps_in_play[self.incorrect_guesses]
            sys.stdout.write(f"\033[{step[1]};{step[2]}H")
            sys.stdout.write(step[0])
            sys.stdout.flush()
