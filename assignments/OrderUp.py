class DinerOrder:
    def __init__(self):
        # Initialize the menu and order
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


    def print_menu(self):
        # Print the available menu
        print(" ")
        print("This is our Menu:")
        for category, items in self.menu.items():
            print(f"\n{category.capitalize()}:")
            for item, price in items.items():
                print(f"{item}: ${price:.2f}")

    def take_order(self):
        # Take the user's order for each category
        self.print_menu()
        print(" ")
        print("Hello my name is non_existent :) , I wil be your waiter for today! :D")
        input("What is your name?: ")
        print("\nPlease place your order (press Enter to skip a category):")

        self.order["drink"] = self.get_order_item("drink", "Drink")
        self.order["appetizer"] = self.get_order_item("appetizer", "Appetizer")
        self.order["main_course"] = self.get_order_item("main_course", "Main Course")
        self.order["side1"] = self.get_order_item("side1", "Side 1")
        self.order["side2"] = self.get_order_item("side2", "Side 2")
        self.order["dessert"] = self.get_order_item("dessert", "Dessert")


    def get_order_item(self, category_key, display_name):
        # Get item from user and check if it's on the menu
        user_input = input(f"{display_name}: ")
        if user_input:
            for category, items in self.menu.items():
                if user_input in items:
                    return user_input
            print(f"Sorry, {user_input} is not on the menu.")
        return None
    

    def print_order(self):
        # Print the user's current order
        print("\nYour current order:")
        for category, item in self.order.items():
            if item:
                print(f"{category.capitalize()}: {item}")
        if not any(self.order.values()):
            print("You haven't ordered anything yet.")

    def calculate_total(self):
        # This wil calculate the total price of what the uer wants to order
        total = 0.0
        for category, item in self.order.items():
            if item:
                for menu_category, items in self.menu.items():
                    if item in items:
                        total += items[item]
        return total

    def is_order_valid(self):
        # Ensure that at least one item has been ordered
        return any(self.order.values())

    def change_item(self):
        # This wil allow the user to change their order
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
        if self.is_order_valid():
            self.print_order()
            total = self.calculate_total()
            print(f"\nThat would be: ${total:.2f}")
            total = self.calculate_total() *0.07
            FullPayment = total + self.calculate_total()
            print(f"\nYour total with taxes is: $ {FullPayment:.2f}")
        else:
            print("You have to order at least one item before placing your order.")

diner = DinerOrder()
diner.take_order()
diner.print_order()
diner.place_order()


diner.change_item()
diner.place_order()