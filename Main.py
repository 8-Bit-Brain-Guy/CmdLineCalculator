import os
import time
import readkeys
import keyboard
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
        self.__marker = 1
        self.__exit = False
        #self.loop()

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



    def loop(self):
        while (self.__exit == False):
            keyboard.on_press(self.on_key_press)
            self.printMenue()            
            keyboard.wait('esc')    
            keyboard.unhook_all()

        # 



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