class Person:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.__address = address

    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary

print(p1.salary)
print(p2.salary)

p1.salary = 72000
p2.salary = 85000

print(p1.salary)
print(p2.salary)

print(p1.get_salary())
print(p2.get_salary())

p1.set_salary(72000)
p2.set_salary(85000)

print(p1.get_salary())
print(p2.get_salary())