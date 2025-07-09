def acc_player(party, player):
    print("Enter one of the following options for", str(player))
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
            c = input("Please enter a valid index: ")

        c = int(c)
        if c < 1 or c > party.script.size:
            if c != 0:
                print("\nPlease input a value in range.\n")
            return player
        
        c = party.script.getChar(c - 1)
        print(str(c) + "\n")
        party.changePC(player, c)
    elif num == 3:
        again = True
        while again:
            rm = input("Enter the reminder to add to this player.\n > ")
            player.addReminder(rm)
            
            yn = input("Would you like to add another? (y/n)\n > ")
            while yn != "y" and yn != "n" and yn != "0":
                yn = input("Please input 'y' for 'yes' or 'n' for 'no'.\n > ")

            if yn != "y":
                again = False
    elif num == 4:
        if len(player.reminders) == 0:
            print("No reminders found.\n")
            return player
        
        again = True
        player.printReminders()
        r = input("Which reminder would you like to remove?\n > ")
        while not r.isnumeric():
            r = input("Please enter a valid index: ")

        r = int(r)
        if r < 1 or r > party.script.size:
            if r != 0:
                print("\nPlease input a value in range.\n")
            return

        player.rmReminder(r - 1)
    elif num == 5:
        print("Life changed.\n")
        player.changeLife()
    elif num != 0:
        print("Please input a value in range.\n")

    return player