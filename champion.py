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
val = False
ville = False
mtn = False
cavo = False
myLuck = 0
end = False

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
    global myLuck
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
    
    return (named, championMeleeBase)

class_data = createChampion()
print("\nYour Champion's Stats: ")
character = champion(class_data[0], class_data[1], 500, 15*myLuck)

pprint(vars(character))

class enemy:
    def __init__ (self, eHealth, eAttack, eName):
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

def enemyGen(levelBoss, EnemyName):
    name = EnemyName
    if levelBoss == False:
        health = random.randint(50,350)
        attack = random.randint(20, 50)
        return enemy(health, attack, name)
    else:
        health = random.randint(200,600)
        attack = random.randint(150, 300)
        return enemy(health, attack, name)
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

bossOpp = enemyGen(True, 'Goblin Chief')
def endFight():
    print("You have found all 4 keys noted on Daj's map. You turn the map over and find a small scribble in the bottom left corner. It reads 'YOU MUST DEFEAT THE GOBLIN CHIEF BEFORE HE DESTROYS THE WORLD'")
    print("So the Goblin Chief is the evil mastermind. Time to face him. You head to the Chief's Palace.")
    time.sleep(1.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".\n")
    print("You arrive at the Palace. You see the Goblin Chief standing with some Goblin Patrollers. ")
    time.sleep(0.3)
    print(str(character.getChampionName())+": Goblin Chief! It's time for for you stop your evil plan or I'll have to stop it for you.")
    time.sleep(0.3)
    print("Goblin Chief: Stop my plan? You and what army? I don't even know you.")
    time.sleep(0.3)
    print(str(character.getChampionName())+": You may not know me now but you will.")
    time.sleep(0.3)
    print("Goblin Chief: You'll have to defeat me in battle to stop me, peasant.")
    time.sleep(0.3)
    print(str(character.getChampionName())+": Very well. It's time to battle!")
    endBattle()
    print("With the Goblin Chief defeated the Goblin's recognize you as their leader now. You live out your days ruling fairly a nd justly and make peace with the surrounding villages.")
    print("final stats:")
    pprint(vars(character))
    print("THE END")
    time.sleep(1.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".\n")
    print("THANKS FOR PLAYING")
    print("░██╗░░░░░░░██╗░█████╗░░██████╗████████╗██╗███╗░░██╗░██████╗░  ██╗░░██╗███████╗██████╗░░█████╗░")
    print("░██║░░██╗░░██║██╔══██╗██╔════╝╚══██╔══╝██║████╗░██║██╔════╝░  ██║░░██║██╔════╝██╔══██╗██╔══██╗")
    print("░╚██╗████╗██╔╝███████║╚█████╗░░░░██║░░░██║██╔██╗██║██║░░██╗░  ███████║█████╗░░██████╔╝██║░░██║")
    print("░░████╔═████║░██╔══██║░╚═══██╗░░░██║░░░██║██║╚████║██║░░╚██╗  ██╔══██║██╔══╝░░██╔══██╗██║░░██║")
    print("░░╚██╔╝░╚██╔╝░██║░░██║██████╔╝░░░██║░░░██║██║░╚███║╚██████╔╝  ██║░░██║███████╗██║░░██║╚█████╔╝")
    print("░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░")
    
