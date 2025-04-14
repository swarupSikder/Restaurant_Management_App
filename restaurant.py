from user import Admin
from menu import Menu
from foodItem import FoodItem

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'{employee.user_name} is added as an Employee')

    def view_employees(self):
        print('\n------------(Employee List)------------')
        print(f'{"Employee":<15}{"Designation":<15}{"Salary":<10}')
        for emp in self.employees:
            print(f'{emp.user_name:<15}{emp.designation:<15}{emp.salary:<10}')

    def add_menu_item(self, restaurant, item):
        self.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        self.menu.remove_item(restaurant, item)

    def show_menu(self, restaurant):
        self.menu.show_menu()