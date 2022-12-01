from constants import MAKE, MODEL, YEAR


class Vehicle:
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
