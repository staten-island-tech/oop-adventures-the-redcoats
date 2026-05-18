import random
""" class Patriots:
    def __init__(self, health = 100, living = True):
        self.health = health
        self.living = living
    def impact_1(self):
        self.health -= 100
        self.living = False """

class Soldier: 
    def __init__(self, name, hunger=100, health=100, fun=100, ammo=30, shots = 0, shillings = 0, suppliescaptured = 0, positionsheld = 0, food = 0, bandages = 0, sabre = 0, kills = 0, living = True): 
        self.name = name
        self.hunger=hunger
        self.health=health
        self.fun=fun
        self.ammo=ammo
        self.shots=shots
        self.shillings=shillings
        self.kills = kills
        self.living=living
        self.suppliescaptured = suppliescaptured
        self.positionsheld = positionsheld
        self.food = food
        self.bandages = bandages
        self.sabre = sabre

    def shopping(self):
        print("Welcome to the shop! My name's Bubbles, and Im selling a lotta good stuff here! Food: 3 shillings, Bandages: 3 shillings, Sabre: 5 shillings!")
        RESPONSE = input("What do you want to buy?")
        RESPONSE =RESPONSE.lower()
        if "food" in RESPONSE:
            if self.shillings >= 3: 
                print("You purchased food!")
                self.food += 1
                self.shillings -= 3
            elif self.shillings <3: 
                print("My apologies..you don't have the expense to buy it...")
        elif "bandages" in RESPONSE:
            if self.shillings >= 3: 
                print("You purchased one bandage!")
                self.bandage += 1
                self.shillings -= 3
            elif self.shillings <3: 
                print("My apologies..you don't have the expense to buy it...")
        elif "sabre" in RESPONSE:
            if self.shillings >=5: 
                print("You purchased one Sabre!")
                self.sabre += 1
                self.shillings -= 5
            elif self.shillings <5: 
                print("My apologies..you don't have the expense to buy it...")
            elif self.sabre == 1: 
                print("You have already bought this")
        else: 
            print("Sorry, that's not in the shop, try again")
    
    def loading(self): 
        print(".")
        print(". .")
        print(". . .")
    def byebye(self): 
        self.fun -= 2
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
        self.shillings +=2
        self.fun +=10
    def capturesupplies(self): 
        self.suppliescaptured += 10
        self.fun += 20
    def death(self): 
        print("You have died and failed your mission...")
        self.living == False
    def findsupplies(self): 
        print("You go searching...") 
        self.loading()
        self.byebye()
        x = random.randint(1, 20)
        if x <15: 
            print("You've found nothing...") 
            self.byebye()
            self.loading()
        elif x>=15: 
            print("You've looted some supplies the Patriots stole!")
            self.capturesupplies()
            self.loading()
    def findpatriots(self): 
        print("You run and try to find filthy rebels to kill")
        self.loading()
        if self.ammo >0: 
            e = random.randint(0, 5)
            if e >0: 
                print(f"You've found {e}!")
                self.loading()
                weaponchoice = input(f"Would you like to kill using a musket or sabre?")
                if "musket" in weaponchoice: 
                    self.loading()
                    shoot = input(f"Press x to shoot!")
                    if "x" in shoot: 
                        self.loading()
                        x = random.randint(1, 20)
                        if x <=10: 
                            print("Oh no! You missed! Now they've shot you!")
                            self.shoot()
                            self.damage()
                            self.byebye()
                            self.loading()
                        elif x >10: 
                            print("You've shot them!") 
                            self.kills += e
                            self.shoot()
                            self.loading()
                elif "sabre" in weaponchoice: 
                    self.loading()
                    if self.sabre == 1: 
                        print("You've successfully killed them!") 
                        self.kills += e
                        self.loading()
                    elif self.sabre <1: 
                        print("You do not have that weapon...you draw nothing and they shoot you instead")
                        self.byebye()
                        self.damage()
                        self.loading()
                else: 
                    self.loading()
                    print("That's not a weapon...you draw nothing and they shoot you instead...")
                    self.byebye()
                    self.damage()
                    self.loading()
            elif e == 0: 
                print("You've found none...")
                self.byebye()
        elif self.ammo == 0: 
            self.loading()
            print("You have no ammo...they shot you before you could react")
            self.byebye()
            self.damage()
    def lootandplunder(self): 
        print("You start looting the dead bodies of fallen comrades and enemies.")
        self.loading()
        self.byebye()
        x = random.randint(1, 20)
        if x <5: 
            print("You've found some money!")
            self.find()
            self.loading()
        elif x >=5: 
            print("You've found nothing...")
            self.byebye()
            self.loading()
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
            self.loading()
        elif x <=10: 
            print("You stumble and fail to help man the cannons...your crew gets targetted for an attack instead...")
            self.damage()
            self.byebye()
            self.loading()
    def charge(self): 
        self.byebye()
        print("The officer has commanded a charge! Give 'em hell boys!")
        x = random.randint(1,20)
        print(f"You were able to charge and kill {x} patriots! But you're so exhausted from the adrenaline...")
        self.loading()
        self.byebye()
        self.killedsomething()
        self.damage()
        self.kills +=x
    def finishedlevel1(self): 
        print("You've successfully completed your mission in Lexington and Concord!")
        self.loading()
        print("You're now ordered to take the land of Bunker's Hill")
        self.loading()
    def resetstats(self):
        self.hunger= 100
        self.health= 100
        self.fun= 100
        self.ammo= 30
        self.shots= 0
        self.kills = 0
    def finishedlevel2(self): 
        print("You've successfully completed your mission in Bunker's Hill!")
        self.loading()
        print("The Battle of Saratoga is about to commence. Win the battle.")
    def usefood(self): 
        if self.hunger <= 70: 
            self.hunger +=30
            self.health+=5
            self.fun +=10
            self.food -=1
            self.loading()
            print("It's delicious...satisfying to this hunger...")
        elif self.hunger > 70: 
            print("You aren't hungry...")
    def usebandages(self): 
        if self.health <=80: 
            self.health +=20
            self.fun +=5
            self.bandages -=1
            self.loading()
            print("Healing the wounds...")
        elif self.health >= 80: 
            print("You're health is fine, no need to heal")
    def holdposition(self): 
        print("Hold your formation! Hold steady lads!") 
        self.loading()
        self.byebye()
        x = random.randint(1,20)
        if x >15: 
            print("Your position was maintained...the rebels couldn't break through your formation")
            self.positionsheld += 1
            self.loading()
        elif x <=15: 
            print("The patriots broke through...you failed to maintain your position...") 
            self.byebye()
            self.damage()
            self.loading()
    def finishedlevel3(self): 
        print("You've completed your mission...but so many lives were lost in the process...") 
        self.loading()
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


        

