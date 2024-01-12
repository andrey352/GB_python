# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def my_get(dict_: dict, key_, default=None):
    try:
        return dict_[key_]
    except KeyError:
        return default
    
if __name__ == '__main__':
    test_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    print(my_get(test_dict, 'a'))
    print(my_get(test_dict, 'd'))
    print(my_get(test_dict, 'd', 4))

