'''Assignment 4: CRUD Application
PROG10004 Fall 2022

Program:
module contains resource
'''
from constants import MAKE, MODEL, YEAR, COLOR


class Vehicle:
    """A resource to be managed and maintained by the program"""

    def __init__(self, make: str, model: str, year: int, color: str) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __repr__(self) -> str:
        return """
{} {} {} {}
""".format(self.color, self.year, self.make, self.model)

    def get_vehicle_information(self) -> dict:
        return {
            MAKE: self.make,
            MODEL: self.model,
            YEAR: self.year,
            COLOR: self.color
        }

    def update_color(self, color: str) -> None:
        self.color = color
