'''Assignment 4: CRUD Application
PROG10004 Fall 2022

main:
module checks for existing database, and runs program
based on whether or not the database exists or not
'''
from Program import Program
from constants import *
from Garage import Garage
from DataPersistence import check_database

if __name__ == "__main__":
    """Runs initial check and looks for a database,
    if none is present, create a new one and run the program"""
    Program.run(Garage(check_database()))
