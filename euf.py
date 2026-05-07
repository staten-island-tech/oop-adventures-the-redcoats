import random

class Soldier: 
    def __init__(self, name, hunger=100, health=100, fun=100, ammo=30, shillings = 0, living = True): 
        self.name = name
        self.hunger=hunger
        self.health=health
        self.fun=fun
        self.ammo=ammo
        self.shillings=shillings
        self.living=living
    def byebye(self): 
        self.fun -= 10
        self.hunger -= 20
    def dec(self): 
        if self.fun <30: 
            print("You're having fun!")
        if self.hunger>30: 
            print("You're full")
        if self.health >30: 
            print("You're surviving so far...")
        if self.ammo >0: 
            print(f"You have {self.ammo}")
        if self.fun <=30: 
            print("You're getting bored!")
        if self.hunger <=30: 
            print("You're getting hungry!")
        if self.health<=50: 
            print("You're health is {self.health} health")
        if self.ammo == 0: 
            print("You have no ammo!")
    def shoot(self): 
        self.ammo -= 1
    def killedsomething(self): 
        self.fun+=20
        if self.fun>=100: 
            self.fun == 100
    def damage(self): 
        self.hunger -=5
        self.health -=20
        self.fun -=10
    def find(self): 
        self.shillings +=5
        self.fun +=10

Name = input("What do you call yourself, sir?")
character = Soldier(Name)

while character.living == True: 
    character.dec()
    print("You're told to stop the patriots at Lexington and Concord by your commander.")
    Userinput = input(f"What would you like to do?")
    Userinput =Userinput.lower()
    if "find supplies" in Userinput: 
        print("You go searching...") 
        character.byebye()
        x = random.randint(1, 20)
        if x <15: 
            print("You've found nothing...") 
        if x>=15: 
            print("You've looted some supplies the Patriots stole!")
            character.find()
            character.fun +=20
    if "find patriots" in Userinput: 
        x = random.randint(1, 20)
        print("You've found {x}!")
        weaponchoice = input(f"Would you like to kill using a musket or sabre?")
        if "musket" in weaponchoice: 
            shoot = input(f"Press x to shoot!")
            if "x" in shoot: 
                x = random.randint(1, 20)
                if x <=10: 
                    print("Oh no! You missed! Now they've shot you!")
                    character.shoot()
                    character.damage()
                    character.byebye()
                elif x >10: 
                    print("You've shot them!") #finish killing part tomorrow, add patriot class
    if "loot and plunder" in Userinput:
        character.byebye()
        x = random.randint(1, 20)
        if x <5: 
            print("You've found some money!")
            character.find()
        elif x >=5: 
            print("You've found nothing...")
            character.byebye()
