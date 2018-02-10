
from datetime import datetime


# 2d array, 3 rows, 2 collumns to hold the 3 in and out times for the week
times_in_out = [[570883306.09, 570883681.47],
                [571222176.41, 571222552.84],
                [571477770.88, 571478148.96]]

time_command = []   # 2D array, holds commands and times

commands = [["turn_on_pa", "----"],
            ["sync_mode", "----"],
            ["data_made", "----"],
            ["SetQbo", "SetQboCmd"],
            ["LatLongSunMode", "LatLongDataCommand"],
            ["sband_on", "PDM-N_on"],
            ["transmit", "----"],
            ["populate_transm_buffer", "----"],
            ["stop_transmit", "----"],
            ["sband_off", "PDM-N_off"]]


def run_start_stop():
    for x, y in times_in_out:
        builder(x, y)
        global time_command
        time_command = []


def builder(start, stop):
    duration = stop-start
    add("SetQbo", start-100)
    add("LatLongDataCommand", start-10)
    add("sband_on", start-7)
    add("turn_on_pa", start-6)
    add("sync_mode", start-5)
    add("populate_transm_buffer", start-5)  # -
    add("data_mode", start-5)   # -
    add("transmit", start)
    add("stop_transmit", stop)
    add("sband_off", stop + 1)
    print_times(start, stop)


def open_file():
    filename = "S-Band_AOP_" + str(datetime.now())


def close_file():
    pass


def print_times(start, stop):
    print("ENTER: " + str(start) + "\tEXIT: " + str(stop))
    print("COMMAND\t\tTIME")
    print("----------------------------")
    for x, y in time_command:
        print(x + "\t" + y + "\n")
    print("\n")

def add(command_name, time):
    """
    Writes given command and time to the schedule file.
    :param command_name: Easyname for command
    :param time: time to run that command.
    :return: True/False depending on success
    """
    try:
        for easy, hard in commands:
            if command_name == easy:
                hard_command = hard
                break
        time_command.append([hard_command, str(time)])
    except:
        return False

run_start_stop()
