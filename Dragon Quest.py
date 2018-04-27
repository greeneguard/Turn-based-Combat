#D&D combat program will run simulated combat for basic D&D type game.
import os
import math
import random

#set function for basic roll
def roll():
    return random.randrange(1,20)


class creature():
    def __init__(self,name, hp, ac, atk, dmg, ini, opponent):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.atk = atk
        self.dmg = dmg
        self.ini = ini
        self.opponent = opponent
        self.initiative = 0

    #representation of object
    def __repr__(self):
        return '({} {} {} {} {})'.format(self.name, self.hp, self.atk, self.dmg, self.ini)

    #set function to roll for initiative
    def roll_initiative(self):
        initiative = roll() + self.ini
        return initiative

    #set function for attack. Use variable for attack roll 
    def roll_attack(self, defender):
        attack = roll() + self.atk
        print(self.name, "attacks: ", attack)
        if attack >= defender.ac:
            print("Hit")
            return True
        else:
            print("Miss")
            return False
    
    #set function for rolling damage
    def roll_damage(self, defender):
       damage = random.randrange(1,self.dmg)
       print(self.name, "deals", damage, "damage!")
       defender.hp = defender.hp - damage

#function to make sure neither of the combatants died with the last attack
def death_check(defender):
    if defender.hp <= 0:
        if defender == dragon:
            print("The dragon is vanquished!")
        else:
            print("Our hero has perished.  Run you fools!")
        return False
    else:
        print(defender.name, "HP: ", defender.hp)
        return True

def attack(attacker, defender):
    if attacker.roll_attack(defender) == True:
        attacker.roll_damage(defender)
        death_check(defender)

def initiative(creature):
    return creature.initiative()

dragon = creature('Dragon', 90, 20, 10, 15, 1, 'opp')
knight = creature('Knight', 45, 25, 10, 8, 4,'opp')
squire = creature('Squire', 25, 15, 8, 8, 6,'opp')

combatant = [dragon, knight, squire]

dragon.opponent = knight
knight.opponent = dragon
squire.opponent = dragon

print(len(combatant))
print(combatant)

#Combat sequence
turn = 0
while dragon.hp > 0 and knight.hp > 0:
    turn = turn + 1

#    for i in range(len(combatant)):
#        combatant[i].initiative = combatant[i].roll_initiative
        
    combatants = sorted(combatant, key=lambda combatant: combatant.initiative)
    for i in range(len(combatants)):
        attack(combatants[i], combatants[i].opponent)
        
print(turn)
