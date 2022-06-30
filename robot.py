from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Mega Sword', 40)

    #returning to this function later on
    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} and dealt 40 damage with a Mega Sword!')
        dinosaur.health -= 40