#http://www.astropy.org/astropy-tutorials/plot-catalog.html
import numpy as np
import pandas

import matplotlib.pyplot as plt
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
degreeSets = []
degreeRA = []
degreeDEC = []

for i in range(1,len(ra)):
  c = SkyCoord(ra[i], dec[i], unit=(u.hour, u.degree))
  degreeRA.append(c.ra)
  degreeDEC.append(c.dec)
  #degreeRA.append(c.ra.radians)
  #degreeDEC.append(c.dec.radians)
  degreeSets.append(c)

#degreeRA = np.asarray(degreeRA)
#degreeDEC = np.asarray(degreeDEC)
print(degreeRA)

'''
# from website
ra = coord.Angle(SNra, u.hour)
print("angle success")
print(ra)
ra = ra.degree
print("degree success")
print(ra)
ra = ra.wrap_at(180*u.degree)
print("wrap success")
print(ra)
dec = coord.Angle(SNdec*u.degree)

# graphing
#ra = ra.wrap_at(180*u.degree)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(degreeRA, degreeDEC)
'''
