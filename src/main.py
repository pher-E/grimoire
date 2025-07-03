from time import sleep
from helpers import clear_screen, acc_player
from boot import boot

def main():
    clear_screen()
    sleep(.7)

    print("\nBlood on the Clocktower Grimoire (v0.1.0)\n")
    sleep(1)

    party = boot()
    if party == 1:
        return

    firstNight = True
    while True:
        print("Enter one of the following commands to prepare for the night:")
        print("\t1. See Town Square")
        print("\t2. See script")
        print("\t3. See in-play characters")
        print("\t4. Access a player")
        print("\t5. Reroll all characters")
        print("\t9. See first night")
        print("\t0. See other nights")
        print("\n\t-1. Exit the grimoire")

        sleep(.2)
        print("\t\t(Enter 'back' to return to this menu anytime)\n")
        sleep(.2)
        text = input(" > ")

        if text == "-1":
            print("Goodbye.")
            sleep(1)
            break
        elif text.casefold() == "back":
            clear_screen()
            continue
        elif text == "test":
            party.showIP()
            continue

        print()

        if text.isnumeric():
            num = int(text)

            if num == 1:
                party.listPlayers()
            elif num == 2:
                party.showScript()
            elif num == 3:
                party.showIP()
            elif num == 4:
                print("Which player would you like to access?")
                party.listPlayersHidden()

                player = input(" > ")

                if player.casefold() == "back":
                    continue

                while not player.isnumeric():
                    player = input("Please enter a valid index: ")

                player = int(player)
                if player < 1 or player > len(party.players):
                    player = input("\nPlease input a value in range.\n")
                    continue

                player = party.getPlayer(player - 1)  
                player = acc_player(party, player)
            elif num == 5:
                yn = input("Are you sure (y/n)?\n > ")
                while yn != "y" and yn != "n":
                    if yn.casefold() == "back":
                        continue

                    yn = input("Please input 'y' for 'yes' or 'n' for 'no'.\n > ")
                if yn == 'n':
                    continue
                party.rollChars()
                print("New characters have been chosen.\n")
            elif num == 9:
                party.showFirstNight()
            elif num == 0:
                party.showOtherNight()
            else:
                print("\nPlease input a value in range.\n")
        else:
            print("\nPlease enter a valid command.\n")

        input("\nPress ENTER to continue to the menu.\n")
        clear_screen()

    return 0

if __name__ == "__main__":
    main()