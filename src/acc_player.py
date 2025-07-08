def acc_player(party, player):
    print("Enter one of the following options for", player.printSimple())
    print("\t1. Change player name")
    print("\t2. Change player character")
    print("\t3. Add a player reminder")
    print("\t4. Remove a player reminder")
    print("\t5. Kill/revive player")

    num = input(" > ")
    while not num.isnumeric():
        num = input("Please enter a valid option: ")

    num = int(num)
    if num == 1:
        name = input("Enter a new name: ")
        player.changeName(name)
    elif num == 2:
        party.script.printChars()
        c = input("Which character shall you assign?\n > ")
        while not c.isnumeric():
            if c.casefold() == "back":
                return

            c = input("Please enter a valid index: ")

        c = int(c)
        if c < 1 or c > party.script.size:
            print("\nPlease input a value in range.\n")
            return
        
        c = party.script.getChar(c - 1)
        print(str(c) + "\n")
        party.changePC(player, c)
    elif num == 3:
        rm = input("Enter the reminder to add to this player.\n > ")
        player.addReminder(rm)
    elif num == 4:
        if len(player.reminders) == 0:
            print("No reminders found.\n")
            return
        
        player.printReminders()
        r = input("Which reminder would you like to remove?\n > ")
        while not r.isnumeric():
            if r.casefold() == "back":
                return

            r = input("Please enter a valid index: ")

        r = int(r)
        if r < 1 or r > party.script.size:
            print("\nPlease input a value in range.\n")
            return

        player.rmReminder(r - 1)
    elif num == 5:
        print("Life changed.\n")
        player.changeLife()
    elif num != 0:
        print("Please input a value in range.\n")

    return player