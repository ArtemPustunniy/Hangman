from .output import InfoForInput


class Input:
    def __init__(self):
        self.language = -1
        self.category_index = -1
        self.level_index = -1
        self.attempts = -1
        self.hints = 0
        self.info_input = InfoForInput(0)
