from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()

    def robot_details(self):
        self.name = 'WALL-E'

    #returning to this function later on
    def attack(self, dinosaur):
        pass
