##Exercise 1 - Turn the shopping cart program from yesterday into 
# an object-oriented program
class cart():
    def __init__(self):
    
        def add(self,item):
            self.add(item)
            print(f"{item} was added to your cart")

        def remove(self,item):
            self.remove(item)
            print(f"{item} was removed from your cart")

        def show(self,item):
            print("Your cart contains: ")
            for items in cart:
                print(item)
                
def cart_ui():
    shopping = cart() 
    while True:
        response= input("What would you like to do? You can: quit/ add/ remove/ \
or show item(s). Only type one at a time.")
        
        if response.lower()== "quit":
            shopping.show()
            print("Thanks for shopping")
            break

        elif response.lower()== 'add':
            item = input("What would you like to add to your cart? ")
            shopping.add()
            
        elif response.lower()== 'remove':
            item = input("What would you like to remove from your cart? ")
            shopping.remove()
            
        elif response.lower()== 'show':
            shopping.show()

        else:
            print("Please try again ")
            

cart_ui()

###Exercise 2 - Write a Python class which has two methods get_String 
# and print_String. get_String accept a string from the user 
# and print_String print the string in upper case

class My_String():
    def __init__(self):
        self.str1 = print("What's Your Name?")

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(f"{self.str1.upper()} Ok. Please stop yelling")

str1 = My_String()
str1.get_String()
str1.print_String()
