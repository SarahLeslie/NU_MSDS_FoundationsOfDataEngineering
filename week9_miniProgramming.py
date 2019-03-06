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
for i in range(10):
    test_case_sizes.append(100*i + 10)

weights = {}
values = {}
bag_weight_capacities = []
for size in test_case_sizes:
    random.seed(size)
    weights['test_case_size_' + str(size)] = [round(random.uniform(0.00, 30.00),2) for i in range(size)]
    values['test_case_size_' + str(size)] = [round(random.uniform(0.00, 300.00),2) for i in range(size)]
    bag_weight_capacities.append(random.randint(5,5*size))

cases = {}
for test_case in range(len(test_case_sizes)):
    cases['case_' + str(test_case + 1)] = {}
    cases['case_' + str(test_case + 1)]['size'] = test_case_sizes[test_case]
    cases['case_' + str(test_case + 1)]['bag_weight_capacity'] = bag_weight_capacities[test_case]
    cases['case_' + str(test_case + 1)]['items'] = []
    for item_num in range(test_case_sizes[test_case]):
        cases['case_' + str(test_case + 1)]['items'].append({})
        cases['case_' + str(test_case + 1)]['items'][item_num]['weight'] = weights['test_case_size_' + str(test_case_sizes[test_case])][item_num]
        cases['case_' + str(test_case + 1)]['items'][item_num]['value'] = values['test_case_size_' + str(test_case_sizes[test_case])][item_num]
        
# checking test data
cases.keys()
cases['case_2'].keys()
cases['case_2']['size']
type(cases['case_2']['items'])
len(cases['case_2']['items'])
cases['case_2']['items'][3]
cases['case_2']['bag_weight_capacity']
sum(cases['case_2']['items'][x]['weight'] for x in range(len(cases['case_2']['items'])))
# all set!


# DEFINES KNAPSACK SOLUTION FUNCTIONS
# greedy method
def greedy_knapsack(case):
    bag = []
    weight_available = case['bag_weight_capacity']
    while weight_available > 0:
        new_subset = [x for x in case['items'] if x['weight'] <= weight_available]
        if not new_subset:
            return bag
        current_max_value = max([x['value'] for x in new_subset])
        items_with_max_value = [x for x in new_subset if x['value'] == current_max_value]
        min_weight_among_max_value_items = min([x['weight'] for x in items_with_max_value])
        item_to_pop_index = [x for x in range(len(case['items'])) if (case['items'][x]['value'] == current_max_value \
            and case['items'][x]['weight'] == min_weight_among_max_value_items)][0]
        weight_available = weight_available - case['items'][item_to_pop_index]['weight']
        bag.append(case['items'].pop(item_to_pop_index))
    return bag

# testing greedy method
single_test_case = copy.deepcopy(cases['case_1'])
result_bag = greedy_knapsack(single_test_case)
single_test_case['bag_weight_capacity']
sum(x['weight'] for x in result_bag)
sum(x['value'] for x in result_bag)


# recursive method
def recursive_knapsack(items, weight_capacity):
    
    return True

int knapsack(int w[], int p[], int n, int M)
{
    //In every pass, we can either include nth item or not
    //if the capacity of knapsack is left to NIL, no value can be attained
    if(M==0)
        return 0;
    //if no more items are left, no value can be attained
    if(n==0)
        return 0;
    //if current item, weighs more than the capacity of knapsack, it can not be included
    if(w[n-1]>M)
        return knapsack(w,p,n-1,M);
    //else select the maximum value of once including the current item and once not including it
    return max(knapsack(w,p,n-1,M),p[n-1]+knapsack(w,p,n-1,M-w[n-1]));
}
int main()
{
    int i,n;
    int M;  //capacity of knapsack
    cout<<"Enter the no. of items ";
    cin>>n;
    int w[n];  //weight of items
    int p[n];  //value of items
    cout<<"Enter the weight and price of all items"<<endl;
    for(i=0;i<n;i++)
    {
        cin>>w[i]>>p[i];
    }
    cout<<"enter the capacity of knapsack  ";
    cin>>M;
    cout<<"The maximum value of items that can be put into knapsack is "<<knapsack(w,p,n,M);
    return 0;
}

# testing recursive method
single_test_case = copy.deepcopy(cases['case_1'])
result_bag = recursive_knapsack(single_test_case)
single_test_case['bag_weight_capacity']
sum(x['weight'] for x in result_bag)
sum(x['value'] for x in result_bag)


# dynamic programming method
def dp_knapsack(items, weight_capacity):
    return True

# testing dynamic programming
single_test_case = copy.deepcopy(cases['case_1'])
result_bag = dp_knapsack(single_test_case)
single_test_case['bag_weight_capacity']
sum(x['weight'] for x in result_bag)
sum(x['value'] for x in result_bag)


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
