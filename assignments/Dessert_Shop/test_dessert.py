from assignments.Dessert_Shop.dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_dessert_item():
    dessert = DessertItem("Generic Dessert")
    assert dessert.name == "Generic Dessert"


def test_candy():
    candy = Candy("Lollipop", 2.5, 1.99)
    assert candy.name == "Lollipop"
    assert candy.candy_weight == 2.5
    assert candy.price_per_pound == 1.99


def test_cookie():
    cookie = Cookie("Chocolate Chip", 12, 5.99)
    assert cookie.name == "Chocolate Chip"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 5.99


def test_ice_cream():
    ice_cream = IceCream("Vanilla", 3, 1.50)
    assert ice_cream.name == "Vanilla"
    assert ice_cream.scoop_count == 3
    assert ice_cream.price_per_scoop == 1.50


def test_sundae():
    sundae = Sundae("Chocolate Sundae", 2, 1.75, "Sprinkles", 0.5)
    assert sundae.name == "Chocolate Sundae"
    assert sundae.scoop_count == 2
    assert sundae.price_per_scoop == 1.75
    assert sundae.topping_name == "Sprinkles"
    assert sundae.topping_price == 0.5
