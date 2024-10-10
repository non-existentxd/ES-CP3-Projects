class DineOrder:
    def __init__(self, drink, appetizer, mainCourse, side1, side2, dessert):
        self.drink = drink
        self.appetizer = appetizer
        self.mainCourse = mainCourse
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert

        self.menu = {
            "drinks" : {"Water": 0, "Soda": 2.00, "Coffee": 3.00, "Juice": 2.50},
            "appetizers": {"Fries": 3.00, "Salad": 4.00, "Wings": 5.00, "Soup": 4.00},
            "main course": {"Burger": 8.00, "Steak": 15.00, "Chicken Sandwich": 9.00, "Pizza": 12.00},
            "side 1": {"Mashed Potatoes": 2.50, "Vegestables": 2.00, "Rice": 3.00, "Soup": 4.00},
            "side 2": {"Mashed Potatoes": 2.50, "Vegestables": 2.00, "Rice": 3.00, "Soup": 4.00},
            "dessert": {"Ice cream": 2.50, "Cake": 4.00, "Float": 3.00, "Surprise Dessert": 3.00}
        }


    def __str__(self):
        return (f"""
                Drink: {self.drink},
                Appetizer: {self.appetizer},
                Main Course: {self.mainCourse},
                Side 1: {self.side1},
                Side 2: {self.side2},
                Dessert: {self.dessert}

""")

    @classmethod
    def name(self):
        return DineOrder(input("What is your name?: "), input("What appeztizer would you like?: "), input("what would you like for your Main Course?: "), input("Your Main Course comes with 2 sides, what would you like for your first side?: "), input("Now what would you like for you second side?: "), input("lastly, what would you like for dessert?: "))
    

def start():
    print("Hello! Welcome to the 'Diner'! my name is Jakob and i will be your server. Here is the menu.")
    print(self.menu)
    print(name(self))
