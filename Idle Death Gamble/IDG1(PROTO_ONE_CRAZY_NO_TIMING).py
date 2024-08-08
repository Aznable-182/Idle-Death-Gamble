import random
import time

class Gambler():
    def __init__(self):
        self._JackpotHit = False
        self._DomainExpanded = False
    def DomainExpansion(self):
        print("Domain Expansion")
        print("ᒥ坐殺博徒ᒧ")
        print("ᒥIdle Death Gambleᒧ")
        self._DomainExpanded = True
        
    def JackpotHit(self):
        self._JackpotHit = True
        self._DomainExpanded = False
        
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
        return "The " +self._name+ " " +self._grammar+ " " +self._colour+ "!"
        

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
        return namevalue

ReserveBall = visualEffect("Reserve Ball")
TrainDoors = visualEffect("Train Doors")
slot1 = slot(1)
slot2 = slot(2)
slot3 = slot(3)
    
class Menu():
    def __init__(self):
        self._choice = None
    def MenuChoice(self):
        choice = input("What do you do?\nEnter 1 to throw a Reserve Ball\nEnter 2 to use the Train Doors\nEnter 3 to Spin ")
        if choice == "1":
            print("")
            print(ReserveBall.spincolour())
            print("")
        elif choice == "2":
            print("")
            print(TrainDoors.spincolour())
            print("")
        elif choice == "3":
            global spincounter
            if spincounter == 10000000000:
                rignumber = random.randint(1,7)
                print("")
                print(slot1.spin(rignumber))
                print(slot2.spin(rignumber))
                print(slot3.spin(rignumber))
            else:
                print("")
                print(slot1.spin(None))
                print(slot2.spin(None))
                print(slot3.spin(None))
            spincounter = spincounter + 1
            
def main():
    DomainOverride = False
    Hakari = Gambler()
    DomainMenu = Menu()
    Hakari.DomainExpansion()
    global spincounter
    spincounter = 0
    while Hakari._DomainExpanded == True:
        DomainMenu.MenuChoice()
        if slot1._value == slot2._value and slot2._value == slot3._value or DomainOverride == True:

            print("Hakari never acquired Reverse Cursed Technique.")
            print("But...")
            print("The infinite Cursed Energy overflowing in Hakari's Body")
            print("caused his body to reflexively perform Reverse Cursed Technique\nin order to avoid damage.")
            print(" ")
            print("In other words,")
            print("in the 4 minutes and 11 seconds following a Jackpot,")
            print("Hakari is")
            print("Effectively")
            print("Immortal.")
            print("*trippingonlove.mp3*\n")
            Hakari.JackpotHit()
            time.sleep(5)

while True == True:
    main()

