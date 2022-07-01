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
        print("")
        print('\nWelcome...TO DINOSAUR VS ROBOT!!!\nToday we have two new challengers...')
        print("")
        print(f"In the red corner itsss {robo.name} the robot!!")
        print(f"And fighting out of the blue corner itsss {dino.name} the dino!")
        print("")

    def battle_phase(self):
        while dino.health > 0 and robo.health > 0:
                robo.assign_weapon()
                robo.attack(dino)
                dino.attack(robo)
                if robo.health == 0 or dino.health == 0:
                    break

        

    def display_winner(self):
        if robo.health <= 0:
            print(f"Should've been built with more teeth... {dino.name} wins!")
        elif dino.health <= 0:
            print(f"Back to the Jurassic with you! {robo.name} wins!")