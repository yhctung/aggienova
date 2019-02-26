#http://www.astropy.org/astropy-tutorials/plot-catalog.html

import numpy as np
import math as m                          # for radians
import matplotlib.pyplot as plt           # for graphing
import pandas                             # for dataframes
from astropy import units as u
from astropy.coordinates import SkyCoord

# read data into dataframe
df = pandas.read_csv('SwiftSNweblist.csv', usecols= ['type', 'ra', 'dec'])

#replace empty and random with Nan
df = df.replace(r'^\s*$', np.nan, regex=True) 
df = df.replace(r'ra', np.nan, regex=True) 
df = df.replace(r'Unk', np.nan, regex=True) 

#drop rows with Nan
df = df.dropna(subset=['type','ra', 'dec']) 

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

# for color coding
Ia = []   # red
Ibc = []  # green
II = []   # blue
other = []
SNcolor = []

for i in range(1,len(type)):
  current = type[i]
  if "Ia" in current:
    Ia.append(i)
    SNcolor.append('red')
  elif "Ib" in current:
    Ibc.append(i)
    SNcolor.append('green')
  elif "Ic" in current:
    Ibc.append(i)
    SNcolor.append('green')  
  elif "II" in current:
    II.append(i)
    SNcolor.append('blue')   
  else:
    other.append(i)
    #SNcolor.append('temp')
    ra.drop(index = i)
    dec.drop(index = i)

SNcolor = np.asarray(SNcolor)

# converting to radians
radianRA = []
radianDEC = []

for i in range(1,len(ra)):
  c = SkyCoord(ra[i], dec[i], unit=(u.hour, u.degree))
  c.ra.wrap_angle = 180 * u.deg
  radianRA.append(m.radians(c.ra.degree))
  radianDEC.append(m.radians(c.dec.degree))

# convert list to array
radianRA = np.asarray(radianRA)
radianDEC = np.asarray(radianDEC)

# graphing
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(radianRA, radianDEC, color = SNcolor)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
fig.savefig("map.pdf")

