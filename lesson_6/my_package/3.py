# 3

# Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

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


if __name__ == '__main__':
    print(puzzle_game('зимой и летом одним цветом', 
                      {'ель', 'елка', 'ёлка'}, 2))
    






