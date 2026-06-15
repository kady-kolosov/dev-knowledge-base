class Employee:
    company = "Google"

    def set_profile(self, name, position):
        self.name = name
        self.position = position

    def get_profile(self):
        print(self.name, self.position)  # Доступ через self к атрибутам экземпляра
        print(self.company)  # Доступ через self к атрибутам класса


emp1 = Employee()
print(emp1.__dict__)  # {}

emp1.set_profile("Arkady", "Developer")
print(emp1.__dict__)  # {'name': 'Arkady', 'position': 'Developer'}

emp1.get_profile()
# Arkady Developer
# Google
Employee.get_profile(emp1)  # Эквивалентно такому вызову emp1.get_profile()
print(type(Employee.test))

# * ------------------------------------------------------------------------------------
