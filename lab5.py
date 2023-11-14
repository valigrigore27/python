import math


#
# # # EX1
# class Shape:
#     def calculate_area(self):
#         pass
#
#     def calculate_perimeter(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#
#     def calculate_area(self):
#         return self.length * self.length
#
#     def calculate_perimeter(self):
#         return self.length * 4
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)
#
#
# square = Square(5)
# square.__init__(5)
# print(square.calculate_perimeter())
# print(square.calculate_area())
# -------------------------------------------------------------------

# class Account:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ${amount}.")
#
#     def withdrawal(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}.")
#         else:
#             print("Insufficient funds!")
#
#     def interest_calculation(self):
#         pass
#
#
# class SavingsAccount(Account):
#     def __init__(self, balance=0, interest_rate=0.02):
#         super().__init__(balance)
#         self.interest_rate = interest_rate
#
#     def interest_calculation(self):
#         interest = self.balance * self.interest_rate
#         self.deposit(interest)
#         print(f"Interest calculated: ${interest}")
#
#
# class CheckingAccount(Account):
#     def __init__(self, balance=0, overdraft_limit=100):
#         super().__init__(balance)
#         self.overdraft_limit = overdraft_limit
#
#     def withdrawal(self, amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#             print(f"Withdrew ${amount}.")
#         else:
#             print("Exceeded overdraft limit!")
#

# savings_account = SavingsAccount(balance=1000)
# savings_account.deposit(500)
# savings_account.withdrawal(200)
# savings_account.interest_calculation()

# checking_account = CheckingAccount(balance=500)
# checking_account.deposit(300)
# checking_account.withdrawal(900)

# --------------------------------------------------------------------

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def mileage(self):
        pass

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def mileage(self):
        mileage = 25
        print(mileage)

    def display_info(self):
        super().display_info()
        print(self.num_doors)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def mileage(self):
        mileage = 50
        print(mileage)

    def display_info(self):
        super().display_info()
        print(self.num_wheels)


class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def towing_capacity(self):
        print(self.cargo_capacity)

    def display_info(self):
        super().display_info()
        print(self.cargo_capacity)



car = Car(make="Toyota", model="Camry", year=2022, num_doors=4)
car.display_info()
car.mileage()
