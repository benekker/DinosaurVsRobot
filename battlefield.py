from dinosaur import Dinosaur
from robot import Robot

dino = Dinosaur('Mr. T', 25)
robo = Robot('WALL-E')

class Battlefield:
    def __init__(self):
        self.run = True

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome...TO DINOSAUR VS ROBOT!!!')
        print("Today we have two new challengers...")
        print(f"In the red corner itsss {robo.name} the robot!!")
        print(f"And fighting out of the blue corner itsss {dino.name} the dino!")

    def battle_phase(self):
        while self.run == True:
            if dino.health > 0:
                robo.attack(dino.name)
                dino.health -= robo.active_weapon.attack_power
                print(f'{dino.name} has {dino.health} health remaining!')
                if dino.health <= 0:
                    break
            if robo.health > 0:
                dino.attack(robo.name)
                robo.health -= dino.attack_power
                print(f'{robo.name} has {robo.health} health remaining!')
                if robo.health <= 0:
                    break
            else:
                self.run = False


    def display_winner(self):
        if robo.health <= 0:
            print(f"Should've been built with more teeth... {dino.name} wins!")
        elif dino.health <= 0:
            print(f"Back to the Jurassic with you! {robo.name} wins!")