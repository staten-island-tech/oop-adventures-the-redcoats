class Soldier: 
    def __init__(self, name, hunger=100, health=100, fun=100, ammo=30, living = True): 
        self.name = name
        self.hunger=hunger
        self.health=health
        self.fun=fun
        self.ammo=ammo
        self.living=living
    def byebye(self): 
        self.fun -= 10
        self.hunger -= 20
    def dec(self): 
        if self.fun >=30: 
            print("You're getting bored!")
        if self.hunger >=30: 
            print("You're getting hungry!")
        if self.health>=50: 
            print("You're low on health!")
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

Name = input("What do you call yourself, sir?")
character = Soldier(Name)

while character.living == True: 