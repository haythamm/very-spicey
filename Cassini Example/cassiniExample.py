import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import spiceypy as spice
print("Toolkit Version: " + spice.tkvrsn("TOOLKIT")) #prints version of toolkit

spice.furnsh("./cassMetaK.txt")

step = 4000

utc = ['Jun 20, 2004', 'Dec 1, 2005']   #Get positions between these two dates

etOne = spice.str2et(utc[0])    #get et values one...
etTwo = spice.str2et(utc[1])    #...and two, we could vectorize str2et
print("ET One: {}, ET Two: {}".format(etOne, etTwo))

times = [x*(etTwo-etOne)/step + etOne for x in range(step)] # get times


print(times[0:3])   #prints the first few times:

#Runs spkpos as a vectorized function
positions, lightTimes = spice.spkpos('Cassini', times, 'J2000', 'NONE', 'SATURN BARYCENTER')

# Positions is a 3xN vector of XYZ positions
print("Positions: ")
print(positions[0])

# Light times is a N vector of time
print("Light Times: ")
print(lightTimes[0])

#Graphs the stuff
fig = plt.figure(figsize=(9, 9))
ax  = fig.add_subplot(111, projection='3d')
ax.plot(positions.T[0], positions.T[1], positions.T[2])
plt.title('SpiceyPy Cassini Position Example from Jun 20, 2004 to Dec 1, 2005')
plt.show()
