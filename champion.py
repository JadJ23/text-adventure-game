from operator import truediv
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

keyCount = 0
valley = False
village = False
mtn = False
cave = False

class champion:
    def __init__(self, cName, championMeleeAttack, championHealth, cCoin):
        self.name = cName
        self.health = championHealth
        self.meleeAttack = championMeleeAttack
        self.coins = cCoin

    def getChampionName(self):
        return self.name
    def getMeleeAttackStat(self):
        return self.meleeAttack
    def getHealth(self):
        return self.health
    def getCoinAmount(self):
        return self.coins
        
    def setChampionName(self, newName):
        self.name = newName;
    def setHealthStat(self, newCurrentHealth):
        self.health = newCurrentHealth
    def setMeleeAttackStat(self, newMeleeAttack):
        self.meleeAttack = newMeleeAttack
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
        championMeleeBase = 150
    if classSelect == "2":
        championMeleeBase = 150
    if classSelect == "3":
        championMeleeBase = 150
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
    
    return (named, championMeleeBase)

class_data = createChampion()
print("\nYour Champion's Stats: ")
character = champion(class_data[0], class_data[1], 500, 0)

pprint(vars(character))

class enemy:
    def __init__ (self, eHealth, eAttack, ePower, eChance, eName):
        self.health = eHealth
        self.attack = eAttack
        self.name = eName    
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getName(self):
        return self.name
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setName(self, newName):
        self.name = newName

class bossEnemy (enemy):
    def __init__ (self, eHealth, eAttack, eName):
        super().__init__(eHealth, eAttack, eName)

def enemyGen(levelBoss, EnemyName):
    name = EnemyName
    if levelBoss == False:
        health = random.randint(50,350)
        attack = random.randint(20, 50)
        power = random.randint(10,30)
        chance = random.randint(1,10)
        return enemy(health, attack, power, chance, name)
    else:
        health = random.randint(200,600)
        attack = random.randint(75, 150)
        power = random.randint(35, 55)
        chance = random.randint(3,10)
        superMove = random.randint(100, 200)
        return bossEnemy(health, attack, power, chance, name, superMove)
gobPatrol = enemyGen(False, 'Goblin Patrol')
gobPatrol2 = enemyGen(False, 'Goblin Patrol')
gobPatrol3 = enemyGen(False, 'Goblin Patrol')
gobPatrol4 = enemyGen(False, 'Goblin Patrol')
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
    print("You look at the map Daj gave you. You recognize the area. You're deep in Goblin territory. There are X's in 4 locations.")

        
sequence1()
def leaveLocation():
    explore = input("Do you want to explore the cave(1) or the mountain(2) or the village(3) or the valley(4)? ")
    while explore != '1' and explore != '2' and explore != '3' and explore != '4':
        print("Invalid input. Try Again")
        explore = input("Hide! Where will you go? Cave(1) or Hill(2) or Village(3) or Valley(4) ")
    if explore == '1':
        print("You head towards a cave")
        cave()
    if explore == '2':
        print("You head towards a mountain")
        mountain()
    if explore == '3':
        print("You head towards a village")
        village()
    if explore == '4':
        print("You head towards a valley")
        valley()

def endFight():
    print("at boss fight")
    #todo boss batlle and finale
    return

