
import csv
import numpy as np
import os

from datetime import date
from time import sleep, time

import bluerobotics_navigator as navigator


def isScannable(vehicle, cmds, missionlist) -> bool:
    return vehicle.armed or cmds.next <= len(missionlist)


def main() -> None:
    print("Navigator initialization...")
    navigator.init()
    print("Navigator initialized")
    navigator.set_led(navigator.UserLed.Led1, True)

    # Initialize data lists
    lat = np.array([])
    lon = np.array([])
    topo = np.array([])
    today = date.today().strftime("%b-%d-%Y")

    # Create and initialize csv file
    csvfile = open(os.getcwd() + "/Data/navigator/" + today + ".csv", "w")
    writer = csv.writer(csvfile)
    _header = ["Latitude", "Longitude", "Depth_in_Feet"]
    writer.writerow(_header)

if __name__ == "__main__":
    main()