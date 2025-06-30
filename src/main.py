from time import sleep
from helpers import *
from party import Party

print("bruh")

def main():
    clear_screen()
    sleep(.7)

    print("Blood on the Clocktower Grimoire (v0.0.2)\n")
    sleep(1)

    print("Welcome to the Grimoire, dear Storyteller\u2026")

    # player input
    names = set_players()
    if names == []:
        return 1

    sleep(.7)

    # script file input
    filepath = input("\nWhat script shall you use?\n > ")

    chars = script_scan("scripts/" + filepath + ".json")
    if (len(chars) == 0):
        # might need more error checking here
        error_out("Invalid script. (Ensure to type only the name of the file in 'scripts/')")
        return 1
    
    sleep(0.5)
    print("\n\u2026\n")

    # now turn them into character dictionaries
    chars = char_convert(chars)
    if (len(chars) == 0):
        error_out("At least one invalid character (listed above) was found.")

    sleep(0.5)

    # creating the Party object
    party = Party(chars, names)
    party.showScript()

    input("Press ENTER to see the character arrangement.\n")
    party.showDefIP()
    party.listPlayers()

    # next show if setup is required and start the loop!!

    return 0

if __name__ == "__main__":
    main()