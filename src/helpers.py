from os import system, name
from time import sleep
import json

def clear_screen():
    # on start
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def error_out(text):
    print("\nERROR:", text)
    sleep(1)
    print("Goodbye.")
    sleep(1.5)
    clear_screen()

def set_players():
    raw_pop = input("\nHow many players are you hosting?\n > ")
    while not raw_pop.isnumeric():
        raw_pop = input("Please input a valid number.\n > ")
    
    pop = int(raw_pop)
    if pop < 5:
        error_out("You need more players to tell this story\u2026")
        return []
    elif pop > 15:
        error_out("You have too many players to tell this story\u2026")
        return []
    
    sleep(.2)

    print("Please enter your players' names (Keeping them in order would be helpful!):")

    names = []
    for i in range(1, pop + 1):
        name = input("\t" + str(i) + " - ")
        while len(name) == 0:
            name = input("Please input a name: ")
        names.append(name)

    return names

def script_scan(filepath):
    try:
        with open(filepath) as f:
            chars = json.loads(f.read())
            chars.pop(0)
            return chars
    except:
        return []
    
def char_convert(chars):
    with open("src/char_lib.json") as f:
        lib = json.loads(f.read())
        objs, good = [], True
        for c in chars:
            found = False
            for obj in lib:
                if c == obj["id"]:
                    objs.append(obj)
                    found = True
                    break
            if not found:
                good = False
                print(c)
                sleep(.5)
        if good:
            return objs 
        else:
            return []