import pandas as pd

## 1: Read csv files with pandas
all_ages = pd.read_csv("data/college-majors/all-ages.csv")
recent_grads = pd.read_csv("data/college-majors/recent-grads.csv")

## 2
# Unique values in Major_category column.
# print(all_ages['Major_category'].unique())
#
# aa_cat_counts = dict()
# rg_cat_counts = dict()
#
# def major_category_counter(dataset):
#     dict_counts = {}
#     for category in dataset['Major_category'].unique():
#         is_category = dataset['Major_category'] == category
#         true_row_values = dataset[is_category]
#         dict_counts[category] = true_row_values['Total'].sum()
#     return dict_counts
#
# aa_cat_counts = major_category_counter(all_ages)
# rg_cat_counts = major_category_counter(recent_grads)

## 3: Calculate proportion of college graduates on low wage jobs
# low_wage_sum = recent_grads['Low_wage_jobs'].sum()
# recent_grads_sum = recent_grads['Total'].sum()
# low_wage_percent = float(low_wage_sum) / recent_grads_sum
# print(low_wage_percent*100, '%')

##4:
