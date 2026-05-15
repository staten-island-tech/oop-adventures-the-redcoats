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
        print("Would you like to check out the shop?")
        if "yes" in Userinput:
            print("Welcome to the shop! My name's Bubbles, and I'm selling a lotta good stuff here! Food: 3 shillings, Bandages: 3 shillings, Sabre: 5 shillings!")
            response = input("What do you want to buy?")
            if self.shillings == 0:
                print("Sorry, you do not have enough shillings to make a purchase.")
            elif "Food" in response and self.shillings >= 3:
                print("You purchased food!")
                self.food += 1
                self.shillings -= 3
            elif "Bandages" in response and self.shillings >= 3:
                print("You purchased one bandage!")
                self.bandage += 1
                self.shillings -= 3
            elif "Sabre" in response and self.shillings >= 5:
                    print("You purchased one Sabre!")
                    self.sabre += 1
                    self.shillings -= 5
        elif "no" in Userinput:
            print("")

    def loading(self):
        print(".")
        print("..")
        print("...")
    def byebye(self): 
        self.fun -= 10
        self.hunger -= 5
    def dec(self): 
        if self.fun >30: 
            print("You're having fun!")
        elif self.fun <=30: 
            print("You're getting bored!")
            self.health -=1
            self.hunger-=5
        if self.hunger>30: 
            print("You're full")
        elif self.hunger <=30: 
            print("You're getting hungry!")
            self.health -=2
        if self.health >50: 
            print("You're surviving so far...")
        elif self.health<=50: 
            print(f"You have {self.health} health")
        if self.ammo >0: 
            print(f"You have {self.ammo} ammo")
        elif self.ammo == 0: 
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
        print("You have died and failed your mission...")
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
    def findpatriots(self): 
        if self.ammo >0: 
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
                            self.shoot()
                            self.damage()
                            self.byebye()
                        elif x >10: 
                            print("You've shot them!") 
                            self.kills += e
                            self.shoot()
            elif e == 0: 
                print("You've found none...")
                self.byebye()
        elif self.ammo == 0: 
            print("You have no ammo...they shot you before you could react")
            self.byebye()
            self.damage()
    def lootandplunder(self): 
        self.byebye()
        x = random.randint(1, 20)
        if x <5: 
            print("You've found some money!")
            self.find()
        elif x >=5: 
            print("You've found nothing...")
            self.byebye()
    def manthecanons(self): 
        self.byebye()
        print("You're ordered to help with artillery strikes") 
        x = random.randint(1,20)
        if x>10: 
            e = random.randint(1,5)
            a = e+2
            print(f"You've armed {e} cannons and killed {a} patriots!")
            self.kills +=a
            self.shots += e
            self.killedsomething()
        elif x <=10: 
            print("You stumble and fail to help man the cannons...your crew gets targetted for an attack instead...")
            self.damage()
            self.byebye()
    def charge(self): 
        self.byebye()
        print("The officer has commanded a charge! Give 'em hell boys!")
        x = random.randint(1,20)
        print(f"You were able to charge and kill {x} patriots! But you're so exhausted from the adrenaline...")
        self.byebye()
        self.killedsomething()
        self.damage()
        self.kills +=x
    def finishedlevel1(self): 
        print("You've successfully completed your mission in Lexington and Concord!")
        print(".")
        print(". .") 
        print('. . .')
        print("You're now ordered to take the land of Bunker's Hill")
    def resetstats(self):
        self.hunger= 100
        self.health= 100
        self.fun= 100
        self.ammo= 30
        self.shots= 0
        self.kills = 0
    def finishedlevel2(self): 
        print("You've successfully completed your mission in Bunker's Hill!")
    def hide(self):
        print("You look for a place to hide...") 
        character.byebye()
        x = random.randint(1, 20)
        if x <6: 
            print("You crouch behind a bush...like the coward you are!") 
        elif x >= 6: 
            print("You were caught trying to hide, you coward!")
            self.fun -= 10 
        

    def finishedlevel4(self):
        print("You've successfully defended Yorktown!")


print("Greetings! You are a officially a British soldier! Are you ready for this war?")
Name = input("What do you call yourself, sir?")
character = Soldier(Name)


character.resetstats()
""" print("You're told to stop the Patriots at Lexington and Concord by your commander.")
while True: 
    level1 = input("Write play to begin the level.")
    if level1 == "play": 
        character.loading()
        character.resetstats()
        if character.kills == 10 and character.shillings == 10: 
            character.finishedlevel1()
            break
        while character.living == True: 
            character.dec()
            print(character.shillings)
            print(character.kills)
            Userinput = input(f"What would you like to do? Loot and plunder, find supplies, or find patriots?")
            Userinput =Userinput.lower()
            if "find supplies" in Userinput: 
                character.loading()
                character.findsupplies()
            elif "find patriots" in Userinput: 
                character.loading()
                character.findpatriots()
            elif "loot and plunder" in Userinput:
                character.loading()
                character.lootandplunder()
            if character.health <= 0: 
                character.loading()
                character.death()
                break
    else: 
        print("Invalid command.")   """

""" while True: 
    level2 = input("Write play to begin the level.")
    if level2 == "play": 
        character.resetstats()
        character.loading()
        if character.kills == 40 and character.shots == 15: 
                character.finishedlevel2()
        while character.living == True: 
            character.dec()
            print(character.shillings)
            print(character.kills)
            Userinput2 = input(f"What would you like to do? Man the canons, bayonet charge, or find patriots?")
            Userinput2 =Userinput2.lower()
            if "man the canons" in Userinput2: 
                character.loading()
                character.manthecanons()
            elif "find patriots" in Userinput: 
                character.loading()
                character.findpatriots()
            elif "bayonet charge" in Userinput2:
                character.loading()
                character.charge()
            if character.health <= 0: 
                character.loading()
                character.death()
                break
    else: 
        print("Invalid command.")  """



#MINE




while True:
    character.resetstats()
    print("Yorktown is going to be sieged by the Patriots! Defend Yorktown!")
    alivecomrades = 20
    deadcomrades = 0
    kills = 0
    level4 = input("Type 'play' to begin the level.")
    if "play" in level4: 
        while character.living == True: 
            character.dec()
            Userinput = input(f"What would you like to do? Attack...or hide?")
            Userinput = Userinput.lower()
            if "hide" in Userinput: 
                character.hide()
            elif "attack" in Userinput: 
                character.findpatriots()
            if character.health <= 0:
                 character.death()
                 break
    if kills == 30 and alivecomrades >= 15:
        character.finishedlevel4()