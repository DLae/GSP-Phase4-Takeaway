from random import randint

class Menu:
    def __init__(self):
        self.menu = {}
    
    def view_menu(self):
        return self.menu

class Place_Order:
    def __init__(self):
        self.customer_order = []
        self.total = 0

    def add_item(self, item, amount):
        menu_instance = Menu()
        
        if item in menu_instance.menu:
            price = menu_instance.menu[item]
            for i in range(amount):
                self.customer_order.append(item)
                self.total += price
        else:
            raise Exception("Item is not on menu.")
    
    def receipt(self):
        order_format = {}
        for item in self.customer_order:
            if item in order_format:
                order_format[item] += 1
            else:
                order_format[item] = 1

        with open ("Receipt.txt", "w") as receipt:
            receipt.write("Bossman's Kebab Korner\n")
            receipt.write(f"Order {randint(0,100)}\n\n")
            for item, amount in order_format.items():
                receipt.write(f"{amount}x {item}\n")
            receipt.write(f"\nTotal: {round(self.total, 2)}")