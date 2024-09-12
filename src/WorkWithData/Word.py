import random
from collections import Counter
# from src.WorkWithData.Output import InfoForInput
from .Output import InfoForInput


class Word:
    list_category = ["animals", "toys", "vegetables", "fruit", "random"]
    list_level = ["easy", "medium", "hard", "random"]

    dict_words = {
        "animals": [
            "cat",
            "dog",
            "bird",
            "fish",
            "elephant",
            "giraffe",
            "dolphin",
            "kangaroo",
            "hippopotamus",
            "chimpanzee",
            "orangutan",
            "rhinoceros",
            "tiger",
            "lion",
            "wolf",
            "hare",
            "crocodile",
            "camel",
            "mouse",
            "horse",
            "deer",
            "boar",
            "duck",
            "sparrow",
            "hawk",
            "owl",
            "parrot",
            "turtle",
            "shark",
            "donkey",
        ],
        "toys": [
            "ball",
            "doll",
            "spinning top",
            "yo-yo",
            "constructor",
            "puzzle",
            "teddy bear",
            "car",
            "robot",
            "boat",
            "airplane",
            "boomerang",
            "transformer",
            "synthesizer",
            "guitar",
            "flute",
            "puppet",
            "gun",
            "train set",
            "racing track",
            "toy train",
            "puzzles",
            "racket",
            "Rubik's cube",
            "billiards",
            "tennis ball",
            "chess",
            "table hockey",
            "table tennis",
            "badminton",
        ],
        "vegetables": [
            "tomato",
            "cucumber",
            "potato",
            "carrot",
            "beetroot",
            "cabbage",
            "onion",
            "garlic",
            "pepper",
            "eggplant",
            "zucchini",
            "pattypan squash",
            "radish",
            "turnip",
            "lettuce",
            "asparagus",
            "celery",
            "parsley",
            "dill",
            "broccoli",
            "cauliflower",
            "spinach",
            "beans",
            "peas",
            "pumpkin",
            "horseradish",
            "radish",
            "chives",
            "ginger",
            "horseradish",
        ],
        "fruit": [
            "apple",
            "orange",
            "lemon",
            "pineapple",
            "peach",
            "apricot",
            "mango",
            "pear",
            "grape",
            "melon",
            "watermelon",
            "strawberry",
            "raspberry",
            "currant",
            "blackberry",
            "cranberry",
            "blueberry",
            "huckleberry",
            "date",
            "fig",
            "banana",
            "kiwi",
            "papaya",
            "grapefruit",
            "avocado",
            "pomelo",
            "carambola",
            "pomegranate",
            "lychee",
            "persimmon",
        ],
    }

    list_category_in_Russian = ["животные", "игрушки", "овощи", "фрукты", "рандомная"]
    list_level_in_Russian = ["легко", "средний", "сложный", "рандомный"]

    dict_words_in_Russian = {
        "животные": [
            "кот",
            "собака",
            "птица",
            "рыба",
            "слон",
            "жираф",
            "дельфин",
            "кенгуру",
            "гиппопотам",
            "шимпанзе",
            "орангутан",
            "носорог",
            "тигр",
            "лев",
            "волк",
            "заяц",
            "крокодил",
            "верблюд",
            "мышь",
            "лошадь",
            "олень",
            "кабан",
            "утка",
            "воробей",
            "ястреб",
            "сова",
            "попугай",
            "черепаха",
            "акула",
            "осел",
        ],
        "игрушки": [
            "мяч",
            "кукла",
            "волчок",
            "йо-йо",
            "конструктор",
            "пазл",
            "плюшевый медведь",
            "машинка",
            "робот",
            "лодка",
            "самолет",
            "бумеранг",
            "трансформер",
            "синтезатор",
            "гитара",
            "флейта",
            "петрушка",
            "пистолет",
            "железная дорога",
            "гоночный трек",
            "паровозик",
            "пазлы",
            "ракетка",
            "кубик Рубика",
            "бильярд",
            "теннисный мяч",
            "шахматы",
            "настольный хоккей",
            "настольный теннис",
            "бадминтон",
        ],
        "овощи": [
            "помидор",
            "огурец",
            "картофель",
            "морковь",
            "свекла",
            "капуста",
            "лук",
            "чеснок",
            "перец",
            "баклажан",
            "кабачок",
            "патиссон",
            "редиска",
            "репа",
            "салат",
            "спаржа",
            "сельдерей",
            "петрушка",
            "укроп",
            "брокколи",
            "цветная капуста",
            "шпинат",
            "фасоль",
            "горох",
            "тыква",
            "редька",
            "цуккини",
            "шнитт-лук",
            "имбирь",
            "хрен",
        ],
        "фрукты": [
            "яблоко",
            "апельсин",
            "лимон",
            "ананас",
            "персик",
            "абрикос",
            "манго",
            "груша",
            "виноград",
            "дыня",
            "арбуз",
            "клубника",
            "малина",
            "смородина",
            "ежевика",
            "клюква",
            "черника",
            "голубика",
            "финик",
            "инжир",
            "банан",
            "киви",
            "папайя",
            "грейпфрут",
            "авокадо",
            "помело",
            "карамбола",
            "гранат",
            "личи",
            "хурма",
        ],
    }

    def __init__(self, language, category_index, level_index):
        self.language = language
        self.strings = ""
        self.level = ""
        self.__result = []
        self.final_word = ""
        self.category_index = category_index
        self.level_index = level_index
        self.category = ""

        # print(self.category_index)

        if self.language == 1:
            try:
                if self.category_index == 5:
                    self.category_index = random.randint(1, 4)
                self.category = self.list_category[self.category_index - 1]
                if self.level_index == 4:
                    self.level_index = random.randint(1, 3)
                self.level = self.list_level[self.level_index - 1]
            except TypeError:
                InfoForInput.error_log()
        else:
            try:
                if self.category_index == 5:
                    self.category_index = random.randint(1, 4)
                self.category = self.list_category_in_Russian[self.category_index - 1]
                if self.level_index == 4:
                    self.level_index = random.randint(1, 3)
                self.level = self.list_level_in_Russian[self.level_index - 1]
            except TypeError:
                InfoForInput.error_log()

        self.select_strings_by_difficulty()

    def select_strings_by_difficulty(self):
        for string in (
            self.dict_words[self.category]
            if self.language == 1
            else self.dict_words_in_Russian[self.category]
        ):
            if self.level_index == 1:
                if len(string) <= 4:
                    self.__result.append(string)

            elif self.level_index == 2:
                if len(string) > 4:
                    counter = Counter(string)
                    repeated_chars = [
                        char for char, count in counter.items() if count >= 3
                    ]
                    if repeated_chars:
                        self.__result.append(string)

            elif self.level_index == 3:
                if len(string) > 4:
                    counter = Counter(string)
                    if all(count <= 2 for count in counter.values()):
                        self.__result.append(string)
            else:
                raise ValueError
        self.final_word = random.choice(self.__result)
