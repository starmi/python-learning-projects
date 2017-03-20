import pandas as pd
fandango = pd.read_csv("data/fandango/fandango_score_comparison.csv")

##1: INTEGER INDEXES
#Select the FILM and RottenTomatoes column then print their first 5 values
series_film = fandango['FILM']
#print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
#print(series_rt[0:5])

##2: CUSTOM INDEXES
#instructions:
#1) Build a new Series with film name as string index and rottentomatoes score as column.
#2) Find Minios (2015) and Leviathan (2014) scores
# to create a series object see: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html#pandas.Series

from pandas import Series

series_custom = Series(data=series_rt.values, index=series_film.values, name='RT_Scores')
#print(series_custom[['Minions (2015)', 'Leviathan (2014)']])

#When it comes to indexes, Series objects act like both dictionaries and lists.
#We can access values with our custom index (like the keys in a dictionary), or
#the integer index (like the index in a list).

##3: REINDEXING
original_index = series_custom.index
list_index = original_index.tolist()
sorted_index = sorted(list_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index[0:5])
