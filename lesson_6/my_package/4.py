
def puzzle_game(
        puzzle: str,
        puzzle_answers: set[str],
        attempts: int
    ) -> int:
    print(puzzle)
    for attempt in range(attempts):
        user_answer = input('input your answer: ')
        if user_answer in puzzle_answers:
            return attempt + 1
    return 0


def __demo_game():
    """
    Добавьте в модуль с загадками функцию, которая хранит словарь списков.
    Ключ словаря - загадка, значение - список с отгадками.
    Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки
    """
    puzzles ={
        'зимой и летом одним цветом': {'ель', 'ёлка', 'сосна'},
        'не лает не кусает в дом не пускает': {'замок'},
        'сидит дед во сто шуб одет': {'лук', 'луковица'},
    }

    for p, ans in puzzles.items():
        puzzle_game(p, ans, 3)



if __name__ == '__main__':
    __demo_game()
    






