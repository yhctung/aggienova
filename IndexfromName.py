import numpy as np
import pandas

# reading all the data
df = pandas.read_csv('SwiftSNweblist.csv', header = 1)
df = df.replace(r'^\s*$', np.nan, regex=True)

# functions 

def getIndex(name):
  # to see entire row with name
  #a = df.loc[df.eq(name).any(axis=1)]
  index = df[df['SNname']==name].index.values.astype(int)
  return index
  
def main():
    name = input("What is the name of the supernova: ")
    index = getIndex(name)

# running the program
main()
