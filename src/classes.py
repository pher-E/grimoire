class Player:
    def __init__(self, name, c):
        self.name = name
        self.c = c
        self.reminders = []

    def __str__(self):
        return f"{self.name} ({self.c.printSimple()})"
    
    def printSimple(self):
        return f"{self.name}"
    
    def getName(self):
        return self.name

    def changeName(self, name):
        self.name = name

    def changeChar(self, c):
        self.c = c

    def addReminder(self, text):
        self.reminders.append(text)

    def rmReminder(self, i):
        self.reminders.pop(i)


class Character:
    def __init__(self, c):
        self.id = c["id"]
        self.name = c["name"]
        self.team = c["team"]
        self.firstNight = c["firstNight"]
        self.firstNightReminder = c["firstNightReminder"]
        self.otherNight = c["otherNight"]
        self.reminders = c["reminders"]
        self.setup = c["setup"]
        self.ability = c["ability"]

    def __str__(self):
        return f"{self.name}\n\t{self.ability}"
    
    def printSimple(self):
        return f"{self.name}"

    def printFull(self):
        return f"{self.name} ({self.team})\n\t{self.ability}"


class Script:
    def __init__(self, chars):
        self.tf, self.os, self.mn, self.dm = [], [], [], []
        for char in chars:
            c = Character(char)
            if c.team == "townsfolk":
                self.tf.append(c)
            elif c.team == "outsider":
                self.os.append(c)
            elif c.team == "minion":
                self.mn.append(c)
            else:
                self.dm.append(c)

    def printChars(self):
        print("\nTownsfolk:")
        for c in self.tf:
            print("\t-", c.printSimple())

        print("\nOutsiders:")
        for c in self.os:
            print("\t-", c.printSimple())

        print("\nMinions:")
        for c in self.mn:
            print("\t-", c.printSimple())

        text = "\nDemon"
        if len(self.dm) != 1:
            text += "s"
        
        print(text + ":")
        for c in self.mn:
            print("\t-", c.printSimple())
        
        print("\n")

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