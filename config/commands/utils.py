from colorama import Fore
import time

# Functions to print colored messages
def error(message):
    print(Fore.RED + "[ERROR] " + message)

def warning(message):
    print(Fore.YELLOW + "[WARNING] " + message)

def confirmation(message):
    print(Fore.GREEN + "[SUCCESS] " + message)

def rejection(message):
    print(Fore.MAGENTA + "[-] " + message)  # Changed to magenta for a distinct look

def info(message):
    print(Fore.CYAN + "[INFO] " + message)  # Changed to cyan for informational messages

def command(message):
    print(Fore.LIGHTCYAN_EX + "[COMMAND] " + message)  # Changed to cyan for informational messages