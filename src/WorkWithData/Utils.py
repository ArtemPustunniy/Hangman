import random

import os


class Utils:
    @classmethod
    def get_random_key(cls, dictionary):
        return random.choice(list(dictionary.keys()))

    @classmethod
    def get_random_category(cls):
        random_number = random.randint(0, 2)
        return random_number

    @classmethod
    def clear_console(cls):
        os.system("cls" if os.name == "nt" else "clear")
