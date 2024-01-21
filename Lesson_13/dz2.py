# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, 
# когда текст не является строкой или является пустой строкой.
# Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'
# И InvalidNumberError, которое будет вызываться, если число не является положительным
# целым числом или числом с плавающей запятой.
# Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'
from typing import Union

class InvalidTextError(ValueError):
    pass

class InvalidNumberError(ValueError):
    pass

class Archive:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or text == '':
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")
        self.text = text
        if not isinstance(number, Union[int, float]) or number < 0:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'



r = Archive('asd', 4)
print(r)
r2 = Archive('zzz', 12)
print(r2)








