#We start with keyboard class and we name them using Pascalcase

class Animal:
    #We start with the constructor
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity

    def get_name(self):
        return self.name

#methods are functions inside of a class
    def fight(self, other):
        if len(self.name)> len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name)< len(other.name):
            self.losses +=1
            return self.name
        else:
            other.losses += 1
            self.losses +=1
            return "Tie"

#Makes a more readable string when printed
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nGender: {self.gender}\nRarity: {self.rarity}\n"


#We generaly store objects in variables (individually or in a list) so we can use it!
cat = Animal("Tom", "cat", 21, "Male", "Common")
frog = Animal("Jarrod", "Poison Dart frog", 500, "Female", "Rare")

cat.losses = 1




#to call a method you put the name of the object.name of the method(needed arguments)    
print(cat.fight(frog)) 
cat.losses = 0
frog.losses = 0    

cat.name = "Thomas" 
print(cat.losses)

print(cat.fight(frog))
print(cat.losses)
print(frog.losses)

cat = None
print(cat)





