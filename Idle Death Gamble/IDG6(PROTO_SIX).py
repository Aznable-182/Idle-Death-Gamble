import random
import time
import pygame
pygame.init()

class Gambler():
    def __init__(self):
        self._JackpotHit = False
        self._DomainExpanded = False
        self._Reach = False
        self._jackpotmp3 = pygame.mixer.Sound('E:\Code And Stuff\Idle Death Gamble\Music\jackpotmusicAY.mp3')
        self._music = "ay"
        self._prob = 0
        self._choice1 = None
        self._choice2 = None
        self._visualcolour1 = None
        self._visualcolour2 = None
        
    def DomainExpansion(self):
        time.sleep(0.5)
        print("\nᒥ領域展開ᒧ\nᒥDomain Expansionᒧ\n")
        time.sleep(1.5)
        print("ᒥ坐殺博徒ᒧ\nᒥIdle Death Gambleᒧ\n")
        self._DomainExpanded = True
        
    def Jackpot(self):
        self._JackpotHit = True
        self._DomainExpanded = False
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
        self._jackpotmp3.play()
        DomainMenu._spincounter = 0
        DomainMenu._visualcounter = 0
        slot1._value = 1
        slot2._value = 2
        slot._value = 3
        if self._music == "tol":
            print("trippingonlove.mp3")
            time.sleep(1)
        elif self._music == "ay":
            print("admiringyou.mp3")
            time.sleep(2)
        print("\n...Let's make a deal")
        time.sleep(2)
        print("Kashimo.")
        time.sleep(3)
        
    def rollall(self,initial,needprob,reachprob):
        self._prob = random.randint(1,1000)
        if self._prob <= needprob:
            Hakari.reachroll(random.randint(1,7),"same")
        elif self._prob <= reachprob:
            Hakari.reachroll(random.randint(1,7),None)
        else:
            print(slot1.spin(initial))
            time.sleep(0.8)
            print(slot2.spin(initial))
            time.sleep(0.8)
            print(slot3.spin(initial))
            time.sleep(0.5)

    def reachroll(self,rig1,rig2):
        self._prob = random.randint(1,1000)
        if rig2 == "same":
            rig2 = rig1
        if self._prob <= 555:
            print("REACH!")
            print("")
            time.sleep(0.8)
            print(slot1.spin(rig1))
            time.sleep(0.8)
            print(slot2.spin(rig1))
            time.sleep(1.2)
            print(slot3.spin(rig2))
            time.sleep(0.5)
        else:
            Hakari.rollall(None,50,270)

    def musicchoice(self):
        print("\nWhich music would you like to have for the jackpot?\n")
        time.sleep(0.5)
        self._music = input("Tripping On Love (Enter 'TOL')\nor\nAdmiring You (Enter 'AY') ")
        self._music = self._music.lower()
        if self._music == "tol":
            self._jackpotmp3 = pygame.mixer.Sound('E:\Code And Stuff\Idle Death Gamble\Music\jackpotmusicTOL.mp3')
            print("Music Changed\n")
        elif self._music == "ay":
            self._jackpotmp3 = pygame.mixer.Sound('E:\Code And Stuff\Idle Death Gamble\Music\jackpotmusicAY.mp3')
            print("Music Changed\n")
            
    def visualcombo(self):
        self._choice1 = DomainMenu._choicelist[0]
        self._choice2 = DomainMenu._choicelist[1]
        if self._choice1 == "1":
            self._visualcolour1 = ReserveBall._colour
        elif self._choice1 == "2":
            self._visualcolour1 = TrainDoors._colour
        if self._choice2 == "1":
            self._visualcolour2 = ReserveBall._colour
        elif self._choice2 == "2":
            self._visualcolour2 = TrainDoors._colour

        if TrainDoors._colour == "Rainbow??" or ReserveBall._colour == "Rainbow??":
            Hakari.rollall(None,1000,1000)
            
        if self._visualcolour1 == "Red" and self._visualcolour2 == "Red":
            Hakari.rollall(None,4,100)
            
        elif self._visualcolour1 == "Red" and self._visualcolour2 == "Green" or self._visualcolour1 == "Green" and self._visualcolour2 == "Red":
            Hakari.rollall(None,25,200)
            
        elif self._visualcolour1 == "Green" and self._visualcolour2 == "Green":
            Hakari.rollall(None,60,330)

        elif self._visualcolour1 == "Green" and self._visualcolour2 == "Gold" or self._visualcolour1 == "Gold" and self._visualcolour2 == "Green":
            Hakari.rollall(None,130,600)
            
        elif self._visualcolour1 == "Gold" and self._visualcolour2 == "Gold":
            Hakari.rollall(None,500,1000)
            
        elif self._visualcolour1 == "Gold" and self._visualcolour2 == "Red" or self._visualcolour1 == "Red" and self._visualcolour2 == "Gold":
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
            self._colour = "Red"
        elif chance >= 28 and chance <= 70:
            self._colour = "Green"
        elif chance >= 71 <= 99:
            self._colour = "Gold"
        if chance == 100:
            self._colour = "Rainbow??"
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
        self._choice = None
        self._spincounter = 0
        self._visualcounter = 0
        self._choicelist = []

    def MenuChoice(self):
        self._choice = input("What do you do?\nEnter 1 to throw a Reserve Ball\nEnter 2 to use the Train Doors ")
        if self._choice == "1":
            print(ReserveBall.spincolour())
            (self._choicelist).append(self._choice)
            time.sleep(1)
            if self._visualcounter == 2 and self._spincounter == 4:
                Hakari.reachroll(random.randint(1,7),"same")
                self._choicelist = []
            if self._visualcounter == 2:
                Hakari.visualcombo()
                self._spincounter = self._spincounter + 1
                self._choicelist = []
        elif self._choice == "2":
            print(TrainDoors.spincolour())
            (self._choicelist).append(self._choice)
            time.sleep(1)
            if self._visualcounter == 2 and self._spincounter == 4:
                Hakari.reachroll(random.randint(1,7),"same")
                self._choicelist = []
            if self._visualcounter == 2:
                Hakari.visualcombo()
                self._spincounter = self._spincounter + 1
                self._choicelist = []
        elif self._choice == "Leave" or self._choice == "leave":
            DomainMenu.initialmenu()
                
    def initialmenu(self):
        print("\nWelcome to Hakari Domain Simulator\n")
        time.sleep(0.5)
        self._choice = input("Enter 1 to start the Sim\nEnter 2 to access settings\nEnter 3 to Quit ")
        if self._choice == "1":
            time.sleep(0.5)
            print("When the 'What do you do' Menu is shown, type 'Leave' to return to this menu")
            self._choice = input("\nYou have to fight!\nExpand your domain? (y/n)")
            if self._choice == "y":
                time.sleep(0.5)
                Hakari.DomainExpansion()
                time.sleep(1)
            else:
                quit()
        if self._choice == "2":
            time.sleep(0.5)
            Hakari.musicchoice()
        if self._choice == "3":
            quit()
                
DomainMenu = Menu()
    
def main():
    DomainMenu.initialmenu()
    while Hakari._DomainExpanded == True:
        DomainMenu.MenuChoice()
        if slot1._value == slot2._value and slot2._value == slot3._value:
            Hakari.Jackpot()

while True == True:
    main()

