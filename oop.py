import random
""" class Patriots:
    def __init__(self, health = 100, living = True):
        self.health = health
        self.living = living
    def impact_1(self):
        self.health -= 100
        self.living = False """

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

    def shopping(self):
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
    def hide(self):
        print("You look for a place to hide...") 
        character.byebye()
        x = random.randint(1, 20)
        if x <15: 
            print("You crouch behind a bush...like the coward you are!") 
        elif x >= 15: 
            print("You were caught trying to hide, you coward!")
        self.fun -= 10
    def death(self): 
        if self.health <= 0: 
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
            e = random.randint(1, 20)
            if e <15: 
                print("You've found nothing...") 
            if e>=15: 
                print("You've looted some supplies the Patriots stole!")
                character.find()
        if "find patriots" in Userinput: 
            e = random.randint(1, 5)
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





#MINE
print("Yorktown is going to be sieged by the Patriots! Defend Yorktown!")
alivecomrades = 20
deadcomrades = 0
kills = 0
level4 = input("Type 'play' to begin the level.")
if "play" in level4: 
    while character.living == True: 
        character.dec()
        Userinput = input(f"What would you like to do?")
        Userinput =Userinput.lower()
        if "hide" in Userinput: 
            print("You look for a place to hide...") 
            character.byebye()
            x = random.randint(1, 20)
            if x <15: 
                print("You crouch behind a bush...like the coward you are!") 
            elif x >= 15: 
                print("You were caught trying to hide, you coward!")
                character.hide()
        if "attack" in Userinput or "fight" in Userinput: 
            e = random.randint(1, 5) 
            print(f"You've found {e}!")
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
        if kills == 30 and alivecomrades >= 15: 
            level1 = "finished"
elif "finished" in level4: 
    print("You've successfully defended Yorktown!")
