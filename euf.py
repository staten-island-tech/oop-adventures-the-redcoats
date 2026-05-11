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
        self.hunger -= 5
    def dec(self): 
        if self.fun >30: 
            print("You're having fun!")
        if self.hunger>30: 
            print("You're full")
        if self.health >50: 
            print("You're surviving so far...")
        if self.ammo >0: 
            print(f"You have {self.ammo} ammo")
        if self.fun <=30: 
            print("You're getting bored!")
            self.health -=1
            self.hunger-=5
        if self.hunger <=30: 
            print("You're getting hungry!")
            self.health -=2
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
        if self.health <= 0: 
            self.living == False
            print("You have died!")
    def findsupplies(self): 
        print("You go searching...") 
        self.byebye()
        x = random.randint(1, 20)
        if x <15: 
            print("You've found nothing...") 
            self.byebye()
        elif x>=15: 
            print("You've looted some supplies the Patriots stole!")
            self.find()
            self.fun +=20

Name = input("What do you call yourself, sir?")
character = Soldier(Name)
print("You're told to stop the patriots at Lexington and Concord by your commander.")
kills = 0
level1 = input("Write play to begin the level.")
if "play" in level1: 
    while character.living == True: 
        character.dec()
        Userinput = input(f"What would you like to do? Loot and plunder, find supplies, or find patriots?")
        Userinput =Userinput.lower()
        if "find supplies" in Userinput: 
            character.findsupplies()
        elif "find patriots" in Userinput: 
            e = random.randint(0, 5)
            if e >0: 
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
                            kills += e
                            character.shoot()
            elif e == 0: 
                print("You've found none...")
                character.byebye()
        elif "loot and plunder" in Userinput:
            character.byebye()
            x = random.randint(1, 20)
            if x <5: 
                print("You've found some money!")
                character.find()
            elif x >=5: 
                print("You've found nothing...")
                character.byebye()
        if kills == 10 and character.shillings == 10: 
            level1 = "finished"
    if character.living == False: 
        character.death()
        


elif "finished" in level1: 
    print("You've successfully completed your mission in Lexington and Concord!")
    print("You're now ordered to take the land of Bunker's Hill")
kills = 0
character.hunger=100
character.health = 100
character.fun = 100
character.ammo=30
shots = 0
level2 = input("Write play to begin the level.")
if "play" in level2: 
    while character.living == True: 
        character.dec()
        Userinput2 = input(f"What would you like to do? Man the canons, bayonet charge, or find patriots?")
        Userinput2 =Userinput2.lower()
        if "man the canons" in Userinput2: 
            print("You're ordered to help with artillery strikes") 
            character.byebye()
            x = random.randint(1, 20)
            if x <15: 
                print("You've found nothing...") 
            elif x>=15: 
                print("You've looted some supplies the Patriots stole!")
                character.find()
                character.fun +=20
        if "find patriots" in Userinput: 
            e = random.randint(0, 5)
            if e >0: 
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
                            kills += e
                            character.shoot()
            elif e == 0: 
                print("You've found none...")
                character.byebye()
        if "bayonet charge" in Userinput2:
            print("The officer has commanded a charge! Give 'em hell boys!")
            character.byebye()
            x = random.randint(1, 20)
            if x <5: 
                print("You've found some money!")
                character.find()
            elif x >=5: 
                print("You've found nothing...")
                character.byebye()
        if kills == 10 and character.shillings == 10: 
            level2 = "finished"
elif "finished" in level2:  
    print("You've successfully completed your mission in Lexington and Concord!")