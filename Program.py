from Garage import Garage
import io
import json
import os
from constants import *


class Program:
    def run():
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print("Loading vehicles from garage database...")
            with open(DB_NAME) as database:
                garage = Garage(json.load(database))
        else:
            print("No database found, creating new database...")
            with io.open(os.path.join(ROOT, DB_NAME), 'w') as database:
                database.write(json.dumps({}))
            garage = Garage({})

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
                        int(input("Specify Year: "))
                    )
                    print("Vehicle Successfully parked")
                    garage.update_database()
                elif user_input == 3:
                    garage.remove_vehicle(
                        int(input("Specify lot number to remove vehicle from: ")))
                    print("Vehicle Successfully removed")
                    garage.update_database()
                elif user_input == 4:
                    break
                else:
                    raise Exception("Input value not in range")

            except Exception as e:
                print(e, "Please try again")
