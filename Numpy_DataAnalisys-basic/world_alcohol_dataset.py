import numpy

#data source: http://apps.who.int/gho/data/node.main.A1025?lang=en?showonly=GISAH
dataset = numpy.genfromtxt("world_alcohol_original.csv", delimiter = ",", dtype = "str", skip_header = 1)

## Seleccionar solo los years 1984, 1985, 1986, 1987 y 1989
select_years = (dataset[:, 0] == "1984") | (dataset[:, 0] == "1985") | (dataset[:, 0] == "1986") | (dataset[:, 0] == "1987") | (dataset[:, 0] == "1989")
select_years = dataset[select_years, :]

## Eliminar las filas cuyas columnas de bebidas sean igual a ALL TYPES
delete_all_type_rows = (select_years[:, 3] != "All types")
delete_all_type_rows = select_years[delete_all_type_rows, :]
dataset = delete_all_type_rows

## Cambiar filas que contengan "Other alcoholic beverages" por "Other"
change_beverage_name = (dataset[:,3] == "Other alcoholic beverages")
dataset[change_beverage_name, 3] = "Other"

## Reemplazar cadenas vacias por 0 en la columna de indices
empty_strings = (dataset[:,4] == '')
dataset[empty_strings,4] = '0'

numpy.savetxt("world_alcohol.csv", dataset, fmt = "%s", delimiter = ",")
