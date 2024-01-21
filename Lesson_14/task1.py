# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters, punctuation

INCORRECT_SYMBOLS = ascii_letters + punctuation + "0123456789"


def clear_text(text: str,) -> str:
    """
    Удаляет лишние символы из строки с кириллицей
    """
    return "".join([symbol for symbol in text if symbol not in INCORRECT_SYMBOLS]).lower()


if __name__ == "__main__":
    print(clear_text("DFGФЫВ123"))


