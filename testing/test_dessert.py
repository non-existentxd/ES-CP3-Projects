from dessert import Dessert

def test_Candy():
    testdessert = Dessert()
    name = testdessert.Candy()
    assert name == "Candy"

def test_Cookie():
    testdessert = Dessert()
    name = testdessert.Cookie()
    assert name == "Cookie"

def test_IceCream():
    testdessert = Dessert()
    name = testdessert.IceCream()
    assert name == "Ice Cream"

def test_Sundae():
    testdessert = Dessert()
    name = testdessert.Sundae()
    assert name == "Sundae"