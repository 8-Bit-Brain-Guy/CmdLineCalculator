import keyboard
import os

value = None
__marker = 1

def clearScreen():
    os.system("cls")


def printMenue():
    clearScreen()
    print("########################################")
    print("############ Taschenrechner ############")
    print("########################################")
    print("")
    print("Alternatively press ESC to exit the program...")
    print("")
    if __marker == 1: 
        print(">>>  Calculate  <<<")
        print("     Print")
        print("     Exit")
    elif __marker == 2:
        print("     Calculate")
        print(">>>  Print      <<<")
        print("     Exit")
    elif __marker == 3:
        print("      Calculate")
        print("      Print")
        print(">>>   Exit           <<<")


def on_key_press(event):
    print("Taste gedrückt: ", event.name)
    print("Scan code:      ", event.scan_code)
    print("Timestamp:      ", event.time)
    ## if event.name == 'esc':
    ##    keyboard.unhook_all()
    value = event.scan_code


keyboard.on_press(on_key_press)


clearScreen()
printMenue()


# Halten Sie das Programm am Laufen, damit es Tastatureingaben abfragen kann
keyboard.wait('esc')
print(value)
## while True:
##     if keyboard.is_pressed("q"):
##         print("QQQQ")

