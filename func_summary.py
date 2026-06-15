# ✅ ок:
# ❌ ErrorName:

# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
#! АННОТАЦИИ ТИПОВ И ДОКСТРОКА
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────

from functools import wraps

example_var1: int = 123
example_var2: set = (1, 2, 3)


def count_letters(word_1: str, word_2: str) -> int:
    """
    Сначала идёт пояснение функции,
    потом описываются аргументы,
    а потом то, что функция возвращает.
    """
    return len(word_1) + len(word_2)


print(count_letters.__doc__)
print(count_letters.__annotations__)
# ────────────────────────────────────────────────────────────────────
#! АННОТАЦИИ ПРИ ПОМОЩИ МОДУЛЯ typing В СТАРЫХ ВЕРСИЯХ < 3.9
#! И НОВЫХ ВЕРСИЯХ >= 3.9 БЕЗ МОДУЛЯ typing
# Встроенный модуль typing позволяет создавать аннотации в более сложных случаях,
# например, если вы хотите проаннотировать переменную сразу несколькими типами или
# указать аннотацию для элементов коллекции.

#! Аннотация списка и множества (в старых версиях < 3.9)
numbers: List[float] = [1.1, 3.0, 4.5]
letters: Set[str] = set("hello")

#! Аннотация списка и множества (в новых версиях >= 3.9)
numbers: list[float] = [1.1, 3.0, 4.5]
letters: set[str] = set("hello")

#! Объект Union (в старых версиях < 3.9)
# C помощью объекта Union можно указывать сразу несколько типов данных, которые
# могут быть сохранены в переменную.


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


print(add_numbers.__annotations__)
# {'a': typing.Union[int, float], 'b': typing.Union[int, float], 'return': typing.Union[int, float]}
print(add_numbers(10, 25.7))  # 35.7

#! Объект Union (в новых версиях >= 3.9)


def add_numbers(a: int | float | str, b: int | float | str) -> int | float | str:
    return a + b


print(add_numbers.__annotations__)
# {'a': int | float | str, 'b': int | float | str, 'return': int | float | str}
print(add_numbers(10, 25.7))  # 35.7

#! Объект Optional (в старых версиях < 3.9)
# Optional, специально создан для аннотирования указанного типа и значения None.

# Переменная num из примера выше может теперь хранить в себе целые числа и также
# значение None.
# Инструкция Optional[int] эквивалента записи Union[None, int]
num: Optional[int] = None
# Инструкция Optional[str] эквивалента записи Union[None, str].
# Переменная word проаннотирована строковым типом и еще пустым значением None.
word: Optional[str] = None

#! Объект Optional (в новых версиях >= 3.9)
num: int | None = None
word: str | None = None

#! Объект Any (в старых версиях < 3.9)
# Например, вы хотите указать при помощи аннотаций, что в переменной можно
# сохранить любой тип данных.
example_var: Any = 123
# В принципе, мы можем добавить совершенно любой тип данных в список, поэтому
# лучше проаннотировать данный параметр объектом Any и заодно указать, что
# функция возвращает список из любых элементов.


def append_to_list(value: Any, my_list: Optional[list] = None) -> List[Any]:
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


#! Аннотация кортежа (в старых версиях < 3.9)
# Ранее, мы аннотировали элементы списка:
numbers: List[float] = [1.1, 3.0, 4.5]
# Тут мы указали тип float для всех элементов списка. С кортежами такая схема не
# пройдет, потому что они, в отличие от списков, часто используются для
# разнотипных элементов.

# Для кортежа в квадратных скобках нужно указывать тип каждого элемента
# по отдельности
words: Tuple[str, int] = ("hello", 300)

# Если же планируется использовать кортеж аналогично списку: хранить
# неизвестное количество однотипных элементов, можно воспользоваться многоточием.
words: Tuple[str, ...] = ("hello", "world", "abc")

#! Аннотация кортежа (в новых версиях >= 3.9)
words: tuple[str, int] = ("hello", 300)
words: tuple[str, ...] = ("hello", "world", "abc")

#! Аннотация словарей (в старых версиях < 3.9)
# Для аннотации словарей нужно указать тип ключа и тип значения следующим образом:
person: Dict[str, str] = {"first_name": "John", "last_name": "Doe"}

#! Аннотация словарей (в новых версиях >= 3.9)
person: dict[str, str] = {"first_name": "John", "last_name": "Doe"}

# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
#! ФУНКЦИИ - ОБЪЕКТЫ ПЕРВОГО КЛАССА
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────

# * Объектом первого класса:
# * С ним можно работать как с переменными
# * Он может быть передан в функцию как аргумент
# * Он может быть возвращен из функции как результат
# * Он может быть включен в другие структуры данных

