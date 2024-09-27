from .output import InfoForInput


class Input:
    """
    Класс для хранения и обработки данных, вводимых пользователем перед началом игры.

    Атрибуты:
        language (int): Выбранный язык (-1, если не выбран).
        category_index (int): Индекс выбранной категории (-1, если не выбран).
        level_index (int): Индекс выбранного уровня сложности (-1, если не выбран).
        attempts (int): Количество доступных попыток (-1, если не указано).
        hints (int): Количество доступных подсказок (по умолчанию 0).
        info_input (InfoForInput): Объект, содержащий информацию для обработки ввода.
    """

    def __init__(self):
        """
        Инициализирует объект Input с начальными значениями для всех параметров.

        Значения по умолчанию:
            language: -1 (не выбран).
            category_index: -1 (не выбрана категория).
            level_index: -1 (не выбран уровень сложности).
            attempts: -1 (не указано количество попыток).
            hints: 0 (подсказки отсутствуют).
            info_input: объект класса InfoForInput с параметром 0.
        """
        self.language = -1
        self.category_index = -1
        self.level_index = -1
        self.attempts = -1
        self.hints = 0
        self.info_input = InfoForInput(0)
