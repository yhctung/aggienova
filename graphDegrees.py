import numpy as np
import math as m                          # for radians
import matplotlib.pyplot as plt           # for graphing
import pandas                             # for dataframes
from astropy import units as u
from astropy.coordinates import SkyCoord  # for converting

# read data into dataframe
df = pandas.read_csv('SwiftSNweblist.csv', usecols= ['type', 'ra', 'dec'])

# clean up data
df = df.replace(r'^\s*$', np.nan, regex=True)     # replace empty, random with Nan
df = df.replace(r'ra', np.nan, regex=True) 
df = df.replace(r'Unk', np.nan, regex=True) 
df = df.replace(r'\s', '', regex = True)          
df = df.dropna(subset=['type','ra', 'dec'])       # drop rows with Nan

df = df.reset_index(drop=True)                    # reset the index from 0
df = df.drop(df.index[0])                         # delete header row

# get series from dataframe columns
type = df.type
ra = df.ra
dec = df.dec

# for color coding ----------------------
# types
#Ia = []   # red
#Ibc = []  # green
#II = []   # blue
#other = []
SNcolor = []

for i in range(1,len(type)):
  current = type[i]
  if "Ia" in current:
    #Ia.append(i)
    SNcolor.append('red')
  elif "II" in current:
    #II.append(i)
    SNcolor.append('blue')  
  elif "Ib" in current:
    #Ibc.append(i)
    SNcolor.append('green')
  elif "Ic" in current:
    #Ibc.append(i)
    SNcolor.append('green')     
  else:
    #other.append(i)
    ra.drop(index = i)
    dec.drop(index = i)

SNcolor = np.asarray(SNcolor)

# graphing ------------------------------

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

# plotting
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(radianRA, radianDEC, color = SNcolor)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
fig.savefig("map.pdf")

