from spacetrack import SpaceTrackClient
import time
import os

proj_filepath = "/home/rojo/PycharmProjects/very_spicey_0.2/"


def login():  # Logs user into space-track, using either default or temporary account.
    choice = input("Would you like to use the default Space-Track login? (y/n): ")
    while choice != 'y' and choice != 'n' and choice != '':  # Asks again if input is invalid
        choice = input("Invalid input, please enter 'y' or 'n': ")

    if choice == 'n':  # If used doesnt want to use default...
        temp_user = input("Please enter the custom Username: ")  # Ask for and store temporary username
        temp_pass = input("Please enter the custom Password: ")  # Ask for and store temporary password
        print("Logging into Space-Track using temporary account...")
        print("Authenticating...")
        st = SpaceTrackClient(identity=temp_user, password=temp_pass)
        print("Authentication Complete!")

    elif choice == 'y' or choice == '':  # If choice entered is y or blank, login with default
        print("Logging into Space-Track using default account...")
        print("Authenticating...")
        st_user = 'hmouti@asu.edu'  # Enter default spacetrack username here
        st_pass = 'WelcomeToTheGalaxy5'  # Enter default spacetrack password here
        st = SpaceTrackClient(identity=st_user, password=st_pass)
        print("Authentication Complete!")
    return st


def get_norad():  # Prompts user for and stores norad number.
    norad = input('Please enter a NORAD ID: ')
    if norad == '':
        norad = 25544
    return norad


def pull_save_tle(norad, st):  # pulls tle for given norad and saves as a file with date and time included
    print("Pulling TLE Data...")
    data = st.tle_latest(norad_cat_id=[norad], format='tle')  # saves pulled data in var
    print("Writing to file...")
    timestr = time.strftime("_%Y-%m-%d_%H-%M-%S")
    with open('tle_' + str(norad) + timestr + '.tle', 'w') as fp:
        # for line in data:   #for every line in data var...
        # fp.write(line + '\n')
        fp.write(data)  # ...write a line in the file (this can be manipulated to change formatting)

    filename = 'tle_' + str(norad) + timestr + '.tle'
    print("File Ready!")
    print("The new TLE file is called " + filename)
    return filename


