# https://www.sanfoundry.com/dynamic-programming-solutions-0-1-knapsack-problem/

# IMPORTS REQUIRED PACKAGES
import random
import time
# import copy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# GENERATES TEST DATA
test_items = None

# checking test data

# all set!


# DEFINES KNAPSACK SOLUTION FUNCTIONS
# recursive method
def recursive_knapsack(items, weight_capacity):
    return True

# testing recursive method
recursive_knapsack(test_items, 10)

# greedy method
def greedy_knapsack(items, weight_capacity):
    return True

# testing greedy method
greedy_knapsack(test_items, 10)

# dynamic programming method
def dp_knapsack(items, weight_capacity):
    return True

# testing dynamic programming
dp_knapsack(test_items, 10)


# TIME TESTING
def dp_showcase_time_testing(function_name, method_name):
  start = time.perf_counter()
  items_to_take = function_name(test_items, 10)
  end = time.perf_counter()
  function_time = (end - start)*1000
  results.append({'Method':method_name
                      ,'List of Items to Take':items_to_take
                      ,'Value of Items Taken':sum([items[x][value] for x in items_to_take])
                      ,'Function Time':function_time})

# instantiates results data structure
results = []

# runs time testing
dp_showcase_time_testing(recursive_knapsack, 'Recursive')
dp_showcase_time_testing(greedy_knapsack, 'Greedy')
dp_showcase_time_testing(dp_knapsack, 'Dynamic Programming')

# organizes results into pandas dataframe for easier exploration
results_df = pd.DataFrame(results)


# RESULTS ANALYSIS

# results_melted = pd.melt(results_df, id_vars='Method Used'
#                         , var_name="Result Type", value_vars=["Number of Stops", "Total Driving Time"]
#                         , value_name="Values")

# sns.set(style="darkgrid")
# ax = sns.barplot(x="Result Type", y="Values", hue = "Method Used", data=results_melted)
# for col in ax.patches:
#     height = col.get_height()
#     ax.text(col.get_x()+col.get_width()/2., height + 1.5,
#             int(height), ha="center") 
# plt.show()
