'''Assignment 4: CRUD Application
PROG10004 Fall 2022

DataPersistence:
Responsible for checking if a database is present,
and updating the database
'''
import io
import json
import os
from constants import *


def update_database(garage) -> None:
    new_garage = {}
    for lot_number, vehicle in garage.vehicles.items():
        new_garage[lot_number] = {MAKE: vehicle.make,
                                  MODEL: vehicle.model, YEAR: vehicle.year}
    with io.open(os.path.join(ROOT, DB_NAME), 'w') as database:
        database.write(json.dumps(new_garage))


def check_database() -> bool:
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        with open(DB_NAME) as database:
            return json.load(database)
    with io.open(os.path.join(ROOT, DB_NAME), 'w') as database:
        database.write(json.dumps({}))
    return {}
