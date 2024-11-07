import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}

    # Определяем тип объекта
    info['type'] = type(obj).__name__

    # Получаем атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]

    # Получаем методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получаем модуль, к которому принадлежит объект, если он есть
    info['module'] = getattr(obj, '__module__', None)

    # Другие интересные свойства
    if hasattr(obj, '__dict__'):
        info['attributes_dict'] = obj.__dict__

    if inspect.isclass(type(obj)):
        info['is_class'] = True
    else:
        info['is_class'] = False

    return info


# Пример класса для тестирования
class Example:
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 = "value2"

    def method1(self):
        return "This is method1"


# Пример использования функции
number_info = introspection_info(42)
pprint(number_info)

