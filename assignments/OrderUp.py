class DinerOrder:
    tax_rate = 0.07

    def __init__(self):
        self.menu = {
            "drinks": {"Water": 0, "Soda": 2.00, "Coffee": 3.00, "Juice": 2.50},
            "appetizers": {"Fries": 3.00, "Salad": 4.00, "Chicken Nuggets": 4.00},
            "main_courses": {"Burger": 8.00, "Steak": 15.00, "Chicken Sandwich": 9.00, "Pizza": 11.00},
            "sides": {"Mashed Potatoes": 2.50, "Vegetables": 2.50, "Rice": 2.00, "Soup": 3.00},
            "desserts": {"Ice Cream": 4.00, "Cake": 5.00, "Float": 4.50, "Dessert of the week": 5.00}
        }
        self.order = {
            "drink": None,
            "appetizer": None,
            "main_course": None,
            "side1": None,
            "side2": None,
            "dessert": None
        }
        self.extras = {}  

    @classmethod
    # This will modify le menu :)
    def modmenu(cls, category, item, price):
        if category in cls.menu:
            cls.menu[category][item] = price
        else:
            cls.menu[category] = {item: price}
        print(f"Menu updated: {item} added to {category}.")

    @staticmethod
    # People need to learn that they need to pay taxes, which is why i put taxes for the static method :)
    def tax(amount):
        # HEHE TAXES >:)
        return amount * DinerOrder.tax_rate

    def print_menu(self):
        print(" ")
        print("Welcome to NONE EXISTENT😎, a non existent Restaurant!!!!!!!")
        print("This is our Menu 😁:")
        for category, items in self.menu.items():
            print(f"\n{category.capitalize()}:")
            for item, price in items.items():
                print(f"{item}: ${price:.2f}")

    def takeorder(self):
        #This will take the order of the user
        self.print_menu()
        print(" ")
        print("Hello, my name is non_existent :) , I will be your waiter for today! :D")
        input("What is your name?: ")
        print("\nPlease place your order (press Enter to skip a category):")

        self.order["drink"] = self.get_order("drink", "Drink")
        if self.order["drink"] in ["Soda", "Water"]:
            self.extras["ice"] = input("Would you like ice with your drink? (yes/no): ").lower()

        self.order["appetizer"] = self.get_order("appetizer", "Appetizer")

        self.order["main_course"] = self.get_order("main_course", "Main Course")
        if self.order["main_course"] == "Burger":
            self.extras["doneness"] = input("How would you like your burger? (well done, medium rare): ").lower()

        self.order["side1"] = self.get_order("side1", "Side 1")
        self.order["side2"] = self.get_order("side2", "Side 2")
        self.order["dessert"] = self.get_order("dessert", "Dessert")

    def get_order(self, category_key, display_name):
        # Get item from user and check if it's on the menu
        user_input = input(f"{display_name}: ")
        if user_input:
            for category, items in self.menu.items():
                if user_input in items:
                    return user_input
            print(f"Sorry, {user_input} is not on the menu :(")
        return None
    
    def print_order(self):
        # Print the user's current order with the customizations
        print("\nYour current order:")
        for category, item in self.order.items():
            if item:
                print(f"{category.capitalize()}: {item}")
        if self.extras:
            print("\nCustomizations:")
            for extra, value in self.extras.items():
                print(f"{extra.capitalize()}: {value}")
        if not any(self.order.values()):
            print("You haven't ordered anything yet... Why T-T")

    def calculate_total(self):
        # This will alculate the total price of the user's order
        total = 0.0
        for category, item in self.order.items():
            if item:
                for menu_category, items in self.menu.items():
                    if item in items:
                        total += items[item]
        return total

    def order_valid(self):
        # This makes sure that the order is all valid cuz why not
        return any(self.order.values())

    def change_item(self):
        # This will allow the user to change their order
        self.print_order()
        category = input("\nWhich item would you like to change (drink, appetizer, main_course, side1, side2, dessert)? ").lower()
        if category in self.order:
            new_item = input(f"Enter the new item for {category.capitalize()}: ")
            if new_item in [item for category in self.menu.values() for item in category]:
                self.order[category] = new_item
                print(f"{category.capitalize()} has been changed to {new_item}.")
            else:
                print(f"Sorry, {new_item} is not on the menu.")
        else:
            print("This category is invalid...")

    def place_order(self):
        if self.order_valid():
            self.print_order()
            total = self.calculate_total()
            print(f"\nYour total without tax is: ${total:.2f}")
            tax = DinerOrder.tax(total)
            FullPayment = total + tax
            print(f"Your total with taxes is: ${FullPayment:.2f}")
        else:
            print("You have to order at least one item before placing your order cuz that aint fair ye know.")



diner = DinerOrder()
diner.takeorder()
diner.print_order()
diner.place_order()

diner.change_item()
diner.place_order()
