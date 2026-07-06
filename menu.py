import os
from utils import *
import time

def menu() -> int:
    os.system("clear||cls")

    print("Welcome to the CSV File Data Cleaner!\n")
    print("Choose an option:\n1) Start Cleaner\n2) Help\n3) Exit\n")

    choice = int(input("Select an option (1-3): "))

    return choice

def menu_selection():

    is_running = True

    while is_running:   
        match menu():
                case 1:    
                    os.system("clear||cls")
                    is_running = False
                case 2:
                    help()
                    is_running = False
                case 3:
                    print('Quitting...')
                    time.sleep(1)
                    os.system("clear||cls")
                    exit()
                case _:
                    print("Invalid Option Try Again...")
                    time.sleep(1)

def help():
    os.system("clear||cls")

    print("Instructions here.\n")
    # Write instructions later

    quitchar = input("Press 'q' to Exit: ")

    is_help_window = True

    while is_help_window:
        if quitchar == 'q':
            menu_selection()
            is_help_window = False
        else:
            print("Invalid Option Try Again...")
            time.sleep(1)
            help()

def clean():
    os.system("clean||cls")

    file_path = input("Please, give the path of the CSV file: ")

    raw_data = load(file_path)