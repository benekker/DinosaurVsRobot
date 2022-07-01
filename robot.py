from weapon import Weapon
MegaSword = Weapon('MegaSword', 40)
bow_arrow = Weapon("Bow n' Arrow", 30)
asteroid = Weapon("Asteroid", 100)


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Mega Sword', 40)

    def get_active_weapon(self):
        print(f'{self.name} you get 3 weapon choices.')
        print("Enter 1 for MegaSword, Enter 2 for Bow n' Arrow, Enter 3 for Asteroid")
        user_input = int(input(f'Please select your weapon: '))
        if user_input == 1:
            self.active_weapon = MegaSword
        elif user_input == 2:
            self.active_weapon = bow_arrow
        elif user_input == 3:
            self.active_weapon = asteroid

    #returning to this function later on
    def attack(self, dinosaur):
        print(f'{self.name} you get 3 weapon choices.')
        print("Enter 1 for MegaSword, Enter 2 for Bow n' Arrow, Enter 3 for Asteroid")
        user_input = int(input(f'Please select your weapon: '))
        if user_input == 1:
            self.active_weapon = MegaSword
        elif user_input == 2:
            self.active_weapon = bow_arrow
        elif user_input == 3:
            self.active_weapon = asteroid
        print(f'{self.name} attacked {dinosaur} and dealt {self.active_weapon.attack_power} damage with a {self.active_weapon.name}')
        



