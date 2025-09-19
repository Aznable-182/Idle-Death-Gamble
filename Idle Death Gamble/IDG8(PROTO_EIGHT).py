#importing the modules
import random
import time
import pygame
pygame.init()

#init the class gambler (the player class)
class Gambler():
    def __init__(self):
        #Most of the attributes are self explanatory
        self._JackpotHit = False
        self._DomainExpanded = False
        #the Reach attribute is for confirming a specific scenario
        self._Reach = False
        #this is the default mp3 that will play when a jackpot is hit
        self._jackpotmp3 = pygame.mixer.Sound(r'C:\Users\ethan\OneDrive\Documents\Computing Backup\_PROJECTS\Idle Death Gamble\Music\jackpotmusicAY.mp3')
        #another default that confims specifics w/ the music
        self._music = "ay"
        #these next attributes are to do with the probibility and are all set to 0 or None by default
        self._prob = 0
        self._choice1 = None
        self._choice2 = None
        self._visualcolour1 = None
        self._visualcolour2 = None

    def taunt(self):
        print("\n'Wanna get high on my Fever?'\n")
        time.sleep(1)
        
    def DomainExpansion(self):
        #prints domain info
        time.sleep(0.5)
        print("\nᒥ領域展開ᒧ\nᒥDomain Expansionᒧ\n")
        time.sleep(1.5)
        print("ᒥ坐殺博徒ᒧ\nᒥIdle Death Gambleᒧ\n")
        #sets a flag that the domain has been expanded
        self._DomainExpanded = True
        
    def Jackpot(self):
        self.taunt()
        #sets two flags that the jackpot is hit, and afterwards, the domain should not be expanded anymore
        self._JackpotHit = True
        self._DomainExpanded = False
        #text that improves the accuracy to the source material
        time.sleep(0.7)
        print("Hakari never acquired Reverse Cursed Technique.")
        time.sleep(3.5)
        print("But...")
        time.sleep(0.5)
        print("The infinite Cursed Energy overflowing in Hakari's Body\ncaused his body to reflexively perform Reverse Cursed Technique\nin order to avoid damage.\n")
        time.sleep(10.9)
        print("In other words,\nin the 4 minutes and 11 seconds following a Jackpot,")
        time.sleep(4.1)
        print("Hakari")
        time.sleep(0.9)
        print("Is effectively")
        time.sleep(1.1)
        print("Immortal.")
        time.sleep(0.5)
        #plays the mp3 for the jackpot
        self._jackpotmp3.play()
        #resets more attributes, ready for the next domain expansion 
        DomainMenu._spincounter = 0
        DomainMenu._visualcounter = 0
        slot1._value = 1
        slot2._value = 2
        slot._value = 3
        self._playing = True
        #these are the specifics for each mp3 jackpot track
        if self._music == "tol":
            print("trippingonlove.mp3")
            time.sleep(181)
        elif self._music == "ay":
            print("admiringyou.mp3")
            time.sleep(251)
        #more lore text
        print("\n...Let's make a deal")
        time.sleep(2)
        print("Kashimo.\n")
        time.sleep(1)
        print("Kinji Hakari Truly Has Incredible Luck!!!")
        time.sleep(4)
        

    #method that rolls all of the slots, with chances of instant jackpots and reach rolls
    def rollall(self,initial,needprob,reachprob):
        self._prob = random.randint(1,1000)
        if self._prob <= needprob:
            Hakari.reachroll(random.randint(1,7),"same")
        #if the user does not get an instant jackpot, it will move down to see if they get a reach
        elif self._prob <= reachprob:
            Hakari.reachroll(random.randint(1,7),None)
        else:
            print(slot1.spin(initial))
            time.sleep(0.8)
            print(slot2.spin(initial))
            time.sleep(0.8)
            print(slot3.spin(initial))
            time.sleep(0.5)

    #method that performs a reach roll(way higher probability for jackpot)
    def reachroll(self,rig1,rig2):
        #1-1000 gives a mid range of specifics for probabilites
        self._prob = random.randint(1,1000)
        #checks if the method has been called with the parameters for an instant jackpot
        if rig2 == "same":
            rig2 = rig1
        #90% chance for a reach
        if self._prob <= 900:
            print("REACH!\n")
            time.sleep(0.8)
            print(slot1.spin(rig1))
            time.sleep(0.8)
            print(slot2.spin(rig1))
            time.sleep(1.2)
            print(slot3.spin(rig2))
            time.sleep(0.5)
        else:
            #5% chance for instant jackpot
            #27% chance for reach roll
            Hakari.rollall(None,50,270)

    #method for choosing the jackpot mp3
    def musicchoice(self):
        print("\nWhich music would you like to have for the jackpot?\n")
        time.sleep(0.5)
        self._music = input("Tripping On Love (Enter 'TOL')\nor\nAdmiring You (Enter 'AY') ")
        #normalises the input
        self._music = self._music.lower()
        if self._music == "tol":
            self._jackpotmp3 = pygame.mixer.Sound(r'C:\Users\ethan\OneDrive\Documents\Computing Backup\_PROJECTS\Idle Death Gamble\Music\jackpotmusicTOL.mp3')
            print("Music Changed\n")
        elif self._music == "ay":
            self._jackpotmp3 = pygame.mixer.Sound(r'C:\Users\ethan\OneDrive\Documents\Computing Backup\_PROJECTS\Idle Death Gamble\Music\jackpotmusicAY.mp3')
            print("Music Changed\n")

    #methods to change the probability depending on the visual effect colour
    def visualcombo(self):
        self._choice1 = DomainMenu._choicelist[0]
        self._choice2 = DomainMenu._choicelist[1]
        #checks each colour and applies each of the two choices to attributes
        if self._choice1 == "1":
            self._visualcolour1 = ReserveBall._colour
        elif self._choice1 == "2":
            self._visualcolour1 = TrainDoors._colour
        if self._choice2 == "1":
            self._visualcolour2 = ReserveBall._colour
        elif self._choice2 == "2":
            self._visualcolour2 = TrainDoors._colour

        #chances for the different colours, all but the rainbow depend on both of the colours
        if TrainDoors._colour == "Rainbow??" or ReserveBall._colour == "Rainbow??":
            #instant jackpot
            Hakari.rollall(None,1000,1000)
        if self._visualcolour1 == "Red" and self._visualcolour2 == "Red":
            #4% chance of instant jackpot
            #10% chance for a reach
            Hakari.rollall(None,4,100)
        elif self._visualcolour1 == "Red" and self._visualcolour2 == "Green" or self._visualcolour1 == "Green" and self._visualcolour2 == "Red":
            #2.5% chance for an instant jackpot
            #30% chance for a reach
            Hakari.rollall(None,25,300)
        elif self._visualcolour1 == "Green" and self._visualcolour2 == "Green":
            #6% chance for an instant jackpot
            #55% chance for a reach
            Hakari.rollall(None,60,550)
        elif self._visualcolour1 == "Green" and self._visualcolour2 == "Gold" or self._visualcolour1 == "Gold" and self._visualcolour2 == "Green":
            #13% chance for an instant jackpot
            #70% chjance for a reach
            Hakari.rollall(None,130,700)
        elif self._visualcolour1 == "Gold" and self._visualcolour2 == "Gold":
            #50% chance for an instant jackpot
            #100% chance for a reach
            Hakari.rollall(None,500,1000)      
        elif self._visualcolour1 == "Gold" and self._visualcolour2 == "Red" or self._visualcolour1 == "Red" and self._visualcolour2 == "Gold":
            #4% chance for an instant jackpot
            #38% chance for a reach
            Hakari.rollall(None,40,380)
            
