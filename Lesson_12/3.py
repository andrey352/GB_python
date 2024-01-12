# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1

class FactorialGenerator:
    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = args[0]
                self.stop = 1
                self.step = 1
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start <= self.stop:
            res = 1
            for i in range(1, self.start + 1):
                res *= i
            self.start += self.step
            return res
        raise StopIteration
    
    
if __name__ == "__main__":
    f = FactorialGenerator(2, 6, 2)
    for i in f:
        print(i)



















