#D&D combat program will run simulated combat for basic D&D type game.
import os
import math
import random

#set function for basic roll
def roll(modifier):
    return random.randrange(1,20)+modifier


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
        initiative = roll(self.ini)
        return initiative

    #set function for attack. If the attack is successful, will call to roll damage.  If unsucessful pass turn.
    def roll_attack(self, defender):
        attack = roll(self.atk)
        print(self.name, "attacks: ", attack)
        if attack >= defender.ac:
            print("Hit")
            return True
        else:
            print("Miss")
            return False
    
    #set function for rolling damage.Print out damage total and deduct from creature's HP
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

#function to call attack sequence.  If an attach meets or beats the opponen't ac roll for damage and check to see if the defender lived.
def attack(attacker, defender):
    if attacker.roll_attack(defender) == True:
        attacker.roll_damage(defender)
        death_check(defender)

def initiative(creature):
    return creature.roll_initiative(roll_initiative(self.ini))

#create list of creatures to do combat
creatures = [creature('Dragon', 90, 20, 10, 15, 1, 'knight'),
             creature('Knight', 45, 25, 10, 8, 4,'dragon'),
             creature('Squire', 25, 15, 8, 8, 6,'dragon')]

def getCreature():
    return creature.initiative

sorted(creatures, key=getCreature())

#Combat sequence
turn = 0
while dragon.hp > 0 and knight.hp > 0:
    turn = turn + 1
    print("Turn", turn)
    for i in range(len(combatants)):
        if creature[i].hp > 0:
            attack(combatants[i], combatants[i].opponent)
        else:
            break
    print()
