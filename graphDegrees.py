'''
I am trying to follow this tutorial: http://www.astropy.org/astropy-tutorials/plot-catalog.html
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas
from astropy.wcs import WCS
import astropy.coordinates as coord
import astropy.units as u

import importlib
# get data 
importlib.import_module(readColumns)

'''
# Testing whether it works for an individual value
ra = coord.Angle(SNra[9], unit=u.hour)
print(ra.degree)
'''

# to graph
print ("Generating degrees")
raDegrees = []

for i in range(1,len(SNra)):
  ra = coord.Angle(SNra[i], unit=u.hour)
  raDegrees.append(ra.degree)

#print(*raDegrees, sep = "\n") 

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
'''

'''
# graphing
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)
'''