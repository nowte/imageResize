import os
import time
from colorama import init, Fore
from importlib import import_module

# Import the utils module
import utils

# Initialize Colorama
init(autoreset=True)
os.system('title iR Config')

def connect_to_system():
    time.sleep(2)
    utils.connect_to_system()

def restart_system():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    utils.confirmation("System is restarting...")
    time.sleep(1)
    connect_to_system()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    connect_to_system()

    while True:
        # Execute image resize module
        module = import_module("commands.main_system")
        module.execute()

        # Ask if user wants to continue
        continue_choice = input("Do you want to resize another image? (y/n): ").strip().lower()
        print("")
        
        if continue_choice == 'n':
            # Show support and contact information
            utils.info("Thank you for using the iR Image Resizer!")
            time.sleep(1)
            print("")
            utils.info("For support, contact us at image@resize.com")
            utils.info("For inquiries, email us at info@imageResize.com")
            print("")
            time.sleep(5)
            break  # Exit the loop and end the program

        elif continue_choice != 'y':
            utils.warning("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
