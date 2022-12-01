'''Assignment 4: CRUD Application
PROG10004 Fall 2022

Program:
module contains all user interaction logic
'''
from constants import *
import DataPersistence


class Program:
    def run(garage):
        print("==Welcome to your Virtual Garage==")
        while(True):
            try:
                user_input = int(input(PROGRAM_MENU))
                if user_input == 1:
                    print(garage)
                elif user_input == 2:
                    garage.add_vehicle(
                        input("Specify Make: "),
                        input("Specify Model: "),
                        int(input("Specify Year: ")),
                        input("Specify Color: ")
                    )
                    print("Vehicle Successfully Parked")
                elif user_input == 3:
                    garage.remove_vehicle(
                        int(input("Specify lot number to remove vehicle from: "))
                    )
                    print("Vehicle Successfully Removed")
                elif user_input == 4:
                    print(garage.search_vehicle(
                        input("Specify Make: "), input("Specify Model: ")))
                elif user_input == 5:
                    garage.paint_vehicle(
                        int(input("Specify lot number of vehicle to  paint: ")),
                        input("Specify Color to paint vehicle: ")
                    )
                    print("Successfully painted vehicle")
                elif user_input == 6:
                    break
                else:
                    raise Exception("Input value not in range")
                DataPersistence.update_database(garage)

            except Exception as e:
                print(e, "Please try again")
