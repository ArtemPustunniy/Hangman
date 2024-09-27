import os


class Utils:
    """
    Вспомогательный класс, содержащий утилитарные методы для работы с системой.
    """

    @classmethod
    def clear_console(cls) -> None:
        """
        Очищает консоль в зависимости от операционной системы.

        Если ОС Windows, используется команда 'cls', в противном случае — команда 'clear'.
        """
        os.system("cls" if os.name == "nt" else "clear")
