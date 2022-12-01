'''Assignment 4: CRUD Application
PROG10004 Fall 2022

main:
module checks for existing database, and runs program
based on whether or not the database exists or not
'''
from Program import Program
import io
import json
import os
from constants import *
from Garage import Garage

if __name__ == "__main__":
    """Runs initial check and looks for a database,
    if none is present, create a new one and run the program"""
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        with open(DB_NAME) as database:
            Program.run(Garage(json.load(database)))
    else:
        with io.open(os.path.join(ROOT, DB_NAME), 'w') as database:
            database.write(json.dumps({}))
        Program.run(Garage())
