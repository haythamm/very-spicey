from spacetrack import SpaceTrackClient
import spiceypy as spice
import sys
import time
import os
class tle_to_bsp:
    def login():    #Logs user into space-track, using either default or temporary account.
        choice = input("Would you like to use the default Space-Track login? (y/n): ")
        while choice != 'y' and choice != 'n' and choice !='':  # asks again if input is invalid
            choice = input("Invalid input, please enter 'y' or 'n': ")

        if choice == 'n':   #if used doesnt want to use default...
            temp_user = input("Please enter the custom Username: ") #ask for and store temporary username
            temp_pass = input("Please enter the custom Password: ") #ask for and store temporary password
            print("Logging into Space-Track using temporary account...")
            print("Authenticating...")
            st = SpaceTrackClient(identity=temp_user, password=temp_pass)
            print("Authentication Complete!")

        elif choice == 'y' or choice =='':  #if choice entered is y or blank, login with default
            print("Logging into Space-Track using default account...")
            print("Authenticating...")
            st_user = 'default_username'  # enter default spacetrack username here
            st_pass = 'default_password'  # enter default spacetrack password here
            st = SpaceTrackClient(identity=st_user, password=st_pass)
            print("Authentication Complete!")
        return st

    def noradGrab():    #Prompts user for and stores norad number.
        norad = input("Please enter a NORAD ID: ")
        if norad == '':
            norad = 25544
        return norad

    def pullAndSave(norad,st):      #pulls tle for given norad and saves as a file with date and time included
        print("Pulling TLE Data...")
        data = st.tle_latest(norad_cat_id=[norad], format='tle') #saves pulled data in var
        print("Writing to file...")
        timestr = time.strftime("_%Y-%m-%d_%H-%M-%S")
        with open('tle_' + str(norad) + timestr + '.tle', 'w') as fp:
            #for line in data:   #for every line in data var...
                # fp.write(line + '\n')
            fp.write(data)  #...write a line in the file (this can be manipulated to change formatting)

        fileName = 'tle_' + str(norad) + timestr + '.tle'
        print("File Ready!")
        print("The new TLE file is called " + fileName)
        return fileName

    def setupFile(fileName):    #Generates a setup file for mkspk
        choice = input("Would you like to use the default setup file configuration? (y/n)")
        while choice != 'y' and choice != 'n' and choice != '':  # asks again if input is invalid
            choice = input("Invalid input, please enter 'y' or 'n': ")

        if choice == 'y' or choice == '':
            f = open(fileName[:-4] + '.setup', "w+")
            #Enter Setup File Defaults Here:
            f.write("\\begindata\n")
            f.write("\tINPUT_DATA_TYPE\t\t= 'TL_ELEMENTS'\n")
            f.write("\tOUTPUT_SPK_TYPE\t\t= 10\n")
            f.write("\tTLE_INPUT_OBJ_ID\t= 25544\n")
            f.write("\tTLE_SPK_OBJ_ID\t\t= -125544\n")
            f.write("\tTLE_START_PAD\t\t= '2 days'\n")
            f.write("\tTLE_STOP_PAD\t\t= '2 days'\n")
            f.write("\tCENTER_ID\t\t\t= 399\n")
            f.write("\tREF_FRAME_NAME\t\t= 'J2000'\n")
            filePath = "/home/(username)/PycharmProjects/very-spicey/"  # Add the tle file path here
            f.write("\tLEAPSECONDS_FILE\t= '"+filePath+"kernels/naif0011.tls'\n")

            f.write("\tINPUT_DATA_FILE\t\t= " + "'" + filePath + fileName + "'\n")
            f.write("\tOUTPUT_SPK_FILE\t\t= " + "'" + filePath + fileName[:-4]+".bsp'\n")
            f.write("\tPCK_FILE\t\t\t= '" + filePath + "kernels/geophysical.ker'\n")
            f.write("\tSEGMENT_ID\t\t\t= 'mkspk setup file'\n")
            f.write("\tPRODUCER_ID\t\t\t= 'very-spicey'\n")
            f.write("\\begintext")

            print("Creating Setup File...")
            f.close()   #closes the file
        
        if choice == 'n':
            print("Please enter your data for the setup file: ")
            print("(No need to enter \' before or after a value)")

            f = open(fileName[:-4] + '.setup', "w+")
            f.write("\\begindata\n")
            f.write("\tINPUT_DATA_TYPE\t\t= " + "'" + input("Input Data Type: ") + "'\n")
            f.write("\tOUTPUT_SPK_TYPE\t\t= " + "'" + input("Output SPK Type: ")+ "'\n")
            f.write("\tTLE_INPUT_OBJ_ID\t= " + "'" + input("TLE Input Obj ID: ")+ "'\n")
            f.write("\tTLE_SPK_OBJ_ID\t\t= " + "'" + input("TLE SPK Obj ID: ")+ "'\n")
            f.write("\tTLE_START_PAD\t\t= " + "'" + input("TLE Start Pad: ")+ "'\n")
            f.write("\tTLE_STOP_PAD\t\t= "+ "'" + input("TLE Stop Pad: ")+ "'\n")
            f.write("\tCENTER_ID\t\t\t= "+ "'" + input("Center ID: ")+ "'\n")
            f.write("\tREF_FRAME_NAME\t\t= " + "'" + input("Ref Frame Name: ")+ "'\n")
            choice2 = input("Leapseconds File Path: (or press \' Enter \' for default)")
            if choice2 == '':
                choice2 = "/home/(username)/PycharmProjects/very-spicey/kernels/naif0011.tls"
            f.write("\tLEAPSECONDS_FILE\t= "+ "'" + choice2 + "'\n")
            filePath = "/home/(username)/PycharmProjects/very-spicey/"     #Add the tle file path here
            f.write("\tINPUT_DATA_FILE\t\t= " +"'" + filePath + fileName + "'\n")
            f.write("\tOUTPUT_SPK_FILE\t\t= " + "'/" + fileName[:-4]+".bsp'\n")
            choice3 = input("PCK File Path: (or press \' Enter \' for default)")
            if choice3 == '':
                choice3 = "/home/(username)/PycharmProjects/very-spicey/kernels/geophysical.ker"
            f.write("\tPCK_FILE\t\t\t= "+ "'" + choice3 + "'\n")
            f.write("\tSEGMENT_ID\t\t\t= " + "'" + input("Segment ID: ")+ "'\n")
            f.write("\tPRODUCER_ID\t\t\t= 'very-spicey'\n")
            f.write("\\begintext")

            print("Creating Setup File...")
            f.close()   #closes the file
        
        setupFileName = fileName[:-4] + ".setup"
        print("Setup File Created!")
        print("The new Setup file is called " + setupFileName)
        return setupFileName

    def convertBsp(fileName):   # asks to convert to bsp, then converts if requested
        choice = input("Would you like to convert the TLE file to a BSP? (y/n)")
        while choice != 'y' and choice != 'n' and choice != '':  #asks again if input is invalid
            choice = input("Invalid input, please enter 'y' or 'n': ")

        if choice == 'y' or choice == '':
            setupFileName = setupFile(fileName)
            print("Converting to BSP...")
            command = str("./kernels/mkspk -setup " + setupFileName)

            os.system(command)
            print("BSP File Created!")
            print("The new BSP file is called " + setupFileName[:-6] + ".bsp")

        return choice

    def main():
        print("Hello! Welcome to very-spicey.")
        print("This program pulls and saves TLE data for a specific NORAD ID \nfrom Space-Track and can convert it to a BSP file\n")

        st = login()            #logs int/authenticats spacetrack ID
        norad = noradGrab()     #assigns norad var to user input from noradGrab func.
        fileName = pullAndSave(norad,st)   #pulls tle for given norad and saves
        choice = convertBsp(fileName)
        if choice == "" or choice == 'y':
            bspName = str(fileName[:-4] + ".bsp")
        spice.furnsh("/very-spicey/" + bspName)
        spice.gfposc

    main()
