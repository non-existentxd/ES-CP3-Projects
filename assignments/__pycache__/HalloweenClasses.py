class Monster:
    def __init__(self, name: str = '', typ: str = '', place: str = '', method_of_attack: str = '', attack_damage: int = 0, unique_hobby: str = '', health:int = 0):
        self.typ = typ
        self.name = name
        self.place = place
        self.method_of_attack = method_of_attack
        self.attack_damage = attack_damage
        self.unique_hobby = unique_hobby
        self.health = health

    def __str__(self):
        return (f"""
                Name: {self.name},
                Place: {self.place},
                Type: {self.typ},
                Method of attack: {self.method_of_attack}
                Attack damage: {self.attack_damage}
                Hobby: {self.unique_hobby}            
""")

class Wendigo(Monster):
    def Jeff(self):
        Monster("Jeff", "Wendigo", "North Carolina", "Magical Antlers", 7, "Likes to read books and does yoga on Sundays")




class Cyclopes(Monster):


class Vampire(Monster):


class Chimera(Monster):

class Attack:
    def combat(self, other):
        if self.health> other.health:
            return f"{self.name} won"
        elif self.health < other.health:
            return f"{self.name} lost!"
        else:
            return f"{other.name} and {self.name} are too exhausted to fight. You both lost."
