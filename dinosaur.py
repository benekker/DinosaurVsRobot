class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def dino_details(self):
        self.name = 'Mr. T'
        self.attack_power = 25

    #returning to this function later on
    def attack(self, robot):
        pass
