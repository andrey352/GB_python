
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    При создании нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков-архивов
    list-архивы также являются свойствами экземпляра
    """
    instance = None

    def __new__(cls, text, number):
        if cls.instance is None:
            cls.instance = super().__new__(cls)                 # наследуемся от класса object
            cls.instance.old_text = []
            cls.instance.old_num = []
        else:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_num.append(cls.instance.number)
        return cls.instance
    
    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __repr__(self):
        return f"Archive({self.text = } {self.number = })"
    
    def __str__(self):
        return f"{a1.old_text} {self.old_num} | {self.text} {self.number}"
    

if __name__ == '__main__':
    a1 = Archive('fakf', 12)
    print(a1.old_text, a1.old_num)
    a2 = Archive('ccc', 777)
    print(a2.old_text, a2.old_num)
    print(a1, a2)                        # класс str вызывается по умолчанию
    # print(repr(a1), repr(a2))             # если есть класс str, то repr нужно вызывать явно





















