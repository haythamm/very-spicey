import sys
import os
import spiceypy as spice
spice.furnsh("kernels/geophysical.ker")
from datetime import datetime
from spacetrack import SpaceTrackClient
from params import *
#from db import Database
import numpy as np
from plotly.offline import init_notebook_mode, plot
from plotly.graph_objs import Scatter3d, Line, Data, Layout
import spiceypy as spice
import math
import csv
init_notebook_mode()

DB_NAME = 'satellites'
ref_frame = 'IAU_EARTH'
ref_body = 'EARTH'
sec_factor = 1
et_search_error = 60 # +/- error in seconds when searching for EE indexes

st_login = 'kolby.devery@yahoo.com'
st_pass = 'Thisisaverylongcode'

# ASU Ground Station variables
gs_spk = "kernels/ASU_gs/ASUGS.bsp"
gs_tf = "kernels/ASUGS.tf"
gs_frame = "ASU-GS_TOPO"
gs_min_el = 5.0 # Minimum angle[degrees] above the horizon for the Ground Station
gs_naif_id = "-9999999"

# Variables for the spice.gf function
gf_crdsys = "LATITUDINAL"
gf_coord = "LATITUDE"
gf_relate = ">"
gf_refval = gs_min_el*spice.rpd()
gf_nintvals = 1000
gf_adjust = 0.0
gf_abcorr = "NONE"
gf_step = 30 # Step size for searching for windows

#Satellite Variables
satellite_norad = 25544
satellite_naif_id = str(-100000 - satellite_norad)

st = None

def sat_naif_id(norad_id):
    return (-100000 - norad_id)

def get_sat_name():
    print('Satellite Name: ')
    name = sys.stdin.readline()
    return str(name).rstrip()

def get_sat_norad():
    print('Satellite NORAD: ')
    norad = sys.stdin.readline()
    return int(norad)

def get_tle(norad_id):
    # Only logs in once...
    global st
    print("\n")
    if(st == None):
        print("Logging into space-track.com...")
        st = SpaceTrackClient(st_login, st_pass)
    print("Retreiving TLE information for NORAD ID " + str(norad_id))
    return st.tle_latest(norad_cat_id=norad_id, format='tle')
tle = get_tle(25544)
def create_tle(sat_name, tle_str, overwrite=False):
    tle_file = "./kernels/ISS/" + sat_name + ".tle"
    isFile = os.path.isfile(tle_file)

    if(len(tle_str) < 50):
        print("Error: incorrect TLE String")
        return
    elif(isFile and overwrite==False):
        print("Error: " + sat_name + ".tle file already exists")
        return
    elif(isFile and overwrite==True):
        print("Warning: Overwritting " + sat_name + ".tle file")
        f = open(tle_file, "w")
    else:
        f = open(tle_file, "x")

    f.write(tle_str)
    f.close()
create_tle('ISS', tle)

def create_setup(sat_name, sat_norad, overwrite=False):
    # Formatted string...
    setup_str = "\\begintext\n"
    setup_str += "  " + sat_name + " satellite .setup file for generating the kernel(.bsp)\n\n"
    setup_str += "\\begindata\n"
    setup_str += "  INPUT_DATA_TYPE     = 'TL_ELEMENTS'\n"
    setup_str += "  OUTPUT_SPK_TYPE     = 10\n"
    setup_str += "  TLE_INPUT_OBJ_ID    = " + str(sat_norad) + "\n"
    setup_str += "  TLE_SPK_OBJ_ID      = " + str(sat_naif_id(sat_norad)) + "\n"
    setup_str += "  TLE_START_PAD       = '2 days'\n"
    setup_str += "  TLE_STOP_PAD        = '10 days'\n"
    setup_str += "  CENTER_ID           = 399\n"
    setup_str += "  REF_FRAME_NAME      = 'J2000'\n"
    setup_str += "  LEAPSECONDS_FILE    = 'kernels/ISS/naif0011.tls'\n"
    setup_str += "  INPUT_DATA_FILE     = 'kernels/ISS/" + sat_name + ".tle'\n"
    setup_str += "  OUTPUT_SPK_FILE     = 'kernels/ISS/" + sat_name + ".bsp'\n"
    setup_str += "  PCK_FILE            = 'kernels/ISS/geophysical.ker'\n"
    setup_str += "  SEGMENT_ID          = 'mkspk setup file for " + sat_name + "'\n"
    setup_str += "  PRODUCER_ID         = 'ASU Ground Station'\n"
    setup_str += "\\begintext\n"

    setup_file = "./kernels/" + sat_name + ".setup"

    isFile = os.path.isfile(setup_file)
    if (isFile and overwrite == False):
        print("Error: " + sat_name + ".setup file already exists")
        return
    elif (isFile and overwrite == True):
        print("Warning: Overwritting " + sat_name + ".setup file")
        f = open(setup_file, "w")
    else:
        f = open(setup_file, "x")
    f.write(setup_str)
    f.close()
create_setup('ISS', 25544)

def create_kernel(sat_name, overwrite=False):
    bsp_file = "./kernels/" + sat_name + ".bsp"
    isFile = os.path.isfile(bsp_file)
    if (isFile and overwrite == False):
        print("Error: " + sat_name + ".bsp file already exists")
        return
    elif (isFile and overwrite == True):
        print("Warning: Removing " + sat_name + ".bsp file")
        os.system("rm " + bsp_file)
    os.system("/opt/cspice/exe/mkspk -setup kernels/ISS.setup")
create_kernel('ISS')
#
# def delete_satellite(name=None, norad=None):
#     sat_id = get_sat_id(name, norad)
#     if (sat_id == -1):
#         print("Error: Unable to find satellite in the satellite.ini file")
#         return
#     return
#
#
# def add_satellite(name=None, norad=None):
#     if (name == None):
#         sat_name = get_sat_name()
#     else:
#         sat_name = name
#     if (norad == None):
#         sat_norad = get_sat_norad()
#     else:
#         sat_norad = norad
#
#     sat_tle = get_tle(sat_norad)
#
#     index = -1
#     if (len(sat_tle) > 50):
#         index = new_sat_param(sat_name, sat_norad)
#         if (index >= 0):
#             create_tle(sat_name, sat_tle)
#             create_setup(sat_name, sat_norad)
#             print("Creating kernel...")
#             create_kernel(sat_name)
#             # TODO: add satellite to database
#     else:
#         print("Error finding TLE for " + sat_name + "(norad=" + str(sat_norad) + ")")
#     return index
#
#
# def update_tle_spk(ID):
#     params = satellite_params(ID)
#     if (params == {}):
#         print("Error: ID not in satellite.ini")
#         return
#     sat_name = params['name']
#     sat_norad = int(params['catalog_number'])
#     sat_tle = get_tle(sat_norad)
#     create_tle(sat_name, sat_tle, True)
#     create_kernel(sat_name, True)


