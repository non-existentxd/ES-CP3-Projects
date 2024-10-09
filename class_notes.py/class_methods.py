
class pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl

    def combat(self, other):
        if self.lvl> other.lvl:
            return f"{self.name} won"
        elif self.lvl < other.lvl:
            return f"{self.name} lost!"
        else:
            return f"{other.name} and {self.name} are too exhausted to fight. You both lost."

    def __str__(self):
        return (f"""
                Name: {self.name},
                HP: {self.hp},
                Type: {self.typ},
                Level: {self.lvl}            
""")
    #@classmethod used to keep method from changing object instances
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp*1.5)
    @classmethod
    def pikachu(self):
        return pokemon(input("Give me a name: "), 50, "electric", 1)

    #static methods do not require self or class, they operate like a normal function
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5


eevee= pokemon("Jayrod", 37, "normal", 2)
pika = pokemon.pikachu()
charizard = pokemon("Bob", 1, "Fire", 36)

pika.hp = pokemon.hp_update(pika)

print(eevee.lvl_up)
print (pika)