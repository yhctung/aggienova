#http://www.astropy.org/astropy-tutorials/plot-catalog.html

import numpy as np
import math as m                          # for radians
import matplotlib.pyplot as plt           # for graphing
import pandas                             # for dataframes
from astropy import units as u
from astropy.coordinates import SkyCoord

# works, but SNname is an array
df = pandas.read_csv('SwiftSNweblist.csv', usecols= ['type', 'ra', 'dec'])
SNname = np.genfromtxt('SwiftSNweblist.csv', delimiter=',',dtype = str, usecols=(0), unpack=True)

#replace empty with Nan
df = df.replace(r'^\s*$', np.nan, regex=True) 
df = df.replace(r'ra', np.nan, regex=True) 

#drop rows with Nan in SNra or SNdec columns
df = df.dropna(subset=['ra', 'dec']) 

# reset the index from 0
df = df.reset_index(drop=True)

# delete header row
df = df.drop(df.index[0])

#delete /t
df = df.replace(r'\s', '', regex = True)

# take each column out of the dataframe
type = df.type
ra = df.ra
dec = df.dec

'''
print("Does it work for one value? ")
c = SkyCoord(ra[1], dec[1], unit=(u.hour, u.degree))
print(c)
'''

# to graph
print ("Generating degrees")
CoordSets = []
radianRA = []
radianDEC = []

for i in range(1,len(ra)):
  c = SkyCoord(ra[i], dec[i], unit=(u.hour, u.degree))
  radianRA.append(m.radians(c.ra.degree))
  radianDEC.append(m.radians(c.dec.degree))
  #degreeRA.append(c.ra.degree)
  #degreeDEC.append(c.dec.degree)
  CoordSets.append(c)

radianRA = np.asarray(radianRA)
radianDEC = np.asarray(radianDEC)

#print(degreeRA) # long
#print(degreeDEC) #lat

#ra = ra.wrap_at(180*u.degree)

# graphing
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(radianRA, radianDEC)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
fig.savefig("map.pdf")
