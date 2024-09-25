import pytest
from src.work_with_data.word import Word


class TestWord:
    """
    Класс для тестирования методов и функциональности класса Word.
    """

    def test_word_selection_english_easy(self):
        """
        Тестирует выбор слова на английском языке для категории "Животные" с легким уровнем сложности.

        Проверяет:
            - Слово должно быть длиной не более 4 символов.
        """
        word = Word(1, 1, 1)  # English, Animals, Easy
        assert len(word.final_word) <= 4

    def test_word_selection_russian_medium(self):
        """
        Тестирует выбор слова на русском языке для категории "Игрушки" со средним уровнем сложности.

        Проверяет:
            - Слово должно содержать повторяющиеся буквы (например, "а", "е", "и").
        """
        word = Word(2, 2, 2)  # Russian, Toys, Medium
        assert any(
            c in word.final_word for c in ["а", "е", "и"]
        )  # проверка на наличие повторяющихся букв

    def test_word_selection_raises_value_error(self):
        """
        Тестирует выброс исключения IndexError при выборе неверного уровня сложности.

        Проверяет:
            - Вызов конструктора Word с некорректным уровнем сложности вызывает IndexError.
        """
        with pytest.raises(IndexError):
            Word(1, 1, 10)  # Неверный уровень сложности
