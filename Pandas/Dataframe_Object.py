import pandas as pd

fandango = pd.read_csv("data/fandango/fandango_score_comparison.csv")

##1: Index attribute to acces indixes directly
print(fandango.head(2))
print(fandango.index)

##2: Integer indexes to select Rows
#a) using slices: fandango[0:5]
#b) using iloc method: fandango.iloc[50]
# iloc method recieves numbers, list of integer, slices, boolean arrays
# Selec first and last rows from fandando dataset
first_last = fandango.iloc[[0, 145]]

##3: CUSTOM INDEX
# method: set_index()
# instructions: Use the pandas dataframe method set_index to assign the FILM column as the custom index for the dataframe. Also, specify that we don't want to drop the FILM column from the dataframe. We want to keep the original dataframe, so assign the new one to fandango_films.
# Display the index for fandango_films using the index attribute and the print function.
fandango_films = fandango.set_index('FILM', drop=False)
print(fandango_films.index)
