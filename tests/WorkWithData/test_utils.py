from src.WorkWithData.Utils import Utils


class TestUtils:
    def test_get_random_key(self):
        test_dict = {"a": 1, "b": 2, "c": 3}
        key = Utils.get_random_key(test_dict)
        assert key in test_dict.keys()

    def test_get_random_category(self):
        category = Utils.get_random_category()
        assert category in [0, 1, 2]
