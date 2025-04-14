from user import Admin, Employee, Customer
from restaurant import Restaurant, FoodItem, Menu

# print(f'Restaurant Name: {restaurant.name}')
# admin = Admin('Khan', '1234', '017')
# admin.add_menu_item(restaurant, FoodItem('Pizza', 12.45, 10))
# admin.add_menu_item(restaurant, FoodItem('Burger', 16.75, 13))
# customer1 = Customer('Khan', '1234')
# customer1.view_menu(restaurant)

# item_name = input('Enter item Name : ')
# item_qty = int(input('Enter Quantity : '))

# customer1.add_to_cart(restaurant, item_name, item_qty)
# customer1.view_cart()

restaurant = Restaurant('Demons Cave')










def customer_menu():
    name = input('Enter name: ')
    password = input('Enter password: ')
    customer = Customer(name, password)

    while True:
        print(f'\nWelcome {customer.user_name}')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View Cart')
        print('4. Pay Bill')
        print('5. Exit')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            customer.view_menu(restaurant)
        elif choice == 2:
            item_name = input('Enter item name: ')
            item_qty = int(input('Enter item qty: '))
            customer.add_to_cart(restaurant, item_name, item_qty)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break












def admin_menu():
    name = input('Enter name: ')
    password = input('Enter password: ')
    phone = input('Enter phone: ')
    admin = Admin(name, password, phone)

    while True:
        print(f'\nWelcome {admin.user_name}')
        print('1. Add new item')
        print('2. Add new employee')
        print('3. View employee')
        print('4. View items')
        print('5. Delete item')
        print('6. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            item_name = input('Enter item name: ')
            item_price = input('Enter item price: ')
            item_qty = int(input('Enter item qty: '))
            item = FoodItem(item_name, item_price, item_qty)
            admin.add_menu_item(restaurant, item)
        elif choice == 2:
            name = input('Enter name: ')
            password = input('Enter password: ')
            designation = input('Enter designation: ')
            salary = input('Enter salary: ')
            emp = Employee(name, password, designation, salary)
            admin.add_employee(restaurant, emp)
        elif choice == 3:
            admin.view_employees(restaurant)
        elif choice == 4:
            admin.show_menu(restaurant)
        elif choice == 5:
            item_name = input('Enter Item Name: ')
            admin.remove_item(restaurant, item_name)
        elif choice == 6:
            break
        else:
            print('Invalid Choice')








while True:
    print('------------Welcome----------')
    print('1. Customer Menu')
    print('2. Admin Menu')
    print('3. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print('Invalid choice')
