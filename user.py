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

    def add_employee(self, restaurant, employee):
        restaurant.employees.append(employee)
        print(f'{employee.user_name} is added as an Employee')

    def view_employees(self, restaurant):
        print('\n------------(Employee List)------------')
        print(f'{"Employee":<15}{"Designation":<15}{"Salary":<10}')
        for emp in self.employees:
            print(f'{emp.user_name:<15}{emp.designation:<15}{emp.salary:<10}')

    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(restaurant, item_name)

    def show_menu(self, restaurant):
        restaurant.menu.show_menu()


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
            if quantity > item.quantity:
                print('Item qty exceeded!!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print(f'{item_name} is added to your cart')
        else:
            print(f'{item_name} not found')

    def view_cart(self):
        print('\n-----------view cart-----------')
        print('Item\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"Total Price : {self.cart.total_price()}")

    def pay_bill(self):
        print('Paid Successfully!')
        self.cart.clear()

