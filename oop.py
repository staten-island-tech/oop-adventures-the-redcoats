import random
""" class Patriots:
    def __init__(self, health = 100, living = True):
        self.health = health
        self.living = living
    def impact_1(self):
        self.health -= 100
        self.living = False """

#(UNDER CLASS SOLDIER)


class Soldier: 
    def __init__(self, name, hunger=100, health=100, fun=100, ammo=30, food = 0, bandages = 0, sabre = 0, living = True): 
        self.name = name
        self.hunger=hunger
        self.health=health
        self.fun=fun
        self.ammo=ammo
        self.living=living
        self.food = food
        self.bandages = bandages
        self.sabre = sabre
        
        def SHOPPING(self):
            print("Welcome to the shop! My name's Bubbles, and Im selling a lotta good stuff here! Food: 3 shillings, Bandages: 3 shillings, Sabre: 5 shillings!")
            RESPONSE = input("What do you want to buy?")
            if "Food" in RESPONSE:
                print("You purchased food!")
                self.food += 1
                self.shillings -= 3
            elif "Bandages" in RESPONSE:
                print("You purchased one bandage!")
                self.bandage += 1
                self.shillings -= 3
            elif "Sabre" in RESPONSE:
                print("You purchased one Sabre!")
                self.sabre += 1
                self.shillings -= 5