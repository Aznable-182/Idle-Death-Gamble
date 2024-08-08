import random
import time
import pygame
pygame.init()
trippingonlove = pygame.mixer.Sound('E:\Code And Stuff\Idle Death Gamble\Music\jackpotmusicTOL.mp3')
    
class Gambler():
    def __init__(self):
        self._JackpotHit = False
        self._DomainExpanded = False
    def DomainExpansion(self):
        time.sleep(0.5)
        print("ᒥ領域展開ᒧ")
        print("ᒥDomain Expansionᒧ")
        time.sleep(0.5)
        print("ᒥ坐殺博徒ᒧ")
        print("ᒥIdle Death Gambleᒧ")
        self._DomainExpanded = True
        
    def Jackpot(self):
        self._JackpotHit = True
        self._DomainExpanded = False
        time.sleep(0.4)
        print("Hakari never acquired Reverse Cursed Technique.")
        time.sleep(3.25)
        print("But...")
        time.sleep(0.3)
        print("The infinite Cursed Energy overflowing in Hakari's Body")
        time.sleep(3)
        print("caused his body to reflexively perform Reverse Cursed Technique\nin order to avoid damage.")
        time.sleep(3.5)
        print(" ")
        time.sleep(0.5)
        print("In other words,")
        time.sleep(1.5)
        print("in the 4 minutes and 11 seconds following a Jackpot,")
        time.sleep(4.5)
        print("Hakari is effectivly")
        time.sleep(2)
        print("Immortal.")
        time.sleep(1.5)
        print("*trippingonlove.mp3*\n")
        trippingonlove.play()
        time.sleep(181)
        
    def rollall(self,initial):
        print(slot1.spin(initial))
        time.sleep(0.8)
        print(slot2.spin(initial))
        time.sleep(0.8)
        print(slot3.spin(initial))
        time.sleep(0.5)

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
            if self._visualcounter == 2 and self._spincounter == 3:
                rignumber = random.randint(1,7)
                Hakari.rollall(rignumber)
            if self._visualcounter == 2:
                Hakari.rollall(None)
                self._spincounter = self._spincounter + 1
        elif self._choice == "2":
            print("")
            print(TrainDoors.spincolour())
            print("")
            time.sleep(1)
            if self._visualcounter == 2 and self._spincounter == 3:
                rignumber = random.randint(1,7)
                Hakari.rollall(rignumber)
            if self._visualcounter == 2:
                Hakari.rollall(None)
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

