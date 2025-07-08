from classes import Script, Player
import random

class Party:
    def __init__ (self, chars, names):
        self.script = Script(chars)
        self.players, self.IP = [], []
        self.tfNum, self.osNum, self.mnNum, self.dmNum = 0, 0, 0, 1

        pop = len(names)
        if pop >= 13:
            self.tfNum, self.mnNum = 9, 3
            pop -= 13
        elif pop >= 10:
            self.tfNum, self.mnNum = 7, 2
            pop -= 10
        elif pop >= 7:
            self.tfNum, self.mnNum = 5, 1
            pop -= 7
        else:
            self.tfNum, self.mnNum = 3, 1
            pop -= 5

        # any remainder are added as outsiders
        for i in range(pop):
            self.osNum += 1

        self.rollChars()
        for i in range(len(names)):
            self.players.append(Player(names[i], self.IP[i]))

    def rollChars(self):
        self.IP = [] # reset IP

        # error check
        if len(self.script.dm) == 0 or len(self.script.mn) < self.mnNum or len(self.script.os) < self.osNum or len(self.script.tf) < self.tfNum:
            # insufficient script -> self.tfIP = self.osIP = self.mnIP = self.dmIP = []
            return
        
        tfInd, osInd, mnInd = [], [], []
        for i in range(max(len(self.script.tf), len(self.script.os), len(self.script.mn))):
            if i < len(self.script.os):
                osInd.append(i)
            if i < len(self.script.mn):
                mnInd.append(i)
            if i < len(self.script.tf):
                tfInd.append(i)

        random.seed()

        random.shuffle(tfInd)
        random.shuffle(osInd)
        random.shuffle(mnInd)
        dmInd = random.randrange(0, len(self.script.dm))
        
        
        for i in range(self.tfNum):
            if i < self.osNum:
                self.IP.append(self.script.os[osInd[i]])
            if i < self.mnNum:
                self.IP.append(self.script.mn[mnInd[i]])
            self.IP.append(self.script.tf[tfInd[i]])

        self.IP.append(self.script.dm[dmInd])
        random.shuffle(self.IP)

    def listPlayers(self):
        for i in range(len(self.players)):
            print("\t" + str(i + 1), "-", str(self.players[i]), f"({self.IP[i].getName()})")

        for s in self.players[i].getReminders():
            print("\t\t~", s)
        print()

    def listPlayersHidden(self):
        for i in range(len(self.players)):
            print("\t" + str(i + 1), "-", str(self.players[i]))
        print()
    
    def getPlayer(self, i):
        return self.players[i]
    
    def changePC(self, player, c):
        i = self.players.index(player)
        self.IP[i] = c
    
    def showSimpleScript(self):
        self.script.printChars()

    def showScript(self):
        self.script.printFull()
    
    def showDefIP(self):
        print(f"{self.tfNum} Townsfolk, {self.osNum} Outsider(s), {self.mnNum} Minion(s), and {self.dmNum} Demon")

    def showIP(self):
        for c in self.IP:
            print(c.printFull())

    def swapChars(self, i1, i2):
        if i1 != i2:
            tmp = self.IP[i1]
            self.IP[i1] = self.IP[i2]
            self.IP[i2] = tmp

    def showSetup(self):
        noSetup = True
        for c in self.IP:
            if c.needsSetup():
                if noSetup:
                    noSetup = False
                    print("This story requires a few more steps:\n")
                print(str(c))

    def showFirstNight(self):
        def sorter(c):
            return c.firstNight
        chars = self.IP.copy()
        chars.sort(key=sorter)

        while chars[0].firstNight == 0:
            chars.pop(0)

        count = 0
        for c in chars:
            if c.firstNight > 6:
                break
            print(c.printSimple(), "-", c.firstNightReminder + "\n")
            count += 1

        print("Minion Info - Wake the Minions so they see each other, and show them their demon.\n")

        while count > 0:
            chars.pop(0)
            count -= 1

        for c in chars:
            if c.firstNight > 9:
                break
            print(c.printSimple(), "-", c.firstNightReminder + "\n")
            count += 1

        print("Demon Info & Bluffs - Wake the Demon and show them their Minions. Then show them 3 good characters that are not in play.\n")

        while count > 0:
            chars.pop(0)
            count -= 1

        for c in chars:
            print(c.printSimple(), "-", c.firstNightReminder + "\n")

        print()

    def showOtherNight(self):
        def sorter(c):
            return c.otherNight
        chars = self.IP.copy()
        chars.sort(key=sorter)

        while chars[0].otherNight == 0:
            chars.pop(0)

        for c in chars:
            print(c.printSimple(), "-", c.otherNightReminder + "\n")

        print()