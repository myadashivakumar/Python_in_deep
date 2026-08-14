import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports',sep = ',')

print(ufo.City) #get one serie  equlas to print(ufo['City'])

print(ufo.columns) #Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object') columns list

print(len(ufo.index)) #length faster way

print(ufo.shape[0]) #length 
