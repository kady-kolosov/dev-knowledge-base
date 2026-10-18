class Square:

    def __init__(self, side):
        self.__side = side
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"value={value} ❌\nСторона должна принадлежать типу int или float"
            )
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side**2
        return self.__area


sq = Square(10)
print(sq.area)  # вычисляет 100
print(sq.area)  # берёт 100 из кэша

sq.side = 11  # изменяет сторону и сбрасывает кэш
print(sq.area)  # вычисляет 121
print(sq.area)  # берёт 121 из кэша