# int, str, list, tuple, dict, set и т.д. являются примером
# объекта первого класса.

#! Функции можно сохранять в переменные
# Функция представляет собой такой же объект, как и строка или список.
# Поэтому как и любой другой объект её можно присвоить переменной.


prt = print
prt("Hello World")

#! Функции можно передавать аргументом другим функциям


def say_upper(text):
    return text.upper() + "!"


def speak(func):
    return func("Меж нами памяти туман, ты как во сне")


print(speak(say_upper))
# МЕЖ НАМИ ПАМЯТИ ТУМАН, ТЫ КАК ВО СНЕ!

# Что, если мы хотим написать код для поиска максимального по модулю элемента
# списка numbers? И вообще, сравнивать элементы не стандартным способом, а более
# специфическими?

# На этот случай встроенные функции min(), max(), sorted() могут принимать
# необязательный аргумент key – функцию, определяющую условия сравнения элементов.
# Функция, определяющая условия сравнения элементов, называется компаратор.

# Например:
numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(min(numbers, key=abs))  # -7
print(max(numbers, key=abs))  # -210
print(sorted(numbers, key=abs))  # [-7, 8, 10, 32, -50, 87, -100, 117, -210]
print(sorted(numbers, key=lambda x: x % 10))
# отсортировали по последней цифре числа
# [10, -100, -50, -210, 32, -7, 87, 117, 8]

# Рассмотрим еще один пример. Пусть в списке points хранятся в виде кортежей
# координаты точек плоскости в двумерной биполярной системе координат.
points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

# При использовании встроенной функции sorted() (или списочного
# метода sort()) сортировка пройдет по первым значениям пар кортежа,
# а в случае их совпадения – по вторым.
points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

points.sort()

print(points)
# [(-10, 15), (1, -1), (1, 5), (2, -4), (2, 3), (7, 18), (10, 9)]

# Рассмотрим следующий код:


def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))
# сортируем по второму значению кортежа
# [(2, -4), (1, -1), (2, 3), (1, 5), (10, 9), (-10, 15), (7, 18)]
print(sorted(points, key=compare_by_sum))
# сортируем по сумме кортежа
# [(2, -4), (1, -1), (2, 3), (-10, 15), (1, 5), (10, 9), (7, 18)]

#! Функции могут возвращать другие функции


def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a * x**2 + b * x + c

    return square_polynom


example1 = generator_square_polynom(a=1, b=2, c=1)
example2 = generator_square_polynom(a=2, b=0, c=-3)
example3 = generator_square_polynom(a=-3, b=-10, c=50)

print(example1(1))
print(example2(2))
print(example3(-1))

# Обратите внимание на то, что внутренняя функция square_polynom() использует
# параметры внешней функции generator_square_polynom(). Такую вложенную функцию
# называют замыканием.

# Вот еще пример:


def get_math_func(operation="+"):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == "+":
        return add
    elif operation == "-":
        return subtract


sign = input("Введите '+' для сложения или '-' для вычитания: ")
math_func = get_math_func(sign)
print(math_func(5, 3))

# Или можно сразу использовать двойной вызов
print(get_math_func("+")(3, 4))
print(get_math_func("-")(3, 4))

#! Функции могут храниться в структурах данных


def say_louder(text):
    return text.upper() + "!"


funcs = [sum, say_louder]

print(funcs[0]([1, 2, 3]))  # 6
print(funcs[1]("Example text"))  # EXAMPLE TEXT!

# Еще пример:


def calculate(x: int, y: int, operation="a") -> None:

    def division() -> int | float:
        try:
            return x / y
        except ZeroDivisionError:
            return "На ноль делить нельзя!"

    my_dict = {
        "a": lambda: x + y,
        "s": lambda: x - y,
        "d": division,
        "m": lambda: x * y,
    }

    try:
        print(my_dict[operation]())
    except:
        print("Ошибка. Данной операции не существует!")


# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
#! Интроспекция - способность определять тип объекта во время выполнения
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────


def test():
    pass


# Создание атрибута
test.name_attr = "val_attr"
# Создание атрибута через функцию setattr
setattr(test, "name_attr", "val_attr")

# Обращение к атрибуту
print(test.name_attr)  # val_attr
# Обращение к атрибуту через функцию getattr
print(getattr(test, "name_attr"))  # val_attr

# Проверка наличия атрибута через функцию hasattr
print(hasattr(test, "name_attr"))  # True
print(hasattr(test, "abcde"))  # False

