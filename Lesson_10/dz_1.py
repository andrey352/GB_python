# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal 
# и добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает
# категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
# Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
# В противном случае, рыба относится к категории "Средневодная рыба".
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию
# млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, 
# то он относится к категории "Малявка".
# Если вес объекта больше 200, то он относится к категории "Гигант".
# В противном случае, объект относится к категории "Обычный".

# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов 
# на основе переданного типа и параметров. Класс-фабрика должен иметь метод create_animal,
# который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для конкретного типа животного. 
# Количество и типы аргументов могут различаться в зависимости от типа животного.
# Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.
# Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError
# с сообщением 'Недопустимый тип животного'

class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        pass


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def make_noise(self):
        return f'mooo'
    
    def category(self):
        if self.weight < 1:
            return f'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return f'Обычный'
    

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name) 
        self.wingspan = wingspan

    def make_noise(self):
        return f'Twit'

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name) 
        self.max_depth= max_depth

    def make_noise(self):
        return None
    
    def depth(self):
        if self.max_depth < 10:
            return f'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'

class AnimalFactory:

    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type not in ['Bird', 'Fish', 'Mammal']:
            raise NameError('Недопустимый тип животного')
        else:
            i = f"{animal_type}('{args[0]}', {args[1]})"
            print(i)
            return i
        
if __name__ == '__main__':
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    print(animal1.wing_length())
 







