Hakari = Gambler()
        
class visualEffect():
    def __init__(self,Name):
        self._name = Name
        self._colour = None
        self._grammar = None
        
    def spincolour(self):
        chance = random.randint(1,100)
        if chance <= 27:
            #27% chance for red
            self._colour = "Red"
        elif chance >= 28 and chance <= 75:
            #48% chance for green 
            self._colour = "Green"
        elif chance >= 76 <= 99:
            #24% chance for gold
            self._colour = "Gold"
        if chance == 100:
            #1% chance for rainbow
            self._colour = "Rainbow??"
        #way to alter the grammar depending on the effect
        if self._name == "Reserve Ball":
            self._grammar = "is"
        else:
            self._grammar = "are"
        time.sleep(0.5)
        DomainMenu._visualcounter = DomainMenu._visualcounter + 1
        return "\nThe " +self._name+ " " +self._grammar+ " " +self._colour+ "!\n"

ReserveBall = visualEffect("Reserve Ball")
TrainDoors = visualEffect("Train Doors")

class slot():
    def __init__(self,Value):
        self._value = Value

    #produces one spin of one of the slots
    def spin(self,rignumber):
        if rignumber != None:
            self._value = rignumber
        else:
            self._value = random.randint(1,7)
        if self._value == 1:
            namevalue = "Number One.\nYuki's Old Friend: Aya Saito!\n"
        elif self._value == 2:
            namevalue = "Number Two.\nYuki's Boss: Sayuri Amanogawa!\n"
        elif self._value == 3:
            namevalue = "Number Three.\nThe Main Heroine: Yume Asagiri!\n"
        elif self._value == 4:
            namevalue = "Number Four.\nYuki's College Classmate: Hiro Kato!\n"
        elif self._value == 5:
            namevalue = "Number Five.\nYuki's Co-Worker: Suzuka Shimuzu!\n"
        elif self._value == 6:
            namevalue = "Number Six.\nYuki's Younger Sister: Sayaka Yamaguchi!\n"
        elif self._value == 7:
            namevalue = "Number Seven.\nThe Main Hero: Yuki Yamaguchi!\n"
        DomainMenu._visualcounter = 0
        return namevalue
    
