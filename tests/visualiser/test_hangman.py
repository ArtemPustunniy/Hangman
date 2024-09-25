import re


def clean_ansi_escape_sequences(text: str) -> str:
    """
    Удаляет ANSI escape-последовательности из строки текста.

    ANSI escape-последовательности используются для управления выводом в терминале,
    такими как изменение цвета текста или очистка экрана. Эта функция удаляет их,
    оставляя только видимый текст.

    Параметры:
        text (str): Строка с возможными ANSI escape-последовательностями.

    Возвращает:
        str: Строка без ANSI escape-последовательностей.
    """
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi_escape.sub("", text)
