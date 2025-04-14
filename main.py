from user import Admin, Employee, Customer
from restaurant import Restaurant, FoodItem, Menu

restaurant = Restaurant('Demons Cave')
print(f'Restaurant Name: {restaurant.name}')

# Optional Admin (not used in this example, but could be used for authorization logic)
admin = Admin('Khan', '1234', '017')

restaurant.add_menu_item(restaurant, FoodItem('Pizza', 12.45, 10))
restaurant.add_menu_item(restaurant, FoodItem('Burger', 16.75, 13))
# restaurant.show_menu(restaurant)

customer1 = Customer('Khan', '1234')
customer1.view_menu(restaurant)
# customer1.view_cart()
