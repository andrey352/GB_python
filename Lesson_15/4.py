# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату
import datetime

WEEKDAYS = {
    "понедельник": 0,
    "вторник": 1,
    "среда": 2,
    "четверг": 3,
    "пятница": 4,
    "суббота": 5,
    "воскресенье": 6
}

MONTHS = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12
}

def correct_date(text: str) -> datetime.datetime:
    week_count, weekday, month = text.split()
    week_count = int(week_count[0])
    weekday = WEEKDAYS[weekday]
    month = MONTHS[month]

    week_passed = 0
    for day in range(1, 31):
        temp_date = datetime.datetime(datetime.datetime.now().year, month, day)
        if temp_date.weekday() == weekday:
            week_passed += 1
            if week_passed == week_count:
                return temp_date
    raise ValueError(f"Такой даты не существует: '{text}'")

if __name__ == "__main__":
    print(correct_date('1-й четверг ноября'))
    print(correct_date('3-я среда мая'))






















