#D&D combat program will run simulated combat for basic D&D type game.
import os
import math
import random

#set function for basic roll
def roll():
    return random.randrange(1,20)

class creature():
    def __init__(self, name, hp, ac, atk, dmg, ini, role):
        self.name = name
        self.role = role
        self.hp = hp
        self.ac = ac
        self.atk = atk
        self.dmg = dmg
        self.ini = roll() + ini

    def __repr__(self):
        return repr((self.name, self.hp, self.ac, self.ini, self.atk, self.dmg))
    
    #set function for attack. Use variable for attack roll 
    def roll_attack(self, ac):
        attack = roll() + self.atk
        if attack - self.atk == 20:
            return "Crit"
        elif attack >= ac:
            return True
        else:
            return False
        return attack
    
    #set function for rolling damage
    def roll_damage(self):
       damage = random.randrange(1,self.dmg)
       print(damage, " Damage")
       return damage

dragon = creature("Dragon", 90, 20, 10, 15, 1, False)
knight = creature("Knight", 45, 25, 10, 8, 3, True)
squire = creature("Squire", 25, 20, 8, 8, 6, True)

#Create combat sequence.

#select combatants for simulation
combatant = [dragon, knight, squire]

#Initiative module
sorted(combatant, key=lambda creature: creature.ini)
print(combatant)

turn = 1
#Continue combat until the dragon or the knight is down to 0 HP
while dragon.hp > 0 and knight.hp > 0:


    for i in combatant:
        if combatant[i] == knight:
            #Knight's attack turn
            print(knight.name, " attacks")
            if knight.roll_attack(dragon.ac) == "Crit":
                print("Critical Hit!")
                dragon.hp = dragon.hp - knight.dmg
            elif knight.roll_attack(dragon.ac) == True:
                print("Hit")
                dragon.hp = dragon.hp - knight.roll_damage()
            else:
                print("Miss")

            #Squire's attack turn
            print(squire.name, " attacks")        
            if squire.roll_attack(dragon.ac) == "Crit":
                print("Critical Hit")
                dragon.hp = dragon.hp - squire.dmg
            elif squire.roll_attack(dragon.ac) == True:
               dragon.hp = dragon.hp - squire.roll_damage()
               print("Dragon HP:  ", dragon.hp)
            else:
                print("Miss")

            if combatant[i] == dragon:
            #Dragon's attack turn
                print(dragon.name, " attacks")        
                if dragon.roll_attack(dragon.ac) == "Crit":
                    knight.hp = knight.hp - dragon.dmg
                elif dragon.roll_attack(knight.ac) == True:
                    knight.hp = knight.hp - dragon.roll_damage()
                    print("Knight HP:  ", knight.hp)
                else:
                    print("Miss")
    
    turn = turn + 1
    if dragon.hp <= 0:
        print("The dragon is vanquished!")
    elif knight.hp <=0:
        print("Our knight has fallen.  Run you fools!")
print(turn)
