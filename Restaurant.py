class Resturant:
    def __init__(self, name, rent, menu=[]):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.orders = []
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.profit = 0
        self.balance = 0
        self.expense = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'server':
            self.server = employee
        elif employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'manager':
            self.manager = employee

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount-order.bill
        else:
            print("Not enough money!! pay more!!")

    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f"expense {amount} pay for {description}")
        else:
            print("Not enough money for expense {amount}")

    def add_order(self, order):
        self.orders.append(order)

    def pay_salery(self, employee):
        if employee.salery < self.balance:
            print(f'{employee.name} salery : {employee.salery}')
            self.balance -= employee.salery
            self.expense += employee.salery
            employee.receive_salery()

    def show_employee(self):
        print("-------------Employee List----------------")
        if self.manager is not None:
            print(
                f"Manager : {self.manager.name} is with salery : {self.manager.salery}")
        if self.chef is not None:
            print(
                f"Chef : {self.chef.name} is with salery : {self.chef.salery}")
        if self.server is not None:
            print(
                f"Server : {self.server.name} is with salery : {self.server.salery}")
