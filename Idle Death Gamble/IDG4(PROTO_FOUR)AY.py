import random
import time
import pygame
pygame.init()
trippingonlove = pygame.mixer.Sound('E:\Code And Stuff\Idle Death Gamble\Music\jackpotmusicAY.mp3')
    
class Gambler():
    def __init__(self):
        self._JackpotHit = False
        self._DomainExpanded = False
        self._Reach = False
        
    def DomainExpansion(self):
        time.sleep(0.5)
        print("ᒥ領域展開ᒧ")
        print("ᒥDomain Expansionᒧ")
        time.sleep(1.5)
        print("ᒥ坐殺博徒ᒧ")
        print("ᒥIdle Death Gambleᒧ")
        self._DomainExpanded = True
        
    def Jackpot(self):
        self._JackpotHit = True
        self._DomainExpanded = False
        time.sleep(0.7)
        print("Hakari never acquired Reverse Cursed Technique.")
        time.sleep(3.5)
        print("But...")
        time.sleep(0.5)
        print("The infinite Cursed Energy overflowing in Hakari's Body")
        print("caused his body to reflexively perform Reverse Cursed Technique\nin order to avoid damage.")
        print(" ")
        time.sleep(8)
        print("In other words,")
        print("in the 4 minutes and 11 seconds following a Jackpot,")
        time.sleep(4.1)
        print("Hakari")
        time.sleep(0.9)
        print("Is effectively")
        time.sleep(1.1)
        print("Immortal.")
        time.sleep(0.5)
        print("*admiringyou.mp3*\n")
        trippingonlove.play()
        time.sleep(251)
        
    def rollall(self,initial):
        print(slot1.spin(initial))
        time.sleep(0.8)
        print(slot2.spin(initial))
        time.sleep(0.8)
        print(slot3.spin(initial))
        time.sleep(0.5)

    def reachroll(self,rig1,rig2):
        prob = random.randint(1,100)
        if rig2 == "same":
            rig2 = rig1
        if prob <= 55:
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
            Hakari.rollall(None)

Hakari = Gambler()
        
class visualEffect():
    def __init__(self,Name):
        self._name = Name
        self._colour = None
        self._grammar = None
        
    def spincolour(self):
        chance = random.randint(1,3)
        if chance == 1:
            self._colour = "Red"
        elif chance == 2:
            self._colour = "Green"
        elif chance == 3:
            self._colour = "Gold"
        if self._name == "Reserve Ball":
            self._grammar = "is"
        else:
            self._grammar = "are"
        time.sleep(0.5)
        DomainMenu._visualcounter = DomainMenu._visualcounter + 1
        return "The " +self._name+ " " +self._grammar+ " " +self._colour+ "!"

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
        
    def MenuChoice(self):
        self._choice = input("What do you do?\nEnter 1 to throw a Reserve Ball\nEnter 2 to use the Train Doors ")
        if self._choice == "1":
            print("")
            print(ReserveBall.spincolour())
            print("")
            time.sleep(1)
            if self._visualcounter == 2 and self._spincounter == 4:
                rignumber = random.randint(1,7)
                Hakari.rollall(rignumber)
            if self._visualcounter == 2:
                Hakari.reachroll(random.randint(1,7),None)
                self._spincounter = self._spincounter + 1
        elif self._choice == "2":
            print("")
            print(TrainDoors.spincolour())
            print("")
            time.sleep(1)
            if self._visualcounter == 2 and self._spincounter == 4:
                rignumber = random.randint(1,7)
                Hakari.reachroll(random.randint,"same")
            if self._visualcounter == 2:
                Hakari.reachroll(random.randint(1,7),None)
                self._spincounter = self._spincounter + 1
                
DomainMenu = Menu()
def varireset():
    DomainMenu._spincounter = 0
    DomainMenu._visualcounter = 0
    slot1._value = 1
    slot2._value = 2
    slot._value = 3
    
def main():
    Hakari.DomainExpansion()
    print("")
    time.sleep(1)
    while Hakari._DomainExpanded == True:
        DomainMenu.MenuChoice()
        if slot1._value == slot2._value and slot2._value == slot3._value:
            Hakari.Jackpot()
            varireset()

while True == True:
    main()

