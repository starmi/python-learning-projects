# How to manipulate DataFrames and make transformations
# Dataset: https://www.ars.usda.gov/northeast-area/beltsville-md/beltsville-human-nutrition-research-center/nutrient-data-laboratory/docs/sr28-download-files/
import pandas

food_info = pandas.read_csv("food_info.csv")
#attributes on pandas DataFrame objects: pandas.shape; pandas.columns; pandas.loc[]; pandas.head()
#methods: index.tolist()

# col_names = food_info.columns.tolist()
# print(col_names)
# print(food_info.head(3))


## 2: Transforming a Column
# sodium_grams = food_info["Sodium_(mg)"] / 1000
# sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

## 3: Math with multiple columns
# grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
# milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]

## 4: Nutritional index
# score = 2 x (Protein_(g)) - 0.75 x (Lipid_Tot_(g))

# weighted_protein = 2 * food_info["Protein_(g)"]
# weighted_fat = -0.75 * food_info["Lipid_Tot_(g)"]
# initial_rating = weighted_protein + weighted_fat
# print(initial_rating.head(10))

## 5: Normalizing columns in a Dataset
#Series.max() method to get the largest value in the column
max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"] / max_protein
max_fat = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / max_fat

## 6: Creating a new column
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

## 7: Normalized nutritional index
food_info["Norm_Nutr_Index"] = (2 * food_info["Normalized_Protein"]) + (-0.75 * food_info["Normalized_Fat"])


## 8: Sorting a DataFrame per column.
## http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
food_info.sort_values("Norm_Nutr_Index", ascending = False, inplace = True)
print(food_info.head(5))
