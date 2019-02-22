'''
Reads SNname, type, SNra, and SNdec columns from SwiftSNweblist.csv
- still need to figure out how to append name to df
'''

import numpy as np
import pandas

# works, but SNname is an array
df = pandas.read_csv('SwiftSNweblist.csv', usecols= ['type', 'SNra', 'SNdec'])

SNname = np.genfromtxt('SwiftSNweblist.csv', delimiter=',',dtype = str, usecols=(0), unpack=True)

'''
# append SNname into dataframe
df = pandas.DataFrame({'Name': SNname, 'Type' : SNtype, 'ra': SNra, 'dec': SNdec}, list(range(805)))
'''

#replace empty with Nan
df = df.replace(r'^\s*$', np.nan, regex=True) 

#drop rows with Nan in SNra or SNdec columns
df = df.dropna(subset=['SNra', 'SNdec']) 

# reset the index from 0
df = df.reset_index(drop=True)

# delete header row
df = df.drop(df.index[0])

#delete /t
df = df.replace(r'\s', '', regex = True)

# take each column out of the dataframe
SNtype = df.type
SNra = df.SNra
SNdec = df.SNdec
