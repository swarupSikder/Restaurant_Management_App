from abc import ABC
from order import Order

class User(ABC):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password


class Employee(User):
    def __init__(self, user_name, password, designation, salary):
        super().__init__(user_name, password)
        self.designation = designation
        self.salary = salary

# emp = Employee('Khan', '1234', 'Officer', 12000)
# print(emp.salary)

class Admin(User):
    def __init__(self, user_name, password, phone):
        super().__init__(user_name, password)
        self.phone = phone



class Customer(User):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)
        self.cart = Order()

    def __repr__(self):
        return f'Customer: {self.user_name}'

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_item(item)
            print(f'{item_name} is added to your cart')
        else:
            print(f'{item_name} not found')

    def view_cart(self):
        print('-----------view cart-----------')
        print('Item\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {quantity}")

        print("Total Price : {self.cart.total_price}")

