import os
import time
import readkeys
import platform

## Mathematische Funktionen später vielleicht in eine eigenen Klasse und eine eigene Datei (Modul) auslagern.


class Taschenrechner:

    def __init__(self):
        self.__mathMethod = None
        # Check operating system this program is running on.
        self.__operatingSystem = platform.system()
        self.__num1 = None
        self.__num2 = None
        self.__res = None


    def clearScreen(self):
        if self.__operatingSystem == 'Windows':
            os.system("cls")
        else:
            os.system("clear")


    def printMenue(self, marker):
        self.clearScreen()
        print("########################################")
        print("############ Taschenrechner ############")
        print("########################################")
        print("")
        if marker == 1: 
            print(">>> Addition       <<<")
            print("    Subtraktion")
            print("    Multiplikation")
            print("    Divison")
            print("    Exit")
        elif marker == 2:
            print("    Addition")
            print(">>> Subtraktion    <<<")
            print("    Multiplikation")
            print("    Divison")
            print("    Exit")
        elif marker == 3:
            print("    Addition")
            print("    Subtraktion")
            print(">>> Multiplikation <<<")
            print("    Divison")
            print("    Exit")
        elif marker == 4:
            print("    Addition")
            print("    Subtraktion")
            print("    Multiplikation")
            print(">>> Divison        <<<")
            print("    Exit")
        else:
            print("    Addition")
            print("    Subtraktion")
            print("    Multiplikation")
            print("    Divison")
            print(">>> Exit           <<<")


    def printOperationView(self):
        #time.sleep(2)
        #self.clearScreen()
        if self.__mathMethod == 'add':
            print("############ Additon ############")
            self.__num1 = float(input())
            print(" + ")
            self.__num2 = float(input())
            self.__res = self.addition(self.__num1, self.__num2)
            print(" = %f" %self.__res )

    def loop(self):
        # wait for input on keyboard
        # key = input("Enter number: ")
#        readkeys.flush()
#        key = readkeys.getkey()

        i = 17
        while i < 6:
            self.printMenue(i)
            time.sleep(0.5)
            i+=1
        self.__mathMethod = 'add'
        self.printOperationView()

####        key = 1
####        if key == 1:
####            self.__mathMethod = 'add'
####            self.printOperationView()



    def addition(self, zahl1, zahl2):
        return zahl1 + zahl2
    
    def subtraktion(self, zahl1,zahl2):
        return zahl1 - zahl2
    
    def multiplikation(self, zahl1,zahl2):
        return zahl1 * zahl2

    def division(self, zahl1, zahl2):
        return zahl1 / zahl2




if __name__ == '__main__':
    Tr = Taschenrechner()
    Tr.loop()





