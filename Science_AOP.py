from datetime import datetime

# 2d array, 3 rows, 2 collumns to hold the 3 in and out times for the week
times_in_out = [[570883306.09, 570883681.47],
                [571222176.41, 571222552.84],
                [571477770.88, 571478148.96]]

#   [start, stop, closest_app]
blackbodies = [[1234, 45678, 6789], [1234, 45678, 6789]]  # Closest Approach
cities = [[1234, 45678, 6789], [1234, 45678, 6789]]

time_command = []  # 2D array, holds commands and times

camera_status = False
blackbody_status = False

pics_taken = len(blackbodies) + len(cities)

commands = [["camera_on", "----"],
            {"camera_off", "----"}
            ["sync_mode", "----"],
            ["data_made", "----"],
            ["SetQbo", "SetQboCmd"],
            ["LatLongSunMode", ""],
            ["LatLongDataCommand", ""]
            ["DO_FCC", "----"],
            ["black_body_capture", "----"],
            ["command_fcc", "----"],
            ["capture_picture", "----"],
            ["sband_off", "PDM-N_off"]]


#
# if (cities[0][2] - blackbodies[0][2]) > 45:
#         cities[0][2] - 45


def run_start_stop():
    for x, y in times_in_out:
        builder(x, y)
        global time_command
        time_command = []


def builder(closest_time, stop):
    for blackbody in blackbodies:  # for every blackbody but the last:
        if blackbody[2] == blackbodies[-1][
            2]:  # If the black body that we are iterating through is the lsat on, do this:
            # if not camera_status:
            #     add("camera_on", blackbody[2] - 970)
            #     global camera_status
            #     camera_status = True
            #     add("SetQbo", blackbody[2] - 970)
            add("LatLongSunMode", blackbody[2] - 70)
            add("LatLongDataCommand", blackbody[2] - 70)
            add("DO_FCC", blackbody[2] - 1)
            add("black_body_capture", blackbody[2])
            global blackbody_status
            blackbody_status = True
            add("transfer_to_obc", blackbody[2] + 70)
            add("camera_off", blackbody[2] + 70 + pics_taken * 30 + 10)  # 30 seconds per picture, 10 sec buffer
        else:  # If it isn't the last one, do this:
            if not camera_status:  # If the camera is off
                add("camera_on", blackbody[2] - 970)
                global camera_status
                camera_status = True
                add("SetQbo", blackbody[2] - 970)
            add("LatLongSunMode", blackbody[2] - 70)
            add("LatLongDataCommand", blackbody[2] - 70)
            add("DO_FCC", blackbody[2] - 1)
            add("black_body_capture", blackbody[2])
            global blackbody_status
            blackbody_status = True
            add("LatLongSunMode", blackbody[2] + 1)
            add("LatLongDataCommand", blackbody[2] + 1)

    for city in cities:
        if city[2] == cities[0][2]:  # If it's the first city
            if (cities[0][0] - blackbodies[0][2]) > 45:  # Then check if the time between the the city and the...
                # ...blackbody is greater than 45
                add("LatLongSunMode", city[0] - 45)
                add("LatLongDataCommand", city[0] - 45)
            else:
                add("LatLongSunMode", blackbodies[0][2] + 1)
                add("LatLongDataCommand", blackbodies[0][2] + 1)
        elif city[2] == cities[-1][2]:
            if (blackbodies[-1][0] - cities[-1][2]) > 45:  # Then check if the time between the the city and the...
                # ...blackbody is greater than 45
                add("LatLongSunMode", blackbodies[-1][0] - 45)
                add("LatLongDataCommand", blackbodies[-1][0] - 45)
            else:
                add("LatLongSunMode", city[2] + 1) # ----------------------------------------------------------------
                add("LatLongDataCommand", city[2] + 1)
        else:

            if (city[0]+1 - city[2]) > 45:  # Then check if the time between the the city and the...
                # ...following city is greater than 45
                add("LatLongSunMode", city[0] - 45)
                add("LatLongDataCommand", city[0] - 45)
            else:
                add("LatLongSunMode", city[2]+1  + 1)
                add("LatLongDataCommand", city[2]+1 + 1)



    print_times(closest_time, stop)


def open_file():
    filename = "S-Band_AOP_" + str(datetime.now())


def close_file():
    pass


def print_times(closest_time, stop):
    print("ENTER: " + str(closest_time) + "\tEXIT: " + str(stop))
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
