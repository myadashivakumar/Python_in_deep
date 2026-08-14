import pandas as pd
import timeit

data = pd.read_csv('http://bit.ly/imdbratings')

print(data[data.genre == 'Crime']) #single value filter

print(data[data.genre.isin(['Crime','Drama'])]) #multiple value filter

print(data[~data.genre.isin(['Crime','Drama'])].genre) # negative data or not in crime and drama
