# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def correct_input():
    while True:
        try:
            num = input()
            if '.' in num:
                return float(num)
            return int(num)
        except ValueError:                                 # Exception будет ловить все попытки
            continue


if __name__ == '__main__':
    print(correct_input())

