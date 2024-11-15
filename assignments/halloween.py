class Monster:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def attack(self):
        return "This monster attacks in a mysterious way!"
    
class Vampire(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)

    def attack(self):
        return f"{self.name} sinks its fangs into you but they can't because their teeth are weak!"
    
class Zombie(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)

    
    def attack(self):
        return f"{self.name} is from wisconsin. He doesn't eat brains he eats flowers"
    
class Ogre(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)

    def attack(self):
        return f"{self.name} loves his swamo. So stay out of it or he'll start singing HALELUJAH"
    
class SlenderMAN(Monster):
    def __iniT__(self, name, origin):
        super().__init__(name, origin)

    def attack(self):
        return f"{self.name} is really tall, he can kill you and he can look like a tree. Be careful!"
    

vampire = Vampire("Edward Collin", "Forks, Washigton")
zombie = Zombie("Bob", "France")
ogre = Ogre("Shrek", "The Swampe")
slender_man = SlenderMAN("sneederman", "italia")

monster = [vampire, zombie, ogre, slender_man]

for monster in monster:
    print(f"{monster.name} from {monster.origin} attacks: {monster.attack()}")