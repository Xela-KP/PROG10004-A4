from Program import Program
import io
import json
import os
from constants import *
from Garage import Garage

if __name__ == "__main__":
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        with open(DB_NAME) as database:
            Program.run(Garage(json.load(database)))
    else:
        with io.open(os.path.join(ROOT, DB_NAME), 'w') as database:
            database.write(json.dumps({}))
        Program.run(Garage({}))
