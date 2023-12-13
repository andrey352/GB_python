# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки

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


if __name__ == '__main__':
    fish = Fish('Bob', 56)
    cow = Mammal('Zorka', 257)
    bird = Bird('Josh', 0.5)
    for each in [fish, cow, bird]:
        print(f'{each.name} says {each.make_noise()}')
    print(fish.depth())
    print(cow.category())
    print(bird.wing_length())



















