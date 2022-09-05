import random
import time
from pprint import pprint

class champion:
    def __init__(self, cName, championMeleeAttack, championDefense, cRangeAttack, cMagic, championHealth, cMaxHealth, cLuck, cXP, cCoin):
        self.name = cName
        self.currentHealth = championHealth
        self.maxHealth = cMaxHealth
        self.xp = cXP
        self.meleeAttack = championMeleeAttack
        self.defense = championDefense
        self.luck = cLuck
        self.rangedAttack = cRangeAttack
        self.magic = cMagic
        self.coins = cCoin

    def getChampionName(self):
        return self.name
    def getCurrentHealthStat(self):
        return self.currentHealth
    def getMaxHealth(self):
        return self.maxHealth
    def getXpStat(self):
        return self.xp
    def getMeleeAttackStat(self):
        return self.meleeAttack
    def getDefenseStat(self):
        return self.defense
    def getLuckStat(self):
        return self.luck
    def getRangedAttackStat(self):
        return self.rangedAttack
    def getMagicStat(self):
        return self.magic
    def getCoinAmount(self):
        return self.coins
        
    def setChampionName(self, newName):
        self.name = newName;
    def setCurrentHealthStat(self, newCurrentHealth):
        self.currentHealth = newCurrentHealth;
    def setMaxHealth(self, newMaxHealth):
        self.maxHealth = newMaxHealth;
    def setXpStat(self, newXpStat):
        self.xp = newXpStat
    def setMeleeAttackStat(self, newMeleeAttack):
        self.meleeAttack = newMeleeAttack
    def setDefenseStat(self, newDefense):
        self.defense = newDefense
    def setLuckStat(self, newLuck):
        self.luck = newLuck
    def setRangedAttackStat(self, newRangedAttack):
        self.rangedAttack = newRangedAttack
    def setMagicStat(self, newMagic):
        self.magic = newMagic
    def setCoinAmount(self, newCoinTotal):
        self.coins = newCoinTotal

def createChampion():
    print("You slowly open your eyes and hazily look around\nMaybe picking a fight with a Giant wasn't the best idea")
    print("\nStranger: 'Hey friend. You alright? You took quite the hit. I thought you might never get up. ")
    named = input("What's your name?' ")
    confirmName = input("Stranger: 'Did you say " + named + " ? Did I hear that right?' (y/n) ")
    while confirmName != "y" and confirmName != "n":
        print("\nInvalid input")
        confirmName = input("Stranger: 'Did you say " + named + " ? Did I hear that right?' (y/n) ")
    if confirmName == "n":
        named = input("\nStranger: 'Speak up this time. What's your name?' ")
    print("Stranger: 'Nice to meet you " + named + ". You must have lost your mind picking a fight with Og. My name is Daj.'")
    time.sleep(0.2)
    print("Daj pauses and looks you up and down")
    time.sleep(0.2)
    print("\nDaj: 'I've been looking for a travelling companion. I know by that tattoo on your neck that you studied at the Erdean Academy of Combat. You seem to be wasting away in this here tavern. Why not join me and see the world?")
    classSelect = input("Did you study as a Mage(1) a Warrior(2) or Archer(3)?' ")
    while classSelect != "1" and classSelect != "2" and classSelect != "3":
        print("\nInvalid input")
        classSelect = input("Are you a Mage(1), Warrior(2), or Archer(3)? ")
    if classSelect == "1":
        championMagicBase = 100
        championMeleeBase = 25
        championDefenseBase = 50
        championRangedAttackBase = 50
    if classSelect == "2":
        championMagicBase = 0
        championMeleeBase = 125
        championDefenseBase = 75
        championRangedAttackBase = 25
    if classSelect == "3":
        championMagicBase = 0
        championMeleeBase = 50
        championDefenseBase = 50
        championRangedAttackBase = 125
    print("\nDaj: 'Now roll this dice I just want to see something...'")
    b = input("Press enter to roll Daj's Luck Dice ")
    print("\nrolling dice...")
    time.sleep(0.2)
    myLuck = random.randint(0,10)
    print("\nDaj: 'Nice! A real Erdean Academy Product. This is truly fascinating. You'll have to tell me all about it, but that can wait for the road. I'll come back at dawn and we'll set off on our journey. See you then, " + named + ".'")

    return (named, championMeleeBase, championDefenseBase, myLuck, championRangedAttackBase, championMagicBase)

class_data = createChampion()
print("\nYour Champion's Stats: ")
character = champion(class_data[0], class_data[1], class_data[2], class_data[4], class_data[5], 100, 100, class_data[3], 0, 0)

pprint(vars(character))

class enemy:
    def __init__ (self, eHealth, eAttack, ePower, eChance, eName):
        self.health = eHealth
        self.attack = eAttack
        self.power = ePower
        self.chance = eChance
        self.name = eName

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getPower(self):
        return self.power
    def getChance(self):
        return self.chance
    def getName(self):
        return self.name
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setPower(self, newPower):
        self.power = newPower
    def setChance(self, newChance):
        self.chance = newChance
    def setName(self, newName):
        self.name = newName
    
    
    
    