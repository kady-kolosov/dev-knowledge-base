# Рассмотрим класс Point, который объединяет несколько возможностей, изученных в предыдущих разделах.
# Из этого примера можно увидеть, как в одном классе используются:
# атрибут класса;
# атрибуты экземпляра;
# метод __init__;
# методы экземпляра;
# вызов одного метода из другого;
# принцип DRY (Don't Repeat Yourself) — не повторяй один и тот же код.
"""
• list_points — атрибут класса, общий для всех экземпляров.
• x и y — атрибуты экземпляра, хранящие координаты конкретной точки.
• __init__() задаёт начальное состояние нового экземпляра и добавляет
  его в общий список.
• Методы работают с экземпляром через параметр self.
• Методы __init__() и go_home() используют move_to(), следуя принципу
  DRY (Don't Repeat Yourself).
"""

from math import sqrt


class Point:
    '''
    Пример класса, объединяющего несколько ранее изученных возможностей.

    Из него можно увидеть, как атрибуты класса, атрибуты экземпляра,
    инициализация и методы работают вместе в одном классе.
    '''
    list_points = []

    def __init__(self, x=0, y=0):
        self.move_to(x, y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Точка с координатами ({self.x}, {self.y})")

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Point")

        return sqrt(
            (self.x - another_point.x) ** 2 +
            (self.y - another_point.y) ** 2
        )

p1 = Point(6, 0)
p1.print_point()

p2 = Point(0, 8)
p2.print_point()

print(p1.calc_distance(p2))
print(p1.calc_distance(10))  # ❌ ValueError: Аргумент должен принадлежать классу Point
