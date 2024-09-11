import re
# from unittest.mock import patch
# from io import StringIO


def clean_ansi_escape_sequences(text):
    ansi_escape = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi_escape.sub("", text)


# @pytest.fixture
# def static_hangman():
#     return Static_Hangman(part_of_hangman=10, attempts=2)


# @pytest.fixture
# def dinamic_hangman(static_hangman):
#     steps_in_play = static_hangman.get_steps_in_play()
#     return Dinamic_Hangman(incorrect_guesses=2, steps_in_play=steps_in_play)


# class TestHangman:
    # def test_display_hangman_only(self, static_hangman):
    #     with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
    #         static_hangman.display_hangman_only()
    #         output = clean_ansi_escape_sequences(mock_stdout.getvalue())
    #         assert "|" in output
    #         assert "+" in output

    # def test_get_steps_in_play(self, static_hangman):
    #     steps = static_hangman.get_steps_in_play()
    #     assert len(steps) > 0
    #     assert steps[-1] == ("|", 8, 51)

    # def test_update_hangman(self, dinamic_hangman):
    #     with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
    #         dinamic_hangman.update_hangman()
    #         output = clean_ansi_escape_sequences(mock_stdout.getvalue())
    #         # Проверка, что шаг виселицы был обновлен
    #         assert "/" in output or "\\" in output
