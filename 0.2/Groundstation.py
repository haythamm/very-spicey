
from runme import *

from Identification import *

from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import Scatter3d, Line, Data, Layout
import spiceypy as spice
import math


init_notebook_mode()

spice.furnsh("./kernels/phx_meta_k.txt")


class Groundstation(object):
    """ A groundstation object that can be run through naif
    to calculate pass times and added to a schedule.

    Attributes:
        name: Name of location
        shorthand: Shorthand notation of location name
        identification: Identification number of location
        reference_frame: Reference frame of location
        times: Time array for location
        result: Spice cell for city
        result: Spice double cell.

    """
    def __init__(self, location, shorthand):
        """Return a groundstation object with name being *location*,
                 shorthand being *shorthand*"""
        self.name = location
        self.shorthand = shorthand
        self.reference_frame = shorthand + "-00_TOPO"
        self.identification = self.set_id(location)
        self.result = spice.stypes.SPICEDOUBLE_CELL(200000)
        self.times = []
        self.three_d_plot = []

# --------------------------------- Setters
    @staticmethod
    def set_id(location):                 # Gets an id number for the Groundstation object
        id_num = Identification(location)           # Create new id object
        return id_num.generate_id()                 # Set the object's id var to the id returned by generate_id()

# --------------------------------- Getters

    def get_name(self):
        return self.name

    def get_shorthand(self):
        return self.shorthand

    def get_ref_frame(self):
        return self.reference_frame

    def get_id(self):
        return self.identification

    def get_result(self):
        return self.result

    def get_times(self):
        return self.times

# ---------------------------------

    def run_gfpos(self):

        # vars
        target = satellite_naif_id
        obsrvr = self.identification
        inframe = self.reference_frame
        crdsys = "LATITUDINAL"
        coord = "LATITUDE"
        relate = ">"
        refval = math.radians(0)
        steps = 30
        nintvals = 100000
        adjust = 0.0
        abcorr = "NONE"

        spice.wninsd(*utc, cnfine)

        spice.gfposc(target, inframe, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, steps, nintvals, cnfine,
                     self.result)
        spice.wnfetd(self.result, 0)

    def calc_positions(self):
        for i, _ in enumerate(times):
            positions.append(spice.spkpos(satellite_naif_id, self.times[i], 'IAU_EARTH', 'NONE', 'EARTH')[0])

    def print_times(self):
        print(self.name + " Access Times:")
        for time in self.times:
            t = spice.timout(time, TIMFMT)
            s = time[0]
            st = time[-1]
            # duration = (st - s)
            start = t[0]
            stop = t[-1]
            closest_approach = spice.timout((st + s) / 2, TIMFMT)
            print("Start: {}   Stop: {} Closest Approach: {}".format(start, stop, closest_approach))

    def plotter(self):
        for i, _ in enumerate(positions):
            self.three_d_plot.append(Scatter3d(
                x=positions[i][:, 0],  # X coordinates
                y=positions[i][:, 1],  # Y coordinates
                z=positions[i][:, 2],  # Z coordinates
                name=self.name,
                mode='lines',
                line=Line(width=10,
                          color='red')
            ))
