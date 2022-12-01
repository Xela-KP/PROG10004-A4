from constants import *


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
                        int(input("Specify Year: "))
                    )
                    print("Vehicle Successfully Parked")
                elif user_input == 3:
                    garage.remove_vehicle(
                        int(input("Specify lot number to remove vehicle from: ")))
                    print("Vehicle Successfully Removed")
                elif user_input == 4:
                    break
                else:
                    raise Exception("Input value not in range")
                garage.update_database()

            except Exception as e:
                print(e, "Please try again")