def caveBattle():
    global keyCount
    global cave
    playerDamaged = 0
    oppDamaged = 0
    while (playerDamaged < character.getHealth()) and (gobPatrol.getHealth() > oppDamaged):
        oppDamaged += character.getMeleeAttackStat()
        print("You did " + str(character.getMeleeAttackStat()) + " points of damage")
        print("Goblin Patrol now has " + str(gobPatrol.getHealth() - oppDamaged) + " health points")
        if oppDamaged >= gobPatrol.getHealth():
            print("You defeated the enemy!")
            print("+50 Coins!")
            character.setCoinAmount(character.getCoinAmount() + 50)
            return
        playerDamaged += gobPatrol.getAttack()
        print("Enemy did " + str(gobPatrol.getAttack()) + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            caveBattle()
def mtnBattle():
    global keyCount
    global mtn
    playerDamaged = 0
    oppDamaged = 0
    while (playerDamaged < character.getHealth()) and (gobPatrol2.getHealth() > oppDamaged):
        oppDamaged += character.getMeleeAttackStat()
        print("You did " + str(character.getMeleeAttackStat()) + " points of damage")
        print("Goblin Patrol now has " + str(gobPatrol2.getHealth() - oppDamaged) + " health points")
        if oppDamaged >= gobPatrol2.getHealth():
            print("You defeated the enemy!")
            print("+50 Coins!")
            character.setCoinAmount(character.getCoinAmount() + 50)
            return
        playerDamaged += gobPatrol2.getAttack()
        print("Enemy did " + gobPatrol2.getAttack() + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            mtnBattle()
def villageBattle():
    global keyCount
    global village
    playerDamaged = 0
    oppDamaged = 0
    while (playerDamaged < character.getHealth()) and (gobPatrol3.getHealth() > oppDamaged):
        oppDamaged += character.getMeleeAttackStat()
        print("You did " + str(character.getMeleeAttackStat()) + " points of damage")
        print("Goblin Patrol now has " + str(gobPatrol3.getHealth() - oppDamaged) + " health points")
        if oppDamaged >= gobPatrol3.getHealth():
            print("You defeated the enemy!")
            print("+50 Coins!")
            character.setCoinAmount(character.getCoinAmount() + 50)
            return
        playerDamaged += gobPatrol3.getAttack()
        print("Enemy did " + gobPatrol3.getAttack() + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            villageBattle()
def valleyBattle():
    global valley
    global keyCount
    playerDamaged = 0
    oppDamaged = 0
    while (playerDamaged < character.getHealth()) and (gobPatrol4.getHealth() > oppDamaged):
        oppDamaged += character.getMeleeAttackStat()
        print("You did " + str(character.getMeleeAttackStat()) + " points of damage")
        print("Goblin Patrol now has " + str(gobPatrol4.getHealth() - oppDamaged) + " health points")
        if oppDamaged >= gobPatrol4.getHealth():
            print("You defeated the enemy!")
            print("+50 Coins!")
            character.setCoinAmount(character.getCoinAmount() + 50)
            return
        playerDamaged += gobPatrol4.getAttack()
        print("Enemy did " + gobPatrol4.getAttack() + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            valleyBattle()
        
def cave():
    global keyCount
    print("You reach the cave")
    stayOrLeave = input("Explore cave(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore cave(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        leaveLocation()
    if stayOrLeave == "1":
        print("You venture deeper into the cave. You hear voices as you turn a corner and run into a patrol of goblins. Time to fight")
        caveBattle()
        keyCount += 1
        print("You found a key in the satchel of one of the Goblins. You now have " + str(keyCount) + " keys")
        cave = True
        if keyCount == 4:
            endFight()
        sequence2
def mountain():
    #to do
    global keyCount
    print("You reach the top of the mountain")
    stayOrLeave = input("Explore mountain(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore mountain(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        leaveLocation()
    if stayOrLeave == "1":
        print("You venture deeper into the cave. You hear voices as you turn a corner and run into a patrol of goblins. Time to fight")
        mtnBattle()
        keyCount += 1
        mtn = True
        print("You found a key in the hands of one of the Goblins. You now have " + str(keyCount) + " keys")
        if keyCount == 4:
            endFight()
        sequence2()

def village():
    #todo
    global keyCount
    print("You arrive at a village")
    stayOrLeave = input("Explore village(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore village(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        leaveLocation()
    if stayOrLeave == "1":
        print("You venture deeper into the cave. You hear voices as you turn a corner and run into a patrol of goblins. Time to fight")
        villageBattle()
        keyCount += 1
        print("You found a key in the pocket of one of the Goblins. You now have " + str(keyCount) + " keys")
        village = True
        if keyCount == 4:
            endFight()
        sequence2()
def valley():
    global keyCount
    print("You reach the valley")
    stayOrLeave = input("Explore valley(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore valley(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        leaveLocation()
    if stayOrLeave == "1":
        print("You venture deeper into the cave. You hear voices as you turn a corner and run into a patrol of goblins. Time to fight")
        valleyBattle()
        keyCount += 1
        print("You found a key in the canteen of one of the Goblins. You now have " + str(keyCount) + " keys")
        valley = True
        if keyCount == 4:
            endFight()
        sequence2()

def sequence2():
    global cave
    global village
    global mtn
    global valley
    escape = input("Where will you go? Cave(1) or Mountain(2) or Village(3) or Valley(4) ")
    while escape != '1' and escape != '2' and escape != '3' and escape != '4':
        print("Invalid input. Try Again")
        escape = input("Hide! Where will you go? Cave(1) or Hill(2) or Village(3) or Valley(4) ")
    if escape == '1':
        if (cave == True):
            print("You already got the key from the cave. Pick another place")
            sequence2()
            return
        print("You head towards a cave")
        cave()
    if escape == '2':
        if (mtn == True):
            print("You already got the key from the mountain. Pick another place")
            sequence2()
            return
        print("You head towards a mountain")
        mountain()
    if escape == '3':
        if (village == True):
            print("You already got the key from the cave. Pick another place")
            sequence2()
            return
        print("You head towards a village")
        village()
    if escape == '4':
        if (valley == True):
            print("You already got the key from the cave. Pick another place")
            sequence2()
            return
        print("You head towards a valley")
        valley()
sequence2()

