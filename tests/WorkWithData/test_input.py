# import pytest
# from src.WorkWithData.Input import Input
#
#
# class TestInput:
#
#     @pytest.fixture(autouse=True)
#     def setup_method(self):
#         self.input_instance = Input()
#
#     def test_input_language_valid(self, mocker):
#         # Корректное значение языка
#         mocker.patch("Output.InfoForInput.language_info", return_value=1)
#         mocker.patch("Utils.Utils.clear_console")
#         self.input_instance.input_language()
#         assert self.input_instance.language == 1
#
#     def test_input_language_invalid(self, mocker):
#         # Некорректное значение языка сначала (-1), затем корректное (1)
#         mocker.patch("Output.InfoForInput.language_info", side_effect=[-1, 1])
#         mocker.patch("Utils.Utils.clear_console")
#         mocker.patch("Output.InfoForInput.warning_unavailable_language_number")
#         self.input_instance.input_language()
#         assert self.input_instance.language == 1
#
#     def test_input_category_valid(self, mocker):
#         # Корректное значение категории
#         mocker.patch("Output.InfoForInput.category_index_info", return_value=3)
#         mocker.patch("Utils.Utils.clear_console")
#         self.input_instance.input_category_index()
#         assert self.input_instance.category_index == 3
#
#     def test_input_category_invalid(self, mocker):
#         # Некорректное значение категории сначала (0), затем корректное (2)
#         mocker.patch("Output.InfoForInput.category_index_info", side_effect=[0, 2])
#         mocker.patch("Utils.Utils.clear_console")
#         mocker.patch("Output.InfoForInput.warning_unavailable_category_number")
#         self.input_instance.input_category_index()
#         assert self.input_instance.category_index == 2
#
#     def test_input_level_valid(self, mocker):
#         # Корректное значение уровня
#         mocker.patch("Output.InfoForInput.level_info", return_value=2)
#         mocker.patch("Utils.Utils.clear_console")
#         self.input_instance.input_level()
#         assert self.input_instance.level_index == 2
#
#     def test_input_level_invalid(self, mocker):
#         # Некорректное значение уровня сначала (0), затем корректное (3)
#         mocker.patch("Output.InfoForInput.level_info", side_effect=[0, 3])
#         mocker.patch("Utils.Utils.clear_console")
#         mocker.patch("Output.InfoForInput.warning_unavailable_level_number")
#         self.input_instance.input_level()
#         assert self.input_instance.level_index == 3
#
#     def test_input_attempts_valid(self, mocker):
#         # Корректное значение попыток
#         mocker.patch("Output.InfoForInput.attempts_info", return_value=5)
#         mocker.patch("Utils.Utils.clear_console")
#         self.input_instance.input_attempts()
#         assert self.input_instance.attempts == 5
#
#     def test_input_attempts_invalid(self, mocker):
#         # Некорректное значение попыток сначала (18), затем корректное (6)
#         mocker.patch("Output.InfoForInput.attempts_info", side_effect=[18, 6])
#         mocker.patch("Utils.Utils.clear_console")
#         mocker.patch("Output.InfoForInput.warning_unavailable_attempts_number")
#         self.input_instance.input_attempts()
#         assert self.input_instance.attempts == 6
