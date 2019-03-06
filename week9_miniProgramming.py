# https://www.sanfoundry.com/dynamic-programming-solutions-0-1-knapsack-problem/

# IMPORTS REQUIRED PACKAGES
import random
import copy
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# GENERATES TEST DATA
test_case_sizes = []
for i in range(9):
    test_case_sizes.append(3*i + 4)

weights = {}
values = {}
bag_weight_capacities = []
for size in test_case_sizes:
    random.seed(test_case_sizes[-1])
    weights['test_case_size_' + str(size)] = [random.randint(0, 30) for i in range(size)]
    values['test_case_size_' + str(size)] = [round(random.uniform(0.00, 300.00),2) for i in range(size)]
    bag_weight_capacities.append(random.randint(10,10*size))

cases = []
for test_case_num in range(len(test_case_sizes)):
    cases.append({})
    cases[test_case_num]['size'] = test_case_sizes[test_case_num]
    cases[test_case_num]['bag_weight_capacity'] = bag_weight_capacities[test_case_num]
    cases[test_case_num]['items'] = []
    for item_num in range(test_case_sizes[test_case_num]):
        cases[test_case_num]['items'].append({})
        cases[test_case_num]['items'][item_num]['weight'] = weights['test_case_size_' + str(test_case_sizes[test_case_num])][item_num]
        cases[test_case_num]['items'][item_num]['value'] = values['test_case_size_' + str(test_case_sizes[test_case_num])][item_num]
        
# checking test data
cases[0].keys()
cases[0]['size']
type(cases[0]['items'])
len(cases[0]['items'])
cases[0]['items'][3]
cases[0]['bag_weight_capacity']
sum(cases[0]['items'][x]['weight'] for x in range(len(cases[0]['items'])))
# all set!


# DEFINES KNAPSACK SOLUTION FUNCTIONS
# greedy method
def greedy_knapsack(items, weight_available):
    bag = []
    while not items or weight_available > 0:
        new_subset = [x for x in items if x['weight'] <= weight_available]
        if not new_subset:
            return bag
        current_max_value = max([x['value'] for x in new_subset])
        items_with_max_value = [x for x in new_subset if x['value'] == current_max_value]
        min_weight_among_max_value_items = min([x['weight'] for x in items_with_max_value])
        item_to_pop_index = [x for x in range(len(items)) if (items[x]['value'] == current_max_value \
            and items[x]['weight'] == min_weight_among_max_value_items)][0]
        weight_available = weight_available - items[item_to_pop_index]['weight']
        bag.append(items.pop(item_to_pop_index))
    return bag

# testing greedy method
single_test_case = copy.deepcopy(cases[0])
result_bag = greedy_knapsack(single_test_case['items'],single_test_case['bag_weight_capacity'])
len(cases[0]['items'])
len(result_bag)
cases[0]['bag_weight_capacity']
sum(x['weight'] for x in result_bag)
sum(x['value'] for x in result_bag)

# recursive method
def recursive_knapsack(items, weight_available):
    if not items or weight_available == 0:
        return []

    if items[-1]['weight'] > weight_available:
        return recursive_knapsack(items[:-1], weight_available)
    else:
        temp = recursive_knapsack(items[:-1], weight_available - items[-1]['weight'])
        return max([recursive_knapsack(items[:-1], weight_available), temp + [items[-1]]], key=lambda m: sum([x['value'] for x in m]), default = [])

# testing recursive method
single_test_case = copy.deepcopy(cases[0])
result_bag = recursive_knapsack(single_test_case['items'],single_test_case['bag_weight_capacity'])
len(cases[0]['items'])
len(result_bag)
cases[0]['bag_weight_capacity']
sum(x['weight'] for x in result_bag)
sum(x['value'] for x in result_bag)

# dynamic programming method
def dp_knapsack(items, weight_capacity):
    rows = len(items) + 1
    cols = weight_capacity + 1
    
    calcs_matrix = [[None for x in range(cols)] for y in range(rows)]
    for j in range(cols):
        calcs_matrix[0][j] = []
    for i in range(rows):
        calcs_matrix[i][0] = []
    
    for i in range(1, rows):
        for j in range(1, cols):
            if items[i-1]['weight'] <= j:
                calcs_matrix[i][j] = max(calcs_matrix[i-1][j], calcs_matrix[i-1][j-items[i-1]['weight']] + [items[i-1]]\
                    , key=lambda m: sum([x['value'] for x in m]))
            else:
                calcs_matrix[i][j] = calcs_matrix[i-1][j]
    
    return calcs_matrix[len(items)][weight_capacity]

# testing dynamic programming
single_test_case = copy.deepcopy(cases[0])
result_bag = dp_knapsack(single_test_case['items'],single_test_case['bag_weight_capacity'])
len(cases[0]['items'])
len(result_bag)
cases[0]['bag_weight_capacity']
sum(x['weight'] for x in result_bag)
sum(x['value'] for x in result_bag)


# TIME TESTING
def dp_showcase_time_testing(function_name, method_name, cases):
    for case_num in range(len(cases)):
        items = copy.deepcopy(cases[case_num]['items'])
        weight_capacity = copy.deepcopy(cases[case_num]['bag_weight_capacity'])
        start = time.perf_counter()
        items_to_take = function_name(items, weight_capacity)
        end = time.perf_counter()
        function_time = (end - start)*1000
        results.append({'Number of Items to Evaluate': len(cases[case_num]['items'])\
                        ,'Method':method_name\
                        ,'Value of Items Taken':sum([x['value'] for x in items_to_take])\
                        ,'Function Time':function_time})

# instantiates results data structure
results = []

# runs time testing
dp_showcase_time_testing(greedy_knapsack, 'Greedy', cases)
dp_showcase_time_testing(recursive_knapsack, 'Recursive', cases)
dp_showcase_time_testing(dp_knapsack, 'Dynamic Programming', cases)

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
