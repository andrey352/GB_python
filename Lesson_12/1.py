# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов

class Factorial:


    def __init__(self, k):
        self.k = k
        self.memoize = []

    def __call__(self, n):
        start = 1
        for i in range (1, n+1):
            start *= i
        self.log(start)
        return start
    
    def log(self, res):
        if len(self.memoize) == self.k:
            self.memoize.pop(0)
        self.memoize.append(res)
    

if __name__ == "__main__":
    f = Factorial(3)
    for i in range(2, 6):
        print(f'{f(i) = }, {f.memoize = }')

