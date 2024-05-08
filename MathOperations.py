class MathOperations:

    def __init__(self):
        self.__zahl = 100
        self.z = 111

    def test(self, zahl1):
        print("Der übergebene Wert ist: %d" %zahl1)
        print("Der Wert ist: %d" %self.__zahl)


    def addition(self, zahl1, zahl2):
        print("Der übergebene Wert ist: %d" %zahl1, "und %d" %zahl2)
        return zahl1 + zahl2


    def subtraktion(self, zahl1,zahl2):
        print("Der übergebene Wert ist: %d" %zahl1, "und %d" %zahl2)
        return zahl1 - zahl2


    def division(self, zahl1, zahl2):
        print("Der übergebene Wert ist: %d" %zahl1, "und %d" %zahl2)
        return zahl1 / zahl2


    def multiplikation(self, zahl1,zahl2):
        print("Der übergebene Wert ist: %d" %zahl1, "und %d" %zahl2)
        return zahl1 * zahl2

