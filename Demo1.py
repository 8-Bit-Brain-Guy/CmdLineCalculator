'''
Demo1: Einfaches Demo einer Funktion mit einem Parameter und einem Rückgabenwert
Test2
HALLO WELT
'''

# Test

def Demofunktion(zahl):
    print("Der übergebene Wert ist: %d" %zahl)
    return zahl*2
    
    

rueckgabewert = Demofunktion(100)
print("Der Rückgabenwert ist %d" %rueckgabewert)
