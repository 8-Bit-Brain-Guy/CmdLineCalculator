import readkeys


class Taschenrechner:

    def __init__(self):
        print("")


    def printMenue(self, marker):
        print("########################################")
        print("############ Taschenrechner ############")
        print("########################################")
        print("")
        if marker == 1:
            print(">>> Addition <<<")
            
        print("    Subtraktion")
        print("    Multiplikation")
        print("    Divison")





    def loop(self):
        self.printMenue(1)
        # wait for input on keyboard
        # key = input("Enter number: ")
        readkeys.flush()
        key = readkeys.getkey()




def test(z):
    print("test")
    return z+1


if __name__ == '__main__':
    Tr = Taschenrechner()
    Tr.loop()




