#Testing from another file to see if it works
from classes_notes import Animal
def test_get_name():
    testanimal = Animal("Bob", "Bobcat", 27, "M", "Epic")
    name = testanimal.get_name()
    assert name == "Bob"