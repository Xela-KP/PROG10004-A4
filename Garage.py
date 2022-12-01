'''Assignment 4: CRUD Application
PROG10004 Fall 2022

Garage:
module acts as CRUD manager and
storage for resource.
Handles conversion of data, and updates the database
'''
from Vehicle import Vehicle
from constants import *
import io
import json
import os


class Garage:
    """Acts as the storage and management for a resource <Vehicle>"""

    def __init__(self, vehicles={}) -> None:
        self.vehicles = vehicles
        if not vehicles == {}:
            self.load_vehicles()
        self.max_occupancy = 5

    def __repr__(self) -> str:
        collection = ""
        for lot_number, vehicle in self.vehicles.items():
            collection += """
Lot: {}
    Make: {}
    Model: {}
    Year: {}
""".format(lot_number,
                vehicle.make,
                vehicle.model,
                vehicle.year)
        if not collection:
            return "Garage is empty"
        return collection

    def add_vehicle(self, make, model, year) -> None:
        if len(self.vehicles) >= 5:
            raise Exception("Max Occupancy Reached")
        lots = ['1', '2', '3', '4', '5']
        lots_used = set(self.vehicles.keys())
        available_lots = [lot for lot in lots if lot not in lots_used]
        self.vehicles[available_lots[0]] = Vehicle(make, model, year)
        self.vehicles = dict(sorted(self.vehicles.items()))

    def remove_vehicle(self, lot_number) -> None:
        if lot_number < 1 or 5 < lot_number:
            raise Exception("No such lot exists")
        if not str(lot_number) in self.vehicles.keys():
            raise Exception("No vehicle parked in specified lot")
        self.vehicles.pop(str(lot_number))

    def load_vehicles(self) -> None:
        for lot_number, vehicle_spec in self.vehicles.items():
            self.vehicles[lot_number] = Vehicle(
                vehicle_spec[MAKE], vehicle_spec[MODEL], vehicle_spec[YEAR])

    def update_database(self) -> None:
        new_garage = {}
        for lot_number, vehicle in self.vehicles.items():
            new_garage[lot_number] = {MAKE: vehicle.make,
                                      MODEL: vehicle.model, YEAR: vehicle.year}
        with io.open(os.path.join(ROOT, DB_NAME), 'w') as database:
            database.write(json.dumps(new_garage))
