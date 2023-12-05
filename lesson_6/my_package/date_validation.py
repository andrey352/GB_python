
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ["is_date_valid"]

__DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def is_date_valid(date: str) -> bool:
    day, month, year = [int(i) for i in date.split('.')]
    return 1 <= year <= 9999 and 1 <= month <= 12 and __day_valid(day, month, year)

def __day_valid(day, month, year) -> bool:
    if __is_leap_year(year) and month == 2:
        return 1 <= day <= 29
    return 1 <= day <= __DAYS_IN_MONTH[month]

def __is_leap_year(year) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == '__main__':
    print(is_date_valid("29.02.2023"))





