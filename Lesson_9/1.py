# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток

def game(puzzle, attempts) -> None:
    def guessing() -> None:
        for i in range(attempts):
            answer = int(input(f'guess the number, you have {attempts - i} attempts: '))
            if answer == puzzle: 
                print(f'you have guessed')
                return True
            elif answer > puzzle:
                print('guess number is less')
            else:
                print('guess number is more')
        return False
    return guessing

if __name__ == '__main__':
    game(5, 3)()





















