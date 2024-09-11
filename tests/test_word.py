import pytest
from WorkWithData.Word import Word


class TestWord:
    def test_word_selection_english_easy(self):
        word = Word(1, 1, 1)  # English, Animals, Easy
        assert len(word.final_word) <= 4

    def test_word_selection_russian_medium(self):
        word = Word(2, 2, 2)  # Russian, Toys, Medium
        assert any(
            c in word.final_word for c in ["а", "е", "и"]
        )  # check for repeated letters

    def test_word_selection_raises_value_error(self):
        with pytest.raises(IndexError):
            Word(1, 1, 10)  # Invalid difficulty level