# Функция dir - возвращает список допустимых атрибутов и методов для этого
# объекта
print(dir(test))
# ['__annotations__', '__builtins__', ... '__type_params__', 'name_attr']
print(dir(list))  # ['__add__', '__class__', ... 'remove', 'reverse', 'sort']

#! Атрибут __name__
print(test.__name__)  # test
print(list.__name__)  # list

#! Атрибут __defaults__
# __defaults__ - представляет собой кортеж, содержащий значения параметров по
# умолчанию, если таких нет, то возвращает None


def test(a: int = 123, b: str = "abc") -> tuple[int, str]:
    pass


print(test.__defaults__)  # (123, 'abc')

#! Атрибут __kwdefaults__
# __kwdefaults__ представляет собой словарь, содержащий значения Keyword-only


def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
    pass


print(my_func.__kwdefaults__)  # {'kw2': 4}

#! Атрибут __code__
# Хранит в себе информацию об объекте


def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
    pass


print(my_func.__code__)  # <code object my_func at 0x1048d1480 ...

# У этого объекта code можно также взглянуть на состав атрибутов при помощи
# функции dir. В конце списка есть ряд атрибутов, например co_varnames
print(dir(my_func.__code__))
# ['__class__', '__delattr__', ... 'co_varnames']
print(my_func.__code__.co_varnames)  # ('a', 'b', 'c', 'kw1', 'kw2', 'kwargs')

# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
#! ДЕКОРАТОРЫ
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────

# Декоратор — это функция, которая позволяет обогатить любую другую функцию
# дополнительным поведением без необходимости изменения ее кода


def header_decorator(func):

    def inner(*args, **kwargs):
        print("<header>")
        func(*args, **kwargs)
        print("</header>")

    return inner


def ul_li_decorator(func):

    def inner(*args, **kwargs):
        print("<ul>")
        print("<li>")
        func(*args, **kwargs)
        print("</li>")
        print("</ul>")

    return inner


@header_decorator
def text(surename, name):
    print(f"\tHello {surename} {name}")


text("Kolosov", "Arkady")

# * @header_decorator работает вот так:
# * text = header_decorator(text)
# * text('Kolosov', 'Arkady')


@header_decorator
@ul_li_decorator
def text(surename, name):
    print(f"\tHello {surename} {name}")


text("Kolosov", "Arkady")

# * @header_decorator + @ul_li_decorator работают вот так:
# * text = header_decorator(ul_li_decorator(text))
# * text('Kolosov', 'Arkady')

# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
#! ДЕКОРАТОР С ПАРАМЕТРОМ ИЛИ ФАБРИКА ДЕКОРАТОРОВ
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────


def html_tag(func, name_tag="h1"):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<{name_tag}>{result}</{name_tag}>"

    return inner


@html_tag(name_tag="table")  # TypeError: html_tag() missing 1 required...
# Нельзя в функции-декораторе определить дополнительные параметры
def text(surename, name):
    return f"Hello {surename} {name}"


text = html_tag(text, name_tag="asdasd")  # можно без синтаксического сахара

print(text("Kolosov", "Arkady"))

# Когда мы используем синтаксический сахар через @, python передает декоратору
# единственный аргумент: функцию, которую мы декорируем, и ничего больше.

#! Как решить проблему?


def decorator_factory():
    print("Запуск функции создания декоратора")

    def decorator(fn):
        print("Запуск декоратора")

        def wrapper(*args, **kwargs):
            print("Запуск функции wrapper")
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@decorator_factory()
def original_func():
    print("Запуск оригинальной функции")


original_func()

# Если не пользоваться синтаксическим сахаром, то строчки равнозначны следующим


def original_func():
    print("Запуск оригинальной функции")


decorator = decorator_factory()  # получаем декоратор из decorator_factory
original_func = decorator(original_func)  # декорируем

# или так
original_func = decorator_factory()(original_func)

# теперь можно передавать аргументы, вот пример


def decorator_factory(a, b):
    print("Запуск функции создания декоратора")

    def decorator(fn):
        print("Запуск декоратора")
        wraps(fn)

        def wrapper(*args, **kwargs):
            print("Запуск функции wrapper")
            print("Переданные переменные: ", a, b)
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@decorator_factory(10, 20)
def original_func():
    print("Запуск оригинальной функции")


original_func = decorator_factory(1, 2)(original_func)

original_func()

#! Возвращаемся к решению проблемы


def html_tag(name_tag="h1"):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{name_tag}>{result}</{name_tag}>"

        return inner

    return decorator


@html_tag(name_tag="span")
def text(surename, name):
    return f"Hello {surename} {name}"


print(text("Kolosov", "Arkady"))
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────
