'''Assignment 4: CRUD Application
PROG10004 Fall 2022

Program:
module contains resource
'''
from constants import MAKE, MODEL, YEAR


class Vehicle:
    """A resource to be managed and maintained by the program"""

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_vehicle_information(self) -> dict:
        return {
            MAKE: self.make,
            MODEL: self.model,
            YEAR: self.year,
        }
