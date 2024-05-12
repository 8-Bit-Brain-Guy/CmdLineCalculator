import os
import time
import readkeys
import keyboard
import platform
from MathOperations import *



## Mathematische Funktionen später vielleicht in eine eigenen Klasse und eine eigene Datei (Modul) auslagern.


class Taschenrechner:

    def __init__(self):
        self.__mathMethod = None
        # Check operating system this program is running on.
        self.__operatingSystem = platform.system()
        self.__num1 = None
        self.__num2 = None
        self.__op = None
        self.__res = None
        self.__marker = 1
        self.__exit = False
        self.__mathOP = MathOperations()
        self.__scanCode = None



    def on_key_press(self, event):
        print("Taste gedrückt: ", event.name)
        print("Scan code:      ", event.scan_code)
        print("Timestamp:      ", event.time)
        if event.scan_code == 72:
            self.__marker -= 1
        elif event.scan_code == 80:
            self.__marker += 1
        elif event.name == 'esc':
            self.__exit = True



    def clearScreen(self):
        if self.__operatingSystem == 'Windows':
            os.system("cls")
        else:
            os.system("clear")



    def printMenue(self):
        self.clearScreen()
        print("########################################")
        print("############ Taschenrechner ############")
        print("########################################")
        print("")
        print("Alternatively press ESC to exit the program...")
        print("")
        if self.__marker == 1: 
            print(">>>  Calculate  <<<")
            print("     Print")
            print("     Exit")
        elif self.__marker == 2:
            print("     Calculate")
            print(">>>  Print      <<<")
            print("     Exit")
        elif self.__marker == 3:
            print("      Calculate")
            print("      Print")
            print(">>>   Exit           <<<")



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


    def parseInputString(self):
        # a = input("Enter number: ")                                 # a = '123': a wird als class 'str' behandelt. int(a)+1 = 124
        inp = input("> ")
        print(inp)
        
        # Eleminate all spaces in inputstring so that they will not have to be handeled later
        if " " in inp:
            pass

        # Find mathematical operator
        if "+" in inp:
            self.__op = "+"
        elif "-" in inp:
            self.__op = "-"
        elif "*" in inp:
            self.__op = "*"
        elif "/" in inp:
            self.__op = "/"
        else:
            self.__op = -1

        # Extract first and second number:
        self.__num1 = inp[0 : inp.find(self.__op)]
        self.__num2 = inp[inp.find(self.__op)+1 : len(inp)]
        # print(self.__num1)
        # print(self.__num2)




    def loop(self):
        while (self.__exit == False):
            self.printMenue()            
            keyboard.on_press(self.on_key_press)
            keyboard.wait('esc')    
            # keyboard.unhook_all()



if __name__ == '__main__':
    Tr = Taschenrechner()
    # Tr.parseInputString()
    Tr.loop()