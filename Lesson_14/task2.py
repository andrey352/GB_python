# Напишите для задачи 1 тесты doctest. Проверьтеследующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потерисимволов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов(кроме п. 1)


from string import ascii_letters, punctuation

INCORRECT_SYMBOLS = ascii_letters + punctuation + "0123456789"

def clear_text(text: str,) -> str:
    """
    Удаляет лишние символы из строки с кириллицей

    >>> clear_text("Привет мир")      
    'привет мир'

    >>> clear_text("Привет миР") 
    'привет мир'

    >>> clear_text("Привет. мир!!!") 
    'привет мир'

    >>> clear_text("ПриветHello мир") 
    'привет мир'

    >>> clear_text("ПриветHello миР123...") 
    'привет мир'
    """
    return "".join([symbol for symbol in text if symbol not in INCORRECT_SYMBOLS]).lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)        # verbose - если Тру то вывод будет подробный






