from Menu import Pizza, Burger, Drink, Menu
from Restaurant import Resturant
from Users import Employee, Chef, Server, Manager, Customer
from Order import Order


def main():
    menu = Menu()
    # add pizza to the menu
    pizza_1 = Pizza("Shutki Pizza", 600, 'large', ["Shutki", "Moida"])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza("Korola Pizza", 1200, "Xtra large",
                    ["Korola", "Onion", "Oil"])
    menu.add_menu_item("pizza", pizza_2)
    pizza_3 = Pizza("Alu Pizza", 1500, "XXL", ["Alu", "Onion", "Chilli"])
    menu.add_menu_item("pizza", pizza_3)

    # add burger to the menu
    burger1 = Burger("Naga Burger", 700, "Chicken", ["Chicken", "Cheese"])
    menu.add_menu_item("burger", burger1)
    burger2 = Burger("Chicken Burger", 250, "Beef", ["Beef", "oil"])
    menu.add_menu_item("burger", burger2)

    # add drinks to the menu
    coke = Drink("Cocacola", 50, True)
    menu.add_menu_item("drink", coke)
    coffee = Drink("Coffee", 200, False)
    menu.add_menu_item("drink", coffee)
    menu.show_menu()

    # add employee
    resturant = Resturant("Kopa samsu restaurant", 3000, Menu)
    manager = Manager("Kopa Manager", 420, "kopa@mail.com",
                      "kopapur", 1500, "1 Feb 2020", 'core')
    resturant.add_employee('manager', manager)
    chef = Chef("Chefu", 425, "sefu@mail.com", "kopapur",
                3500, "1 Feb 2020", 'chef', 'everything')
    resturant.add_employee('chef', chef)
    server = Server("Hablu", 430, "hablu@mail.com",
                    "Kaliapur", 200, "5 March 2021", 'server')
    resturant.add_employee('server', server)
    # show employee
    resturant.show_employee()

    # customer1 place ing an order
    customer_1 = Customer("Sakib Khan", 232, "sakib@khan", "Bonani", 100000)
    order_1 = Order(customer_1, [burger2, pizza_3,
                    pizza_3, pizza_3, pizza_3, pizza_3])
    customer_1.place_order(order_1)
    resturant.add_order(order_1)

    resturant.receive_payment(order_1, 20000, customer_1)
    print(
        f"Revenue : {resturant.revenue}, Balance : {resturant.balance} after first customer")

    resturant.pay_expense(resturant.rent, "Rent")
    resturant.pay_salery(chef)
    print(
        f"after paying salery : Revenue : {resturant.revenue} Balance : {resturant.balance} Expense : {resturant.expense}")


if __name__ == '__main__':
    main()
