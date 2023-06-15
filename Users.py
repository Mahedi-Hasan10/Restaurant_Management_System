from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        super().__init__()


class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        self.name = name
        self.wallet = money
        self.due_amount = 0
        self.__order = None
        super().__init__(name, phone, email, address)

    @property
    def order(self, order):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.due_amount += order.bill
        print(f"{self.name} place an order with bill {order.bill}")

    def eat_food(self, order):
        print(f"{self.name} eating food {order.items}")

    def pay_for_order(self, amount):
        pass

    def give_tips(self, amount):
        pass

    def write_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, phone, email, address, salery, starting_date, department) -> None:
        self.salery = salery
        self.due = salery
        self.starting_date = starting_date
        self.department = department
        super().__init__(name, phone, email, address)

    def receive_salery(self):
        self.due = 0


class Chef(Employee):
    def __init__(self, name, phone, email, address, salery, starting_date, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salery, starting_date, department)
        self.cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, salery, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salery, starting_date, department)
    tips_earning = 0

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_order(self, order):
        pass

    def take_tips(self, amount):
        self.tips_earning += amount


class Manager(Employee):
    def __init__(self, name, phone, email, address, salery, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salery, starting_date, department)
