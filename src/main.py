from time import sleep
from helpers import clear_screen, set_players
from boot import boot
from night import night

def main():
    clear_screen()
    sleep(.7)

    print("\nBlood on the Clocktower Grimoire (v0.0.3)\n")
    sleep(1)

    party = boot()
    firstNight = True
    while True:
        sleep(1)
        print("Enter one of the following commands to prepare for the night:")
        print("\t1. See Town Square")
        print("\t2. See script")
        print("\t3. See in-play characters")
        print("\t4. Change player name")
        print("\t5. Change player character")
        print("\t6. Add a player reminder")
        print("\t7. Remove a player reminder")
        print("\t8. Reroll all characters")
        print("\t0. Start the night")
        print("\n\t-1. Exit the grimoire")

        sleep(.5)
        print("\t\t(Enter 'back' to return to this menu anytime)\n")
        sleep(.5)
        text = input(" > ")

        if text.casefold() == "quit":
            break
        elif text.casefold() == "back":
            clear_screen()
            continue

        if text.isnumeric():
            num = int(text)

            if num == 1:
                party.listPlayers()
            elif num == 2:
                party.showScript()
            elif num == 3:
                party.showIP()
            elif num == 4:
                party.showSetup()
            elif num >= 4 or num <= 7:
                print("Which player would you like to access?")
                party.listPlayersHidden()

                player = input(" > ")
                while not player.isnumeric():
                    if player.casefold() == "back":
                        continue

                    player = input("Please enter a valid index: ")
                if int(player) < 1 or int(player) > len(party.players):
                    player = input("\nPlease input a value in range.\n")
                    continue

                player = party.getPlayer(player - 1)

                if num == 4:
                    name = input("Enter a new name: ")
                    player.changeName(name)
                elif num == 5:
                    party.script.printChars()
                    print("(Keep in mind the characters currently in-play, shown below.)")
                    party.showIP()
                    c = input("Which character shall you assign?\n > ")
                    while not c.isnumeric():
                        if c.casefold() == "back":
                            continue

                        c = input("Please enter a valid index: ")
                    if int(c) < 1 or int(c) > len(party.script.size):
                        print("\nPlease input a value in range.\n")
                        continue
                    
                    c = party.script.getChar(c - 1)
                    player.changeChar(c)
                elif num == 6:
                    rm = input("Enter the reminder to add to this player.\n > ")
                    player.addReminder(rm)
                elif num == 7:
                    player.printReminders()
                    r = input("Which reminder would you like to remove?\n > ")
                    while not r.isnumeric():
                        if r.casefold() == "back":
                            continue

                        r = input("Please enter a valid index: ")
                    if int(r) < 1 or int(r) > len(party.script.size):
                        print("\nPlease input a value in range.\n")
                        continue

                    player.rmReminder(r - 1)                
            elif num == 8:
                yn = input("Are you sure (y/n)?\n > ")
                while yn != "y" and yn != "n":
                    if yn.casefold() == "back":
                        continue

                    yn = input("Please input 'y' for 'yes' or 'n' for 'no'.\n > ")
                if yn == 'n':
                    continue
                party.rollChars()
                print("New characters have been chosen.\n")
            elif num == 0:
                night(firstNight)
                firstNight = False
            else:
                print("\nPlease input a value in range.\n")
        else:
            print("\nPlease enter a valid command.\n")

    return 0

if __name__ == "__main__":
    main()