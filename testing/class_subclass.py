class PetStore:
    name = "Pet Smart"
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        self.featured_pet = None

    def add_pet(self, animal):
        #assert will check if statement is true and stop code if false
        #isinstance is like isnum (isnumeric) it just checks if the itme is an instance of the class given
        assert isinstance(animal, Animal)
        self.animals.append(animal)

    def remove(self, animal):
        try:
            self.animals.remove(animal)
        except:
            print("No such animal")
        else:
            print(animal, 'remove')

    def feature(self, name):
        for pet in self.animals:
            if pet.name == name:
                self.featured_pet = pet
                print('Featured pet . . .', pet)
                break
        else:
            print("There is no such pet")

    def get_featured(self):
        return self.featured_pet
    
    def feed(self):
        for pet in self.animals:
            pet.eat()

    def get_mammals(self):
        return self.get_by_type(Mammal)
    
    def get_reptiles(self):
        return self.get_by_type(Reptile)
    
    def get_birds(self):
        return self.get_by_type(Bird)
    
    def get_amphibians(self):
        return self.get_by_type(Amphibian)
    
    def get_fishes(self):
        return self.get_by_type(Fish)
    
    def get_by_type(self, typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]
    

class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"
    
    def eat(self):
        print(self.name, "eating", self.diet)

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Amphibian(Animal):
    pass

class Fish(Animal):
    pass

class Cat(Mammal):
    def __init__(self, name, diet):
        super().__init__(name)
        self.diet = diet
    diet = "mice"

class Dog(Mammal):
    diet = "kibble"

class Reptile(Animal):
    pass

class Snake(Reptile):
    diet = "rodents"

class Turtle(Reptile):
    diet = "carrots"

class Parakeet(Bird):
    diet = "seeds"

class Toucan(Bird):
    diet = "caterpillars"

class Frog(Amphibian):
    diet = "flies"

class newt(Amphibian):
    diet = "worms"
    
class koi(Fish):
    diet = "algae"

class guppy(Fish):
    diet = "flakes"


store = PetStore(1)
store.add_pet(Turtle("Shelly"))
store.add_pet(Cat("Joe"))
store.add_pet(Turtle("Flash"))
store.add_pet(Snake("Robin"))

store.feature("Flash")
store.feed()

print("Reptiles: ")
for pet in store.get_reptiles():
    print(pet)

print("Fishes: ")
for pet in store.get_fishes():
    print(pet)
