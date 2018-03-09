"""
Science AOP
Verison 0.2

"""

# 2d array, 3 rows, 2 collumns to hold the 3 in and out times for the week
times_in_out = [[570883306.09, 570883681.47],
                [571222176.41, 571222552.84],
                [571477770.88, 571478148.96]]

#           [start, stop, closest_app]
blackbody_1 = [1234, 45678, 6789]
blackbody_2 = [1234, 45678, 6789]
cities = [[1000, 3000, 2000], [4000, 6000, 5000]]

time_command = []  # 2D array, holds commands and times

camera_status = False

blackbody_status = False

pics_taken = 2 + len(cities)

commands = [["camera_on", "camera_on_cmd-"],
            ["camera_off", "camera_off_cmd-"],
            ["sync_mode", "sync_mode_cmd-"],
            ["data_mode", "data_mode_cmd-"],
            ["SetQbo", "SetQboCmd"],
            ["LatLongSunMode", "LLSunMode_cmd-"],
            ["LatLongDataCommand", "LLData_cmd-"],
            ["DO_FFC", "DO_FFC_cmd-"],
            ["black_body_capture", "bb_capture_cmd-"],
            ["command_fcc", "cmd_fcc_cmd-"],
            ["capture_picture", "capture_pic_cmd-"]]


def run_start_stop():
    builder()
    global time_command
    time_command = []


def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)


def builder():
    # Blackbody 1

    try:
        add("LatLongSunMode", blackbody_1[2] - 70)
        add("LatLongDataCommand", blackbody_1[2] - 70)
        add("DO_FFC", blackbody_1[2] - 1)
        add("black_body_capture", blackbody_1[2])
        global blackbody_status
        blackbody_status = True
        # add("LatLongSunMode", blackbody_1[2] + 1)
        # add("LatLongDataCommand", blackbody_1[2] + 1)
    except NameError:
        print("Blackbody 1 doesn't exist.")

    for prev, city, next_city in neighborhood(cities):
        if city[2] == cities[0][2]:  # If it's the first city
            if (cities[0][0] - blackbody_1[2]) > 70:  # Then check if the time between the the city and the...
                # ...blackbody is greater than 45
                add("LatLongSunMode", city[2] - 70)
                add("LatLongDataCommand", city[2] - 70)

            else:
                add("LatLongSunMode", blackbody_1[2] + 1)
                add("LatLongDataCommand", blackbody_1[2] + 1)

            add("DO_FFC", city[2] - 1)
            add("capture_picture", city[2])

        elif city[2] == cities[-1][2]:  # if a city is the last city...
            if (blackbody_2[0] - cities[-1][2]) > 70:  # Then check if the time between the the city and the...
                # ...blackbody is greater than 45
                add("LatLongSunMode", blackbody_2[0] - 70)
                add("LatLongDataCommand", blackbody_2[0] - 70)

            else:
                add("LatLongSunMode", city[2] + 1)
                add("LatLongDataCommand", city[2] + 1)

            add("DO_FFC", city[2] - 1)
            add("capture_picture", city[2])

        else:

            if (next_city[0] - city[2]) > 45:  # Then check if the time between the the city and the...
                # ...following city is greater than 45
                add("LatLongSunMode", next_city[0] - 45)
                add("LatLongDataCommand", next_city[0] - 45)

            else:
                add("LatLongSunMode", city[2] + 1)
                add("LatLongDataCommand", city[2] + 1)

            add("DO_FFC", city[2] - 1)
            add("capture_picture", city[2])




            # Blackbody 2
    try:
        add("LatLongSunMode", blackbody_2[2] - 70)
        add("LatLongDataCommand", blackbody_2[2] - 70)
        add("DO_FFC", blackbody_2[2] - 1)
        add("black_body_capture", blackbody_2[2])
        # global blackbody_status
        blackbody_status = True
        add("transfer_to_obc", blackbody_2[2] + 70)
        add("camera_off", blackbody_2[2] + 70 + pics_taken * 30 + 10)  # 30 seconds per picture, 10 sec buffer
    except NameError:
        print("Blackbody 2 doesn't exist.")

    print_times()


def print_times():
    print("COMMAND\t\tTIME")
    print("----------------------------")
    for x, y in time_command:
        print(x + "\t" + y + "\n")
    print("\n")


def add(command_name, time):
    """ss
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

        time_command.append([hard, str(time)])
    except:
        return False


run_start_stop()
