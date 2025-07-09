class Player:
    def __init__(self, name):
        self.name = name
        self.reminders = []
        self.alive = True

    def __str__(self):
        if self.alive:
            return f"{self.name}"
        
        return f"X*{self.name}*X"
    
    def printSimple(self):
        return f"{self.name}"
    
    def getName(self):
        return self.name

    def changeName(self, name):
        self.name = name

    def getReminders(self):
        return self.reminders

    def addReminder(self, text):
        self.reminders.append(text)

    def rmReminder(self, i):
        self.reminders.pop(i)

    def changeLife(self):
        self.alive = not self.alive

    def printReminders(self):
        for i in range(len(self.reminders)):
            print("\t" + str(i + 1), "-", self.reminders[i])
        print()


class Character:
    def __init__(self, c):
        self.id = c["id"]
        self.name = c["name"]
        self.team = c["team"]
        self.firstNight = c["firstNight"]
        self.firstNightReminder = c["firstNightReminder"]
        self.otherNight = c["otherNight"]
        self.otherNightReminder = c["otherNightReminder"]
        self.setup = c["setup"]
        self.ability = c["ability"]

    def __str__(self):
        return f"{self.name}\n\t{self.ability}"
    
    def needsSetup(self):
        return self.setup
    
    def getName(self):
        return self.name

    def printFull(self):
        return f"{self.name} ({self.team})\n\t{self.ability}"


class Script:
    def __init__(self, chars):
        self.tf, self.os, self.mn, self.dm = [], [], [], []
        self.size = 0
        for char in chars:
            c = Character(char)
            self.size += 1

            if c.team == "townsfolk":
                self.tf.append(c)
            elif c.team == "outsider":
                self.os.append(c)
            elif c.team == "minion":
                self.mn.append(c)
            else:
                self.dm.append(c)

    def getChar(self, i):
        if i < len(self.tf):
            return self.tf[i]
        
        i -= len(self.tf)
        if i < len(self.os):
            return self.os[i]
        
        i -= len(self.os)
        if i < len(self.mn):
            return self.mn[i]
        
        i -= len(self.mn)
        return self.dm[i]
    
    def printChars(self):
        print("\nTownsfolk:")
        i = 1
        for c in self.tf:
            print("\t" + str(i), "-", c.getName())
            i += 1

        print("\nOutsiders:")
        for c in self.os:
            print("\t" + str(i), "-", c.getName())
            i += 1

        print("\nMinions:")
        for c in self.mn:
            print("\t" + str(i), "-", c.getName())
            i += 1

        text = "\nDemon"
        if len(self.dm) != 1:
            text += "s"
        print(text + ":")
        for c in self.mn:
            print("\t" + str(i), "-", c.getName())
            i += 1
        
        print()

    def printFull(self):
        print("\n---TOWNSFOLK---")
        for c in self.tf:
            print("\n" + str(c))

        print("\n---OUTSIDERS---")
        for c in self.os:
            print("\n" + str(c))

        print("\n---MINIONS---")
        for c in self.mn:
            print("\n" + str(c))

        text = "DEMON"
        if len(self.dm) != 1:
            text += "S"

        print("\n---" + text + "---")
        for c in self.dm:
            print("\n" + str(c))

        print("\n")