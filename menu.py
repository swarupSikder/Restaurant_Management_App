class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name:
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'{item_name} is removed')
        else:
            print(f'{item_name} is not found')

    def show_menu(self):
        print("\n-------------Menu-------------")
        print(f"{'Item':<15}{'Price':<10}{'Quantity'}")
        for item in self.items:
            print(f"{item.name:<15}{item.price:<10}{item.quantity}")