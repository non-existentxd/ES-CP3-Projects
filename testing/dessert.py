
class DessertShop:
    name = "dessert Shop"
    def __init__(self, item, measured):
        self.item = item
        self.measured = measured
        self.desserts = []

    def add_item(self, dessert):
        assert isinstance(dessert, Dessert)
        self.desserts.append(dessert)

    def remove(self, dessert):
        try:
            self.desserts.remove(dessert)
        except:
            print("No such Dessert")
        else:
            print(dessert, 'remove')

    def get_pound(self):
        return self.get_by_item(Candy)
    
    def get_dozen(self):
        return self.get_by_item(Cookie)
    
    def get_scoop(self):
        return self.get_by_item(IceCream)

    def get_topping(self):
        return self.get_by_item(Sundae)
    
    def get_by_item(self, typ):
        return [item for item in self.desserts if isinstance(item, typ)]
    

class Dessert:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"
    

class Candy(Dessert):
    candy_weight: float = 0.0
    price_per_pound: float = 0.0

class Cookie(Dessert):
    cookie_quantity: int = 0
    price_per_dozen: float = 0.0

class IceCream(Dessert):
    scoop_count: int = 0
    price_per_scoop: float = 0.0

class Sundae(IceCream):
    scoop_count: int = 0
    price_per_scoop: float = 0.0
    topping_price: float = 0.0



