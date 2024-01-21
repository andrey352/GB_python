# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from task2 import clear_text

def test_register_change():
    assert clear_text('привет мир') == 'привет мир'

def test_punktuation_delete():
    assert clear_text("Привет. мир!!!") == 'привет мир'

def test_foreign_alphabets():
    assert clear_text("ПриветHello мир") == 'привет мир'

def test_all_condition():
    assert clear_text("ПриветHello миР123...") == 'привет мир'