def endBattle():
    global end
    playerDamaged = 0
    oppDamaged = 0
    while (playerDamaged < character.getHealth()) and (bossOpp.getHealth() > oppDamaged):
        oppDamaged += character.getMeleeAttackStat()
        print("You did " + str(character.getMeleeAttackStat()) + " points of damage")
        print("Goblin Patrol now has " + str(bossOpp.getHealth() - oppDamaged) + " health points")
        if oppDamaged >= bossOpp.getHealth():
            print("You defeated the Goblin Chief!")
            print("+1500 Coins!")
            character.setCoinAmount(character.getCoinAmount() + 1500)  
            end = True
            return
        playerDamaged += bossOpp.getAttack()
        print("Enemy did " + str(bossOpp.getAttack()) + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            endBattle()

def caveBattle():
    global keyCount
    global cavo
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
            cavo = True
            keyCount+=1
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
            mtn = True
            keyCount+= 1
            return
        playerDamaged += gobPatrol2.getAttack()
        print("Enemy did " + str(gobPatrol2.getAttack()) + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            mtnBattle()
def villageBattle():
    global keyCount
    global ville
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
            keyCount+= 1
            ville = True
            return
        playerDamaged += gobPatrol3.getAttack()
        print("Enemy did " + str(gobPatrol3.getAttack()) + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            villageBattle()
def valleyBattle():
    global val
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
            val = True
            keyCount+= 1
            return
        playerDamaged += gobPatrol4.getAttack()
        print("Enemy did " + str(gobPatrol4.getAttack()) + " points of damage")
        print("You now have " + str(character.getHealth() - playerDamaged) +" health points")
        if playerDamaged >= character.getHealth():
            print("You were defeated but your drink a potion before your eyes close...")
            character.setHealthStat(character.getHealth() + 50)
            character.setMeleeAttackStat(character.getMeleeAttackStat() + 50)
            valleyBattle()
        
def cave():
    global keyCount
    global end
    if (end == True and keyCount == 4):
        return
    print("You reach the cave")
    stayOrLeave = input("Explore cave(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore cave(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        sequence2()
    if stayOrLeave == "1":
        print("You venture deeper into the cave. You hear voices as you turn a corner and run into a patrol of goblins. Time to fight")
        caveBattle()
        print("You found a key in the satchel of one of the Goblins. You now have " + str(keyCount) + " keys")
        if keyCount == 4:
            endFight()
            return
        sequence2()
def mountain():
    #to do
    global keyCount
    global end
    if (end == True and keyCount == 4):
        return
    print("You reach the top of the mountain")
    stayOrLeave = input("Explore mountain(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore mountain(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        sequence2()
    if stayOrLeave == "1":
        print("You climb up the mountain. As you reach the top you realize it's a Goblin Outpost. Time to fight")
        mtnBattle()
        print("You found a key in the hands of one of the Goblins. You now have " + str(keyCount) + " keys")
        if keyCount == 4:
            endFight()
            return
        sequence2()

def village():
    #todo
    global keyCount
    global end
    if (end == True and keyCount == 4):
        return
    print("You arrive at a village")
    stayOrLeave = input("Explore village(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore village(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        sequence2()
    if stayOrLeave == "1":
        print("You arrive at the village. Goblin Soldiers start yelling at you at the gates. Time to fight")
        villageBattle()
        print("You found a key in the pocket of one of the Goblins. You now have " + str(keyCount) + " keys")
        if keyCount == 4:
            endFight()
            return
        sequence2()
def valley():
    global keyCount
    global end
    if (end == True and keyCount == 4):
        return
    print("You reach the valley")
    stayOrLeave = input("Explore valley(1) or go somewhere else(2)? ")
    while stayOrLeave != "1" and stayOrLeave != "2":
        print("Invalid input. try again")
        stayOrLeave = input("Explore valley(1) or go somewhere else(2)? ")
    if stayOrLeave == "2":
        sequence2()
    if stayOrLeave == "1":
        print("You travel to the valley. You hear leaves rustling. It's a trap! Time to fight")
        valleyBattle()
        print("You found a key in the canteen of one of the Goblins. You now have " + str(keyCount) + " keys")
        if keyCount == 4:
            endFight()
            return
        sequence2()

def sequence2():
    global cavo
    global ville
    global mtn
    global val
    global keyCount
    global end
    if end == True and keyCount == 4:
        return
    escape = input("Where will you go? Cave(1) or Mountain(2) or Village(3) or Valley(4) ")
    while escape != '1' and escape != '2' and escape != '3' and escape != '4':
        print("Invalid input. Try Again")
        escape = input("Hide! Where will you go? Cave(1) or Hill(2) or Village(3) or Valley(4) ")
    if escape == '1':
        if (cavo == True):
            print("You already got the key from the cave. Pick another place")
            sequence2()
        cave()
    if escape == '2':
        if (mtn == True):
            print("You already got the key from the mountain. Pick another place")
            sequence2()
        mountain()
    if escape == '3':
        if (ville == True):
            print("You already got the key from the cave. Pick another place")
            sequence2()
        village()
    if escape == '4':
        if (val == True):
            print("You already got the key from the cave. Pick another place")
            sequence2()
        valley()
sequence2()

