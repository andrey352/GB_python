# Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номерпопытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение

__all__ = ['puzzle_game', 'show_result']


_result = {}

def puzzle_game(
        puzzle: str,
        puzzle_answers: set[str],
        attempts: int
    ) -> int:
    print(puzzle)
    for attempt in range(attempts):
        user_answer = input('input your answer: ')
        if user_answer in puzzle_answers:
            res = attempt + 1
            break
    else:
        res = 0
    __save_results(puzzle=puzzle, attempts=res)
    return res


def __demo_game():
    puzzles ={
        'зимой и летом одним цветом': {'ель', 'ёлка', 'сосна'},
        'не лает не кусает в дом не пускает': {'замок'},
        'сидит дед во сто шуб одет': {'лук', 'луковица'},
    }

    for p, ans in puzzles.items():
        puzzle_game(p, ans, 3)


def __save_results(puzzle: str, attempts: int):
    # global _result
    _result[puzzle] = attempts

def show_result():
    for k, v in _result.items():
        print(k, v)



if __name__ == '__main__':
    __demo_game()
    show_result()

    






