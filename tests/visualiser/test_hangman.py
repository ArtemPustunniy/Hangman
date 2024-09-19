import re
# from unittest.mock import patch
# from io import StringIO


def clean_ansi_escape_sequences(text):
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi_escape.sub("", text)