slot1 = slot(1)
slot2 = slot(2)
slot3 = slot(3)
    
class Menu():
    def __init__(self):
        self._bmchoice = None
        self._spincounter = 0
        self._visualcounter = 0
        self._choicelist = []
        self._imchoice = None
        self._mchoice = None
        
    def visualdecision(self):
        #checcks if the program should spin the slots, or grant an instant jackpot
        (self._choicelist).append(self._mchoice)
        time.sleep(1)
        if self._visualcounter == 2 and self._spincounter == 5:
            Hakari.reachroll(random.randint(1,7),"same")
            self._choicelist = []
        if self._visualcounter == 2:
            Hakari.visualcombo()
            self._spincounter = self._spincounter + 1
            self._choicelist = []
            if slot1._value == slot2._value and slot2._value == slot3._value:
                Hakari.Jackpot()
            

    def MenuChoice(self):
        #asks for a visual effect to produce then spins the related specific
        if slot1._value == slot2._value and slot2._value == slot3._value:
            Hakari.Jackpot()
        self._mchoice = input("What do you do?\nEnter 1 to throw a Reserve Ball\nEnter 2 to use the Train Doors ")
        if self._mchoice == "1":
            print(ReserveBall.spincolour())
            DomainMenu.visualdecision()
        elif self._mchoice == "2":
            print(TrainDoors.spincolour())
            DomainMenu.visualdecision()
        elif self._mchoice == "Leave" or self._mchoice == "leave":
            DomainMenu._spincounter = 0
            DomainMenu._visualcounter = 0
            slot1._value = 1
            slot2._value = 2
            slot._value = 3
            DomainMenu.initialmenu()

    def BattleMenu(self):
        #grants more user interaction with this menu 
        self._bmchoice = input("\nYou have to fight!\nExpand your domain? (y/n)")
        if self._bmchoice == "y":
            time.sleep(0.5)
            Hakari.DomainExpansion()
            time.sleep(1)
            DomainMenu.MenuChoice()
        else:
            quit()
            
    def initialmenu(self):
        #the beginning message that gives the user the options they need
        print("Welcome to Hakari Domain Simulator")
        time.sleep(0.5)
        self._imchoice = input("\nEnter 1 to start the Sim\nEnter 2 to access settings\nEnter 3 to Quit ")
        if self._imchoice == "1":
            time.sleep(0.5)
            print("When the 'What do you do' Menu is shown, type 'Leave' to return to this menu (Resets to start of sim)")
            DomainMenu.BattleMenu()
        if self._imchoice == "2":
            time.sleep(0.5)
            Hakari.musicchoice()
        if self._imchoice == "3":
            quit()
                
DomainMenu = Menu()
    
def main():
    DomainMenu.initialmenu()
    while Hakari._DomainExpanded == True:
        DomainMenu.MenuChoice()
while True == True:
    main()

