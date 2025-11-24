# Creating an app for a cafe in python

#Just simple menu for a cafe using basics of python.

# Used Class, defined functions, and wrote code to create a user interactive menu

# creating necessary class
class Tea:
    
    # initialize Tea with name and price

    def __init__(self, name, price):

        self.name = name

        self.price = price

class Order:

    # Initializing the the required options

    def __init__(self):

        self.items = []

    # adding menu to order 
    
    def add_items(self, tea):
        self.items.append(tea)

        print(f"Added {tea.name} to your order.")

    # calculating the total bill
    def total(self):
        return sum(item.price for item in self.items)
    
    # showing the order summary
    
    def show_order(self):
        if not self.items:
            print("No items in the order")
            return
        print("\nYour Order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}.{item.name} - $ {item.price}")
        print(f"total: ${self.total()}\n")

    # defining checkout

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        
        self.show_order()
    
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':

            print("Order confirmed! Thank You.")
            self.items.clear()

        else :
            print('Checkout Cancelled.')

# Now displaying the menu and function to handle user input

def main():

    menu = [
        
        Tea("Tea", 10),

        Tea("Masala Tea", 15),

        Tea("Ginger Tea", 12),

        Tea("Lemon Tea", 15),

        Tea("Black Tea", 8),

        Tea("Green Tea", 20),

        Tea("Biscuits", 5)

    ]
    
    order = Order()

    # User internaction

    while True:
        print("\n--- Menu Card ---")

        for i, tea in enumerate(menu, 1):

            print(f"{i}. {tea.name} - ${tea.price}")
        print("8. View Order")

        print("9. Checkout")

        print("10. Exit")

        choice =  input("Choose an option: ")

        if choice in ['1','2','3','4','5','6','7']:
            order.add_items(menu[int(choice) - 1])
        elif choice == '8':
            order.show_order()
        elif choice == '9':
            order.checkout()
        elif choice == '10':
            print("Thanks for visiting. Goodbye!")
            break
        else :
            print("invalid option")

if __name__ == "__main__":
    main()