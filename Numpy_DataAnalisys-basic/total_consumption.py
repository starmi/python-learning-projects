###Calcular el consumo para cada pais:
# a) Se solicita que sea solo para el year 1989
# adicional: calcular el consumo de todos los paises

import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter = ',', dtype = 'str')

totals = {}
countries = list(set(world_alcohol[:, 2]))

year = '1989'
for country in countries:
    country_consumption = (world_alcohol[:,0] == year) & (world_alcohol[:,2] == country)
    country_consumption = world_alcohol[country_consumption, 4].astype(float)
    country_consumption = country_consumption.sum()
    totals[country] = country_consumption

###Solucion 1
# years_list = list(set(world_alcohol[:, 0]))
# country_list = list(set(world_alcohol[:,2]))
#
#
# for country in country_list:
#     for year in years_list:
#         country_consumption = (world_alcohol[:,0] == year) & (world_alcohol[:,2] == country)
#         country_consumption = world_alcohol[country_consumption, 4].astype(float)
#         country_consumption = country_consumption.sum()
#         if country not in totals:
#             totals[country] = country_consumption
#         else:
#             totals[country] += country_consumption
# print(totals)

###Solucion 2: Luego de ver la respuesta de Dataquest. Simplificacion de la solucion 1
# country_list = list(set(world_alcohol[:,2]))
#
# for country in country_list:
#     is_country = (world_alcohol[:, 2] == country)
#     country_consumption = world_alcohol[is_country, :]
#     alcohol_column = country_consumption[:, 4].astype(float)
#     totals[country] = alcohol_column.sum()
# print(totals)

### Solucion by Dataquest
# totals = {}
# is_year = world_alcohol[:,0] == "1989"
# year = world_alcohol[is_year,:]
#
# for country in countries:
#     is_country = year[:,2] == country
#     country_consumption = year[is_country,:]
#     alcohol_column = country_consumption[:,4]
#     is_empty = alcohol_column == ''
#     alcohol_column[is_empty] = "0"
#     alcohol_column = alcohol_column.astype(float)
#     totals[country] = alcohol_column.sum()

###############################################################################
################### COUNTRY THAT DRINKS THE MOST ##############################
###############################################################################
highest_value = 0
highest_key = None

for country in totals:
    if totals[country] > highest_value:
        highest_value = totals[country]
        highest_key = country
print(highest_value, highest_key)

###############################################################################
######################## CONCLUSIONS ABOUT NUMPY ##############################
###############################################################################
# You should now have a good foundation in NumPy, and in handling issues with
# your data. NumPy is much easier to work with than lists of lists, because:
#
# It's easy to perform computations on data.
# Data indexing and slicing is faster and easier.
# We can convert data types quickly.
# Overall, NumPy makes working with data in Python much more efficient. It's
# widely used for this reason, especially for machine learning.
#
# You may have noticed some limitations with NumPy as you worked through the past
# two missions, though. For example:
#
# - All of the items in an array must have the same data type. For many datasets,
# this can make arrays cumbersome to work with.
# - Columns and rows must be referred to by number, which gets confusing when
# you go back and forth from column name to column number.
# In the next few missions, we'll learn about the Pandas library, one of the most
# popular data analysis libraries. Pandas builds on NumPy, but does a better job
# addressing the limitations of NumPy.
