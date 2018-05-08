#D&D combat program will run simulated combat for basic D&D type game.
import os
import math
import random

from operator import itemgetter, attrgetter

global monters
monsters = []
global heroes
heroes = []

#set function for basic roll expected to pass object modifier as arguement
def roll(modifier):
    return random.randrange(1,20) + modifier

#create a creature class that will hold a name, hit points, armor class, attack modifier, damage maximium, and initiative

class creature():
    def __init__(self,name, hp, ac, atk, dmg, ini, ct):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.atk = atk
        self.dmg = dmg
        self.ini = ini
        self.creatureType = ct
        self.initiative = roll(ini)
        

    #function to get Name attribute
    def get_name(self):
        return self.name

    #representation of object
    def __repr__(self):
        return '{} Name:{} HP:{} Attack:{} Damage{}\n'.format(self.creatureType, self.name, self.hp, self.atk, self.dmg)

    #function to call attack sequence.  If an attach meets or beats the opponen't ac roll for damage and check to see if the defender lived.
    def attack(self, defender):

        #set function for attack. If the attack is successful, will call to roll damage.  If unsucessful pass turn.
        def roll_attack(self, defender):
            attack = roll(self.atk)
            print(self.name, "attacks", defender.name)
            if attack >= defender.ac:
                return True
            else:
                print("Miss")
                return False

        #set function for rolling damage.Print out damage total and deduct from creature's HP
        def roll_damage(self, defender):
            damage = random.randrange(1,self.dmg)
            print(self.name, "deals", damage, "damage!")
            defender.hp = defender.hp - damage
            death_check(defender)

        #function to make sure neither of the combatants died with the last attack
        def death_check(defender):
            if defender.hp <= 0:
                if defender.creatureType == "monster":
                    global monsters
                    print("The", defender.get_name(), " is vanquished!")
                    global teamMonsters
                    teamMonsters = teamMonsters - 1
                    print(teamMonsters, "monsters remain")
                else:
                    global heroes
                    print("Our ", defender.get_name(), ' has perished.')
                    global teamHeroes
                    teamHeroes = teamHeroes - 1
                    print(teamHeroes, "heroes remain")
                print()
            else:
                print(defender.name, "HP: ", defender.hp)

        if roll_attack(self, defender) == True:
            roll_damage(self, defender)

    #function to create initiative score for creature
    def roll_initiative():
        self.initiativeScore = roll(self.ini)

#create list of creatures to do combat: name, hp, ac, atk, dmg, ini, ct
creatures = [
            creature('Frick', 35, 20, 10, 15, 1, 'monster'),
            creature('Frack', 35, 20, 10, 15, 1, 'monster'),
            creature('Frook', 35, 20, 10, 15, 1, 'monster'),
            creature('Knight',35, 20, 10, 15, 1, 'hero'),
            creature('Squire', 35, 20, 10, 15, 1, 'hero'),
            creature('Fighter', 35, 20, 10, 15, 1, 'hero')
            ]

def getInitiative(l):
    for c in range(len(l)):
        return int(l[c].initiative)
    
for i in range(len(creatures)):
    if creatures[i].creatureType == 'monster':
        monsters.append(creatures[i])
    elif creatures[i].creatureType == 'hero':
        heroes.append(creatures[i])
          
print(monsters)
print(heroes)
print()

#Combat sequence
teamMonsters = len(monsters)
teamHeroes = len(heroes)
turn = 0
while teamMonsters > 0 and teamHeroes > 0:
    print('------------------------------------------')
    turn = turn + 1
    print("Turn:", turn)

    #create sequence for initiative
    for i in range(len(creatures)):
        creatures[i].initiative = roll(creatures[i].ini)
    combatSequence = sorted(creatures, key = attrgetter('initiative'), reverse = True)

    #print out the initiative list of current participants
    for p in range(len(combatSequence)):
        if creatures[p].hp > 0:
            print(creatures[p].name, creatures[p].initiative)
    print()

    #run combat loop for combatants
    for i in range(len(combatSequence)):
        #check to see if character is alive to attack
        if combatSequence[i].hp > 0:
            #select opponent who doesn't share the same creatureType and is still alive
            for o in range(len(creatures)):
                if creatures[o].creatureType != combatSequence[i].creatureType and creatures[o].hp > 0:
                    #call attack function and move on to next participant.
                    combatSequence[i].attack(creatures[o])
                    break

    #set victory terms and break from comabt loop
    if teamMonsters == 0:
        print("The day has been won.  Hip Hip Hooray!")
        print()
        print(heroes)
        break
    elif teamHeroes == 0:
        print("All of our heros have follen.  Run you fool!")
        print()
        print(monsters)
        break

#End program
