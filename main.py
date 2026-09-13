class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        print("Вызван метод balance (геттер)")
        print(f"Баланс: {self.__balance}")
        return self.__balance

    @balance.setter
    def balance(self, value):
        print("Вызван метод balance (сеттер)")
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"❌ value={value}\nБаланс должен принадлежать типу int или float"
            )
        self.__balance = value

    @balance.deleter
    def balance(self):
        print("Вызван метод balance (делитер)")
        self.__balance = 0


id123 = BankAccount("Arkady", 1_567_682.64)
id123.balance  # Вызван метод balance (геттер)
# Баланс: 1567682.64

id123.balance = 2_892_788.58  # Вызван метод balance (сеттер)
id123.balance  # Вызван метод balance (геттер)
# Баланс: 2892788.58

del id123.balance  # Вызван метод balance (делитер)
id123.balance  # Вызван метод balance (геттер)
# Баланс: 0