def setupfile(filename):  # Generates a setup file for mkspk
    choice = input("Would you like to use the default setup file configuration? (y/n)")
    while choice != 'y' and choice != 'n' and choice != '':  # asks again if input is invalid
        choice = input("Invalid input, please enter 'y' or 'n': ")

    if choice == 'y' or choice == '':
        f = open(filename[:-4] + '.setup', "w+")
        # Enter Setup File Defaults Here:
        f.write("\\begindata\n")
        f.write("\tINPUT_DATA_TYPE\t\t= 'TL_ELEMENTS'\n")
        f.write("\tOUTPUT_SPK_TYPE\t\t= 10\n")
        f.write("\tTLE_INPUT_OBJ_ID\t= 25544\n")
        f.write("\tTLE_SPK_OBJ_ID\t\t= -125544\n")
        f.write("\tTLE_START_PAD\t\t= '2 days'\n")
        f.write("\tTLE_STOP_PAD\t\t= '2 days'\n")
        f.write("\tCENTER_ID\t\t\t= 399\n")
        f.write("\tREF_FRAME_NAME\t\t= 'J2000'\n")
        file_path = proj_filepath   # Add the tle file path here
        f.write("\tLEAPSECONDS_FILE\t= '" + file_path + "kernels/naif0011.tls'\n")

        f.write("\tINPUT_DATA_FILE\t\t= " + "'" + file_path + filename + "'\n")
        f.write("\tOUTPUT_SPK_FILE\t\t= " + "'" + file_path + filename[:-4] + ".bsp'\n")
        f.write("\tPCK_FILE\t\t\t= '" + file_path + "kernels/geophysical.ker'\n")
        f.write("\tSEGMENT_ID\t\t\t= 'mkspk setup file'\n")
        f.write("\tPRODUCER_ID\t\t\t= 'very-spicey'\n")
        f.write("\\begintext")

        print("Creating Setup File...")
        f.close()  # closes the file

    if choice == 'n':
        print("Please enter your data for the setup file: ")
        print("(No need to enter \' before or after a value)")

        f = open(filename[:-4] + '.setup', "w+")
        f.write("\\begindata\n")
        f.write("\tINPUT_DATA_TYPE\t\t= " + "'" + input("Input Data Type: ") + "'\n")
        f.write("\tOUTPUT_SPK_TYPE\t\t= " + "'" + input("Output SPK Type: ") + "'\n")
        f.write("\tTLE_INPUT_OBJ_ID\t= " + "'" + input("TLE Input Obj ID: ") + "'\n")
        f.write("\tTLE_SPK_OBJ_ID\t\t= " + "'" + input("TLE SPK Obj ID: ") + "'\n")
        f.write("\tTLE_START_PAD\t\t= " + "'" + input("TLE Start Pad: ") + "'\n")
        f.write("\tTLE_STOP_PAD\t\t= " + "'" + input("TLE Stop Pad: ") + "'\n")
        f.write("\tCENTER_ID\t\t\t= " + "'" + input("Center ID: ") + "'\n")
        f.write("\tREF_FRAME_NAME\t\t= " + "'" + input("Ref Frame Name: ") + "'\n")
        choice2 = input("Leapseconds File Path: (or press \' Enter \' for default)")
        if choice2 == '':
            choice2 = proj_filepath + "kernels/naif0011.tls"
        f.write("\tLEAPSECONDS_FILE\t= " + "'" + choice2 + "'\n")
        file_path = proj_filepath   # Add the tle file path here
        f.write("\tINPUT_DATA_FILE\t\t= " + "'" + file_path + filename + "'\n")
        f.write("\tOUTPUT_SPK_FILE\t\t= " + "'/" + filename[:-4] + ".bsp'\n")
        choice3 = input("PCK File Path: (or press \' Enter \' for default)")
        if choice3 == '':
            choice3 = proj_filepath + "kernels/geophysical.ker"
        f.write("\tPCK_FILE\t\t\t= " + "'" + choice3 + "'\n")
        f.write("\tSEGMENT_ID\t\t\t= " + "'" + input("Segment ID: ") + "'\n")
        f.write("\tPRODUCER_ID\t\t\t= 'very-spicey'\n")
        f.write("\\begintext")

        print("Creating Setup File...")
        f.close()  # closes the file

    setup_filename = filename[:-4] + ".setup"
    print("Setup File Created!")
    print("The new Setup file is called " + setup_filename)
    return setup_filename


def convert_bsp(filename):  # asks to convert to bsp, then converts if requested
    choice = input("Would you like to convert the TLE file to a BSP? (y/n)")
    while choice != 'y' and choice != 'n' and choice != '':  # asks again if input is invalid
        choice = input("Invalid input, please enter 'y' or 'n': ")

    if choice == 'y' or choice == '':
        setup_filename = setupfile(filename)
        print("Converting to BSP...")
        command2 = str("chmod u+x tle_to_bsp.py")
        command = str("./kernels/mkspk -setup " + setup_filename)

        os.system(command2)
        os.system(command)
        print("BSP File Created!")
        print("The new BSP file is called " + setup_filename[:-6] + ".bsp")

    return choice


def main():
    print("Hello! This is TLE TO BSP.")
    print(
        "This program pulls and saves TLE data for a specific NORAD ID \nfrom Space-Track and can convert it to a "
        "BSP file\n")

    st = login()  # logs int/authenticates spacetrack ID
    norad = get_norad()  # assigns norad var to user input from get_norad func.
    filename = pull_save_tle(norad, st)  # pulls tle for given norad and saves
    choice = convert_bsp(filename)
    if choice == "" or choice == 'y':
        bsp_name = str(filename[:-4] + ".bsp")
        return bsp_name


main()
