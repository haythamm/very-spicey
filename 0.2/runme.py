"""
______________  ______________________   ____________  __
___  __ \__  / / /_  __ \__  ____/__  | / /___  _/_  |/ /
__  /_/ /_  /_/ /_  / / /_  __/  __   |/ / __  / __    /
_  ____/_  __  / / /_/ /_  /___  _  /|  / __/ /  _    |
/_/     /_/ /_/  \____/ /_____/  /_/ |_/  /___/  /_/|_|

Image Pass Scheduler
Version: 0.2
Date Last Modified: 1/3/18

"""
#   Import Packages

from Identification import *
from Location import *
from Groundstation import *

import numpy as np
from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import Scatter3d, Line, Data, Layout
import spiceypy as spice
import math
from difflib import SequenceMatcher

#   Import Classes


init_notebook_mode()

# --------------------------------- Initialize Variable


TIMFMT = "YYYY MON DD HR:MN:SC.###### TDB::RND::TDB"    # Formats time from naif/Time Conversion

satellite_norad = 2544
satellite_naif_id = str(-100000 - satellite_norad)      # Generate Satellite naif ID

# Calculates window of time TLE will populate
cover = spice.utils.support_types.SPICEDOUBLE_CELL(200000)
spice.spkcov("kernels/ISS/ISS.bsp", int(satellite_naif_id), cover)
coverWIN = spice.wnfetd(cover, 0)
etStart = coverWIN[0]
etStop = coverWIN[1]

step = 100000   # 100,000
times = np.linspace(etStart, etStop, step, endpoint=False)  # Retrieve times covered by TLE

# Run spkpos as a vectorized function
positions, lightTimes = spice.spkpos('-125544', times, 'IAU_EARTH', 'NONE', 'EARTH')

# Start and stop times covered by TLE
utc = [etStart, etStop]

# gf_pos variables
cnfine = spice.stypes.SPICEDOUBLE_CELL(200000)

global current_schedule
current_schedule = []


def run_gfpos():                        # Runs gfpos for all cities in schedule.
    for location in current_schedule:
        location.run_gfpos()


def print_times():                      # Print times for all cities and ground stations in current schedule.
    for location in current_schedule:
        location.print_times()


def calc_positions():                   # Calculates positions for every location in the schedule
    for location in current_schedule:
        location.calc_positions()


def plot_all():                         # Plots passes for all locations in the schedule
    for location in current_schedule:
        location.plotter()


def display_location_db():              # Prints locations already in database.
    print("----- Cities in Database -----")
    Identification.print_dict()


def full_info_array():      #May not need this
    for key,val in location_ids:
        num = 0
        location = key
        ident = val



def similar(location):  # If not in array, checks if there is a similar one and returns it.
    if location not in location_ids:        # If the given location is not in the array...
        option = ""                         # Initialize option variable
        for f in location_ids:              # For every location in location_ids...
            if SequenceMatcher(None, f, location).ratio() > 0.80:   # ...if it's 80% similar or more...
                option = option + "\n" + f  # ...add it to the list of possible options
        print(option)
        choice = input("This location is not in the database, did you mean one of the above? (y/n) ")
        if choice == 'y' or "":
            return option
        if choice == 'n':
            choice = input("Would you like to add it as a new location? (y/n) ")
            if choice == 'y' or "":
                exec(location + "= Identification(" + location + ")")   # Creates new identification object with the...
                # ...given location as the name of the ID object and location of the new ID object.
                return exec(location + ".get_id")   # Return the generated ID.

def clear_schedule():
    global current_schedule
    current_schedule = []

def schedule_creator():                 # Builds a location schedule.
    print("----- Schedule Builder -----")
    print("")
    print("(1) Clear the current schedule.")
    print("(2) View the current schedule.")
    print("(3) Append the current schedule.")
    print("(4) Create a new schedule.")
    print("(5) Calculate Times.")
    print("(6) Add city to database.")
    print("(7) Quit.")

    choice = input("Please choose an option: ")
    while choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5 or choice != 6 or choice != 7:
        choice = input("Please choose a number 1-5: ")
    while choice != 6:
        if choice == 1:
            clear_schedule()
        elif choice == 2:
            print(current_schedule)
        elif choice == 3:       # Appends the current_schedule
            display_location_db()
            print("----- Current Schedule -----")
            print(current_schedule)
            choice = 'y'
            while choice == 'y' or '':
                city_to_add = input('Type in a city to add to the schedule: ')
                if city_to_add not in location_ids:
                    loc_id = similar(city_to_add)
                    global current_schedule
                    current_schedule = np.append(loc_id)
                choice = input('Would you like to add another city? (y/n) ')
            print("Done!")
        elif choice == 4:
            print("Clearing current schedule...")
            clear_schedule()
            display_location_db()
            choice = 'y'
            while choice == 'y' or '':
                city_to_add = input('Type in a city to add to the schedule: ')
                if city_to_add not in location_ids:
                    loc_id = similar(city_to_add)
                    global current_schedule
                    current_schedule = np.append(loc_id)
                choice = input('Would you like to add another city? (y/n) ')
            print("Done!")
        elif choice == 5:
            main()
        elif choice == 6:
            pass
        elif choice == 7:
            break

    display_location_db()               # Displays cites and IDs already in the database
    choice = 'y'
    while choice == 'y' or '':
        city_to_add = input('Type in a city to add to the schedule: ')
        if city_to_add not in location_ids:
            loc_id = similar(city_to_add)
            global current_schedule
            current_schedule = np.append(loc_id)
        choice = input('Would you like to add another city? (y/n) ')
    print("Done!")



def main():
    gs = Groundstation("ASU", "ASU")
    gs.run_gfpos()
    print_times()
    plot_all()

