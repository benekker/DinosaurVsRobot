from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dino = Dinosaur('Mr. T', 25)
        self.robo = Robot('WALL-E')

    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome...TO DINOSAUR VS ROBOT!!!')

    def battle_phase(self):
        pass

    def display_winner(self):
        pass