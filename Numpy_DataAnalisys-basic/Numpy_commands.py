import numpy

#Get data from csv files
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter = ",", dtype = "str")
print(len(world_alcohol))
# print(world_alcohol[:10, :])

#Boolean operations within numpy
# matrix = numpy.array([
#                     [5, 10, 15],
#                     [20, 25, 30],
#                     [35, 40, 45]
#
#         ])
# print(matrix == 25)

#Extract third column in world_alcohol and compare it to the string 'Canada'.
#Extract the first column and compare it to the string '1984'
third_column = world_alcohol[:, 2]
countries_canada = (third_column == 'Canada')

first_column = world_alcohol[:, 0]
years_1984 = first_column == '1984'

# Compare third column to 'Algeria'
# Select only the rows where Algeria is True
country_is_algeria = (third_column == 'Algeria')
country_algeria = world_alcohol[country_is_algeria, :]

# Compare first_column to the string 1986 and the third_column to 'Algeria'
is_algeria_and_1986 = (first_column == '1986') & (third_column == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]
#print(rows_with_algeria_and_1986)

##REPLACING VALUES
# Replace all instances of 1986 with 2014 and all instances of 'Wine' with 'Grog'
#copy_world_alcohol = world_alcohol
# wine_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,3] == 'Wine')
# copy_world_alcohol[wine_1986, 0] = '2014'
# copy_world_alcohol[wine_1986, 3] = 'Grog'

is_value_empty = (world_alcohol[:,4] == '')
world_alcohol[is_value_empty, 4] = '0'
#print(world_alcohol[world_alcohol[:,4] == '0', :])

## CONVERTING DATA TYPES
# astype() method
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)

## OPERATIONS ON ARRAYS: https://docs.scipy.org/doc/numpy-1.10.1/index.html
# Syntax: vector.sum(axis=[0 or 1])
# axis = 1 para sumar a lo largo de la fila y axis = 0 a lo largo de la columna
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

#Total annual alcohol consumption
canada_1986 = (first_column == '1986') & (third_column == 'Canada')
canada_1986 = world_alcohol[canada_1986, :]
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()
print(total_canadian_drinking)
