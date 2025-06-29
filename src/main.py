from time import sleep
from helpers import *
# from party import *

print("bruh")

def main():
    clear_screen()
    sleep(.7)

    print("Blood on the Clocktower Grimoire (v0.1.1)\n")
    sleep(1)

    print("Welcome to the Grimoire, dear Storyteller\u2026")

    raw_pop = input("How many players are you hosting?\n > ")
    while not raw_pop.isnumeric():
        raw_pop = input("Please input a valid number.\n > ")
    
    pop = int(raw_pop)
    if pop < 5:
        error_out("You need more players to tell this story\u2026")
        return
    elif pop > 15:
        error_out("You have too many players to tell this story\u2026")
        return
    
    sleep(.7)
    filepath = input("What script shall you use?\n > ")

    # might need more error checking here
    chars = script_scan("scripts/" + filepath + ".json")
    if (len(chars) == 0):
        error_out("Invalid script. (Ensure to type only the name of the file in 'scripts/')")
        return
    
    print(chars)

if __name__ == "__main__":
    main()