import random

class Soldier: 
    def __init__(self, name, hunger=100, health=100, fun=100, ammo=30, shillings = 0, food = 0, bandages = 0, sabre = 0, living = True): 
        self.name = name
        self.hunger=hunger
        self.health=health
        self.fun=fun
        self.ammo=ammo
        self.shillings=shillings
        self.living=living
        self.food = food
        self.bandages = bandages
        self.sabre = sabre
        
    def byebye(self): 
        self.fun -= 10
        self.hunger -= 20
    def dec(self): 
        if self.fun >30: 
            print("You're having fun!")
        if self.hunger>30: 
            print("You're full")
        if self.health >30: 
            print("You're surviving so far...")
        if self.ammo >0: 
            print(f"You have {self.ammo} ammo")
        if self.fun <=30: 
            print("You're getting bored!")
            self.health -=10
            self.hunger-=20
        if self.hunger <=30: 
            print("You're getting hungry!")
            self.health -=30
        if self.health<=50: 
            print(f"You have {self.health} health")
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
    def death(self): 
        if self.health == 0: 
            self.living == False
            print("You have died!")

Name = input("What do you call yourself, sir?")
character = Soldier(Name)
print("You're told to stop the patriots at Lexington and Concord by your commander.")
kills = 0
level1 = input("Write play to begin the level.")
if "play" in level1: 
    while character.living == True: 
        character.dec()
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
            x = random.randint(1, 5)
            print(f"You've found {x}!")
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
                        print("You've shot them!") 
                        kills += x
        if "loot and plunder" in Userinput:
            character.byebye()
            x = random.randint(1, 20)
            if x <5: 
                print("You've found some money!")
                character.find()
            elif x >=5: 
                print("You've found nothing...")
                character.byebye()
        if kills == 20 and character.shillings == 30: 
            level1 = "finished"
elif "finished" in level1: 
    print("You've successfully completed your mission in Lexington and Concord!")