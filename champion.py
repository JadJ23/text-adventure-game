import random
import time
from pprint import pprint

print("░██╗░░░░░░░██╗░█████╗░░██████╗████████╗██╗███╗░░██╗░██████╗░  ██╗░░██╗███████╗██████╗░░█████╗░")
print("░██║░░██╗░░██║██╔══██╗██╔════╝╚══██╔══╝██║████╗░██║██╔════╝░  ██║░░██║██╔════╝██╔══██╗██╔══██╗")
print("░╚██╗████╗██╔╝███████║╚█████╗░░░░██║░░░██║██╔██╗██║██║░░██╗░  ███████║█████╗░░██████╔╝██║░░██║")
print("░░████╔═████║░██╔══██║░╚═══██╗░░░██║░░░██║██║╚████║██║░░╚██╗  ██╔══██║██╔══╝░░██╔══██╗██║░░██║")
print("░░╚██╔╝░╚██╔╝░██║░░██║██████╔╝░░░██║░░░██║██║░╚███║╚██████╔╝  ██║░░██║███████╗██║░░██║╚█████╔╝")
print("░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░")
time.sleep(0.5)
print("How to play: You will receive prompts with options. To select the option you would like type the corresponding input exactly as shown. I hope you enjoy it!")
time.sleep(1.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".\n")
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
    time.sleep(0.3)
    print("\nStranger: Hey friend. You alright? You took quite the hit. I thought you might never get up. ")
    named = input("What's your name? ")
    confirmName = input("Stranger: Did you say " + named + " ? Did I hear that right? (y/n) ")
    while confirmName != "y" and confirmName != "n":
        print("\nInvalid input")
        confirmName = input("Stranger: Did you say " + named + " ? Did I hear that right?' (y/n) ")
    if confirmName == "n":
        named = input("\nStranger: You best speak up this time. What's your name, friend? ")
    print("Stranger: Nice to meet you " + named + ". You must have lost your mind picking a fight with Og. My name is Daj.")
    time.sleep(0.3)
    print("*Daj pauses and looks you up and down*")
    time.sleep(0.5)
    print("\nDaj: I've been looking for a travelling companion. I know by that tattoo on your neck that you studied at the Erdean Academy of Combat. You seem to be wasting away in this here tavern. Why not join me and see the world?")
    classSelect = input("Did you study as a Mage(1) a Warrior(2) or Archer(3)? ")
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
    print("\nDaj: Now roll this dice I just want to see something...")
    b = input("Press enter to roll Daj's Luck Dice ")
    print("\nrolling dice...")
    time.sleep(0.3)
    myLuck = random.randint(0,10)
    print("\nDaj: Nice! A real Erdean Academy Product. This is truly fascinating. You'll have to tell me all about it, but that can wait for the road. I'll come back at dawn and we'll set off on our journey. See you then, " + named + ".")
    time.sleep(0.5)
    print("\n*Daj hands you a coin purse and nods before walking out of the tavern*")
    time.sleep(0.5)
    print("\n+50 coins!")
    
    return (named, championMeleeBase, championDefenseBase, myLuck, championRangedAttackBase, championMagicBase)

class_data = createChampion()
print("\nYour Champion's Stats: ")
character = champion(class_data[0], class_data[1], class_data[2], class_data[4], class_data[5], 100, 100, class_data[3], 0, 50)

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

class bossEnemy (enemy):
    def __init__ (self, eHealth, eAttack, ePower, eChance, eName, bossSuper):
        super().__init__(eHealth, eAttack, ePower, eChance, eName)
        self.super = bossSuper

    def getSuper(self):
        return self.super
    def setSuper(self, newSuper):
        self.super = newSuper

def enemyGen(levelBoss, EnemyName):
    name = EnemyName
    if levelBoss == False:
        health = random.randint(50,150)
        attack = random.randint(20, 100)
        power = random.randint(10,30)
        chance = random.randint(1,10)
        return enemy(health, attack, power, chance, name)
    else:
        health = random.randint(200,500)
        attack = random.randint(100, 200)
        power = random.randint(35, 55)
        chance = random.randint(3,10)
        superMove = random.randint(100, 200)
        return bossEnemy(health, attack, power, chance, name, superMove)
# en1 = enemyGen(False, 'Goblin')
# pprint(vars(en1))
def sequence1():
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(0.7)
    print("\nYou wake the next morning to the sound of horses neighing and cows mooing\nYou feel around and grab a handful of hay. You're in a barn. Some night you had")
    print("\nDaj: Oh there you are my friend! Were you sleeping in the barn? Never mind that. We've got a journey ahead of us and we better get going.")
    print("*You splash your face with water and head out with Daj*")
    time.sleep(1.0)
    print("It's been a while since you've left the barn but it's been silent the whole trek. Daj has been acting weird. He seems paranoid.")
    print("Daj: I must tell you that these parts are dangerous. You must be on alert, for your sake and mine.")
    print("You: Would've been nice to know before we got here. I'll keep a lookout, don't worry.")
    time.sleep(1.0)
    print("BOOOOOODAAAABOOOOOOOOOOO\nThe sound of a horn. You've heard it before, it's a siren used by Goblins for intruders. It must be for you and Daj")
    print("You: Daj! Quick we've got to go befo-")
    time.sleep(0.5)
    print("You look over at Daj. He's looking down at his chest. An arrow gleams in sunlight, fresh with blood. He reaches in his pocket and hands you a map.")
    print("Daj: You must... find it. Protect it with... your life. Go now. GO!")
    print("*You grab the map and look at Daj before darting away*")
    time.sleep(0.5)

sequence1()

def cave():
    #to do
    print("You reach the cave")

def mountain():
    #to do
    print("You reach the top of the mountain")

def village():
    #todo
    print("You arrive at a village")

def valley():
    #todo
    print("You reach the valley")

def sequence2():
    escape = input("Hide! Where will you go? Cave(1) or Mountain(2) or Village(3) or Valley(4) ")
    while escape != '1' and escape != '2' and escape != '3' and escape != '4':
        print("Invalid input. Try Again")
        escape = input("Hide! Where will you go? Cave(1) or Hill(2) or Village(3) or Valley(4) ")
    if escape == '1':
        print("You head towards a cave")
        cave()
    if escape == '2':
        print("You head towards a mountain")
        mountain()
    if escape == '3':
        print("You head towards a village")
        village()
    if escape == '4':
        print("You head towards a valley")
        valley()
sequence2()
