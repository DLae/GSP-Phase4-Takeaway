--------------------------------
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

Fair warning: if you push your Twilio API Key to a public GitHub repository, anyone will be able to see and use it. What are the security implications of that? How will you keep that information out of your repository?

--------------------------------
from random import randint
class Menu:
    def init(self):
        self.menu = {item : price}
    
    def view_menu(self):
        returns menu

class Place_Order:
    def _init(self):
        customer order list
        total price variable

    def add_item(self, item, amount):
        get instance of menu so can check if item exists

        adds amount of item to customer order
        adds price to total for later
        could do this in a for loop based on amount
        of any item user asks
        (can raise errors after)

    
    def receipt(self):
        formatted order dictionary so can find out how many times an item is added
        
        for loop to go through the order list to count times same item appears
        adds the name of the item and amount of times it appears

        can write all of the information to a file so it looks nicer
        if this is the case test for this will have to be different
        (testing to see if the file is created first)

--------------------------------
def test_menu_is_dictionary():
    menu = Menu()
    assert menu.view_menu() is dictionary

def check_if_item_not_in_menu():
    item = Place_Order()
    with pytest.raises(Exception) as e:
        item.add_item("Ice cream")
    assert str(e.value) == "Item not in menu."