Name = input("What do you call yourself, sir?")
character = Soldier(Name)
character.resetstats()
print("You're told to stop the patriots at Lexington and Concord by your commander.")

while True: 
    level1 = input("Write play to begin the level.")
    if level1 == "play": 
        character.loading()
        character.resetstats()
        if character.kills == 10 and character.shillings == 4: 
            character.finishedlevel1()
            break
        while character.living == True: 
            character.dec()
            print(f"{character.shillings} shillings")
            print(f"{character.kills} kills")
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
            elif "shop" in Userinput: 
                character.shopping()
            elif "use food" in Userinput: 
                character.usefood()
                character.loading()
            elif "use bandages" in Userinput: 
                character.usebandages()
                character.loading()
            if character.health <= 0: 
                character.loading()
                character.death()
                break
    else: 
        print("Invalid command.")  


while True: 
    level2 = input("Write play to begin the level.")
    if level2 == "play": 
        character.resetstats()
        character.loading()
        if character.kills == 30 and character.shots == 6: 
            character.finishedlevel2()
            break
        while character.living == True: 
            character.dec()
            print(f"{character.shillings} shillings")
            print(f"{character.kills} kills")
            Userinput2 = input(f"What would you like to do? Man the canons, bayonet charge, or find patriots?")
            Userinput2 =Userinput2.lower()
            if "man the canons" in Userinput2: 
                character.loading()
                character.manthecanons()
            elif "find patriots" in Userinput2: 
                character.loading()
                character.findpatriots()
            elif "bayonet charge" in Userinput2:
                character.loading()
                character.charge()
            elif "shop" in Userinput2: 
                character.shopping()
            elif "use food" in Userinput2: 
                character.usefood()
                character.loading()
            elif "use bandages" in Userinput2: 
                character.usebandages()
                character.loading()
            if character.health <= 0: 
                character.loading()
                character.death()
                break
    else: 
        print("Invalid command.")  
        
while True: 
    level3 = input("Write play to begin the level.")
    if level3 == "play": 
        character.resetstats()
        character.loading()
        if character.kills == 50 and character.positionsheld == 10: 
            character.finishedlevel3()
            break
        while character.living == True: 
            character.dec()
            print(f"{character.shillings} shillings")
            print(f"{character.kills} kills")
            Userinput3 = input(f"What would you like to do? Kill patriots, bayonet charge, or hold position?")
            Userinpu32 =Userinput3.lower()
            if "hold position" in Userinput3: 
                character.loading()
                character.holdposition()
            elif "kill patriots" in Userinput3: 
                character.loading()
                character.findpatriots()
            elif "bayonet charge" in Userinput3:
                character.loading()
                character.charge()
            elif "shop" in Userinput3: 
                character.shopping()
            elif "use food" in Userinput3: 
                character.usefood()
                character.loading()
            elif "use bandages" in Userinput3: 
                character.usebandages()
                character.loading()
            if character.health <= 0: 
                character.loading()
                character.death()
                break
    else: 
        print("Invalid command.") 


while True:
    print("Yorktown is going to be sieged by the Patriots! Defend Yorktown!")
    level4 = input("Type 'play' to begin the level.")
    if level4 == "play": 
        character.resetstats()
        character.loading()
        if character.kills == 30 and character.alivecomrades >= 15:
            character.finishedlevel4()
            break
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


while character.finishedlevel4:
    character.loading()
    print("Another day, another battle.")
    character.loading()
    print("However, this morning you woke up with a bad feeling in your stomach...")
    character.loading()
    character.loading()
    ending = input("You're now in the middle of a fight against a Patriot! Are you willing to do whatever it takes to survive?")
    if ending == "yes":
        print("You pull out your musket and point it straight towards your opponent...")
        print("You are about to pull the trigger, but suddenly... an immense pain explodes across your body...")
        character.loading()
        print("You've just been brutally shot...")
        character.loading()
        print("You fall to the ground...the bullet's force had taken the breath out of your lungs...")
        print("You cough up blood...you try to scream, call for help...but the words don't come out...")
        print("You feel your life slowly fading away...but there is a warm, welcoming light inviting you to come towards it...")
        print("You have died...was it worth it?")