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

# Logo function
def print_logo():
    print("""                               
    _                            ____            _          
   (_)___ ___  ____ _____ ____  / __ \___  _____(_)___  ___ 
  / / __ `__ \/ __ `/ __ `/ _ \/ /_/ / _ \/ ___/ /_  / / _ `
 / / / / / / / /_/ / /_/ /  __/ _, _/  __(__  ) / / /_/  __/
/_/_/ /_/ /_/\__,_/\__, /\___/_/ |_|\___/____/_/ /___/\___/ 
                  /____/                                 
          """)

# System connection screen
def connect_to_system():
    time.sleep(2)
    print(" ")
    print(" ")
    info("Connecting...")
    time.sleep(1)
    print(" ")
    print(" ")
    print_logo()
    print(" ")
    print(" ")
    time.sleep(1)
    confirmation("Connected to the system")
    print(" ")
    print(" ")
    print(" ")
    info("Welcome to the Image Resizer Tool!")
    time.sleep(1)
    info("This application allows you to resize your images easily.")
    time.sleep(1)
    print(" ")

# System restart screen
def restart_system():
    print(" ")
    print(" ")
    warning("Testing connection...")
    time.sleep(1)
    print(" ")
    print(" ")
    print_logo()
    print(" ")
    print(" ")
    time.sleep(1)
    confirmation("System connection tested")
    print("")
