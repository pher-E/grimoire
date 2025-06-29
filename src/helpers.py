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

    

def script_scan(filepath):
    try:
        with open(filepath) as f:
            chars = json.loads(f.read())
            chars.pop(0)
            return chars
    except:
        return []