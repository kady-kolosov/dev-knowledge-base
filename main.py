class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def __display_private_data(self):
        print(self.__balance)

    def get_private_data(self):
        self.__display_private_data()


id123 = BankAccount(1_567_682.64)

print(id123.__balance)  # ❌ AttributeError
id123.__display_private_data()  # ❌ AttributeError

id123.get_private_data()  # 1567682.64

print(dir(id123))  # ['_BankAccount__balance',
#  '_BankAccount__display_private_data', ...]

print(id123._BankAccount__balance)  # 1567682.64
id123._BankAccount__display_private_data()  # 1567682.64
