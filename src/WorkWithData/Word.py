import random
from collections import Counter
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
            "constructor",
            "puzzle",
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
            "puzzles",
            "racket",
            "billiards",
            "chess",
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
            "конструктор",
            "пазл",
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
            "паровозик",
            "пазлы",
            "ракетка",
            "бильярд",
            "шахматы",
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

    dict_hints = {
        "animals": [
            "a soft, kind domestic animal",  # cat
            "a loyal, furry friend of humans",  # dog
            "a flying creature with feathers",  # bird
            "an underwater inhabitant with fins",  # fish
            "a huge animal with a trunk",  # elephant
            "a tall animal with a long neck",  # giraffe
            "a smart marine mammal",  # dolphin
            "a marsupial hopping animal",  # kangaroo
            "a heavy animal living near water",  # hippopotamus
            "a close relative of humans, a smart ape",  # chimpanzee
            "a large orange ape",  # orangutan
            "a huge animal with a horn on its nose",  # rhinoceros
            "a striped predator from the jungle",  # tiger
            "the king of beasts with a red mane",  # lion
            "a wild relative of dogs living in forests",  # wolf
            "a fast animal with long ears",  # hare
            "a large predatory reptile",  # crocodile
            "an animal that can live without water for a long time",  # camel
            "a small rodent with a long tail",  # mouse
            "a fast domestic animal you can ride",  # horse
            "a graceful animal with antlers, living in the forest",  # deer
            "a wild pig with large tusks",  # boar
            "a waterfowl",  # duck
            "a small sparrow bird",  # sparrow
            "a predatory bird with sharp eyesight",  # hawk
            "a nocturnal bird with large eyes",  # owl
            "a talking exotic bird",  # parrot
            "a slow creature with a shell",  # turtle
            "a dangerous marine predator with fins",  # shark
            "a stubborn animal often used for carrying loads",  # donkey
        ],
        "toys": [
            "a round object for playing",  # ball
            "a miniature figure representing a person",  # doll
            "a set of parts for building models",  # construction set
            "a mind game where the task is to assemble the whole from pieces",  # puzzle
            "a model car for playing",  # toy car
            "a toy mechanism resembling a human",  # robot
            "a small model of a boat",  # toy boat
            "a toy airplane for children",  # toy airplane
            "a curved throwing stick",  # boomerang
            "a mechanical toy that changes shape",  # transformer
            "a musical instrument with keys",  # synthesizer
            "a stringed musical instrument",  # guitar
            "a wind instrument with a melodic sound",  # flute
            "a toy marionette on strings",  # puppet
            "a toy gun",  # toy gun
            "a brain game that requires assembling a figure",  # brain teaser
            "a tool for playing tennis",  # racket
            "a game with balls on a table",  # billiards
            "a tabletop strategy game",  # chess
            "a game with a shuttlecock and rackets",  # badminton
        ],
        "vegetables": [
            "a red juicy vegetable",  # tomato
            "a green long vegetable",  # cucumber
            "a root vegetable used in cooking",  # potato
            "an orange root vegetable",  # carrot
            "a red vegetable with a rich flavor",  # beetroot
            "a green leafy vegetable",  # cabbage
            "an aromatic vegetable with a sharp flavor",  # onion
            "a pungent spice with a sharp taste",  # garlic
            "a hot or sweet pepper",  # pepper
            "a purple elongated vegetable",  # eggplant
            "a green zucchini",  # zucchini
            "a crunchy root vegetable with a sharp taste",  # radish
            "a yellow round root vegetable",  # turnip
            "a green leafy vegetable for salads",  # lettuce
            "a long green vegetable with soft shoots",  # asparagus
            "a crunchy green vegetable with an aroma",  # celery
            "aromatic greens for dishes",  # parsley
            "aromatic greens with a strong smell",  # dill
            "a green vegetable in the shape of a tree",  # broccoli
            "a white vegetable in the shape of a tree",  # cauliflower
            "a leafy green vegetable",  # spinach
            "a legume plant",  # beans
            "small green pods",  # peas
            "a large orange vegetable",  # pumpkin
            "a hot spice from a root",  # horseradish
            "a crunchy hot root vegetable",  # radish
            "a green aromatic herb",  # green onion
            "a hot pungent root",  # ginger
            "a root with a sharp taste",  # horseradish
        ],
        "fruit": [
            "a round fruit that grows in orchards",  # apple
            "a juicy citrus fruit",  # orange
            "a sour citrus with a bright taste",  # lemon
            "an exotic tropical fruit",  # pineapple
            "a sweet juicy fruit with a pit",  # peach
            "a small orange fruit with a pit",  # apricot
            "a tropical fruit with a bright flavor",  # mango
            "a pear-shaped fruit with soft flesh",  # pear
            "a small fruit growing on vines",  # grape
            "a large fruit with a green rind",  # melon
            "a huge sweet fruit with red flesh",  # watermelon
            "a red berry with tiny seeds",  # strawberry
            "a small red berry",  # raspberry
            "a sour berry of black or red color",  # currant
            "a sweet forest berry",  # blackberry
            "a sour bog berry",  # cranberry
            "a blue berry with a rich flavor",  # blueberry
            "a forest berry",  # bilberry
            "a sweet dried fruit",  # date
            "a fruit with soft and sweet flesh",  # fig
            "a long yellow fruit",  # banana
            "a sour-sweet fuzzy fruit",  # kiwi
            "a sweet tropical fruit with bright flesh",  # papaya
            "a large citrus with a bitter taste",  # grapefruit
            "a green fruit with buttery flesh",  # avocado
            "a large yellow citrus",  # pomelo
            "a fruit in the shape of a star",  # starfruit
            "a red fruit with many tiny seeds",  # pomegranate
            "an exotic fruit with tender flesh",  # lychee
            "an orange fruit with an astringent taste",  # persimmon
        ],
    }

    dict_hints_in_Russian = {
        "животные": [
            "мягкое доброе домашнее животное",  # кошка
            "верный лохматый друг человека",  # собака
            "летающее существо с перьями",  # птица
            "подводный обитатель с плавниками",  # рыба
            "огромное животное с хоботом",  # слон
            "высокое животное с длинной шеей",  # жираф
            "умное морское млекопитающее",  # дельфин
            "сумчатое прыгающее животное",  # кенгуру
            "тяжелое животное, живущее возле воды",  # гиппопотам
            "близкий родственник человека, умная обезьяна",  # шимпанзе
            "большая рыжая обезьяна",  # орангутан
            "огромное животное с рогом на носу",  # носорог
            "полосатый хищник из джунглей",  # тигр
            "царь зверей с рыжей гривой",  # лев
            "дикий родственник собаки, живущий в лесах",  # волк
            "быстрое животное с длинными ушами",  # заяц
            "крупный хищный рептилий",  # крокодил
            "животное, способное долго жить без воды",  # верблюд
            "маленький грызун с длинным хвостом",  # мышь
            "быстрое домашнее животное, на котором ездят",  # лошадь
            "изящное животное с рогами, обитающее в лесу",  # олень
            "дикая свинья с большими клыками",  # кабан
            "водоплавающая птица",  # утка
            "маленькая воробьиная птица",  # воробей
            "хищная птица с острым зрением",  # ястреб
            "ночная птица с большими глазами",  # сова
            "говорящая экзотическая птица",  # попугай
            "медлительное существо с панцирем",  # черепаха
            "опасный морской хищник с плавниками",  # акула
            "упрямое животное, часто используемое для перевозки грузов",  # осел
        ],
        "игрушки": [
            "круглый предмет для игр",  # мяч
            "миниатюрная фигурка, изображающая человека",  # кукла
            "вращающийся волчок для детей",  # юла
            "набор деталей для строительства моделей",  # конструктор
            "игра для ума с задачей собрать целое из частей",  # пазл
            "модель автомобиля для игры",  # машинка
            "игрушечный механизм, похожий на человека",  # робот
            "маленькая модель лодки",  # лодка
            "игрушечный самолет для детей",  # самолет
            "изогнутая палка для метания",  # бумеранг
            "механическая игрушка, меняющая форму",  # трансформер
            "музыкальный инструмент с клавишами",  # синтезатор
            "струнный музыкальный инструмент",  # гитара
            "духовой инструмент с мелодичным звуком",  # флейта
            "игрушечная марионетка на нитках",  # кукла-марионетка
            "игрушечный пистолет",  # пистолет
            "миниатюрный поезд для игр",  # игрушечный поезд
            "мозговая игра, требующая сложить фигуру",  # головоломка
            "инструмент для игры в теннис",  # ракетка
            "игра с шарами на столе",  # бильярд
            "настольная стратегическая игра",  # шахматы
            "игра с воланчиком и ракетками",  # бадминтон
        ],
        "овощи": [
            "красный сочный овощ",  # помидор
            "зелёный длинный овощ",  # огурец
            "корнеплод, используемый для приготовления еды",  # картофель
            "оранжевый корнеплод",  # морковь
            "красный овощ с насыщенным вкусом",  # свекла
            "зелёный листовой овощ",  # капуста
            "ароматный овощ с острым вкусом",  # лук
            "ароматная пряность с острым вкусом",  # чеснок
            "острый или сладкий перец",  # перец
            "фиолетовый продолговатый овощ",  # баклажан
            "зелёный кабачок",  # цуккини
            "маленький круглый кабачок",  # патиссон
            "хрустящий корнеплод с острым вкусом",  # редис
            "жёлтый круглый корнеплод",  # репа
            "зелёный листовой овощ для салатов",  # салат
            "длинный зелёный овощ с мягкими побегами",  # спаржа
            "хрустящий зелёный овощ с ароматом",  # сельдерей
            "ароматная зелень для блюд",  # петрушка
            "ароматная зелень с сильным запахом",  # укроп
            "зелёный овощ в форме деревца",  # брокколи
            "лиственный зелёный овощ",  # шпинат
            "бобовое растение",  # фасоль
            "маленькие зелёные стручки",  # горох
            "крупный оранжевый овощ",  # тыква
            "острая пряность из корня",  # хрен
            "хрустящий острый корнеплод",  # редька
            "зелёная ароматная травка",  # зелёный лук
            "острый пряный корень",  # имбирь
            "корень с острым вкусом",  # хрен
        ],
        "фрукты": [
            "круглый фрукт, растущий в садах",  # яблоко
            "сочный цитрусовый плод",  # апельсин
            "кислый цитрус с ярким вкусом",  # лимон
            "экзотический тропический фрукт",  # ананас
            "сладкий сочный фрукт с косточкой",  # персик
            "мелкий оранжевый фрукт с косточкой",  # абрикос
            "тропический плод с ярким вкусом",  # манго
            "грушевидный фрукт с мягкой мякотью",  # груша
            "мелкий фрукт, растущий на лозах",  # виноград
            "крупный плод с зелёной коркой",  # дыня
            "огромный сладкий фрукт с красной мякотью",  # арбуз
            "красная ягода с мелкими семечками",  # клубника
            "мелкая красная ягода",  # малина
            "кислая ягода чёрного или красного цвета",  # смородина
            "сладкая лесная ягода",  # ежевика
            "кислая болотная ягода",  # клюква
            "синяя ягода с насыщенным вкусом",  # черника
            "лесная ягода",  # голубика
            "сладкий сушёный плод",  # финик
            "плод с мягкой и сладкой мякотью",  # инжир
            "длинный жёлтый фрукт",  # банан
            "кисло-сладкий пушистый фрукт",  # киви
            "сладкий тропический плод с яркой мякотью",  # папайя
            "крупный цитрус с горьковатым вкусом",  # грейпфрут
            "зелёный фрукт с маслянистой мякотью",  # авокадо
            "крупный жёлтый цитрус",  # помело
            "фрукт в форме звезды",  # карамбола
            "красный плод с множеством мелких зёрен",  # гранат
            "экзотический плод с нежной мякотью",  # личи
            "оранжевый фрукт с терпким вкусом",  # хурма
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
            except ValueError:
                InfoForInput.error_log()
        else:
            try:
                if self.category_index == 5:
                    self.category_index = random.randint(1, 4)
                self.category = self.list_category_in_Russian[self.category_index - 1]
                if self.level_index == 4:
                    self.level_index = random.randint(1, 3)
                self.level = self.list_level_in_Russian[self.level_index - 1]
            except ValueError:
                InfoForInput.error_log()

        self.select_strings_by_difficulty()

    def select_strings_by_difficulty(self) -> None:
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
        return

    def get_hint(self) -> str:
        if self.language == 1:
            try:
                result = self.dict_hints[self.category][self.dict_words[self.category].index(self.final_word)]
                return result
            except ValueError:
                InfoForInput.error_log()
        else:
            try:
                result = self.dict_hints_in_Russian[self.category][self.dict_words_in_Russian[self.category].index(self.final_word)]
                return result
            except ValueError:
                InfoForInput.error_log()
