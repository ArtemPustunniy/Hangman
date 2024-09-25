import re


def clean_ansi_escape_sequences(text):
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi_escape.sub("", text)
