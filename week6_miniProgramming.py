# IMPORTS REQUIRED PACKAGES
import random
import string
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

fake = Faker()


# GENERATES LIST OF 3K FAKE NAMES
num_names_needed = 5 + 5**2 + 5**3 + 5**4 + 5**5
fake.seed(7)
names = [fake.name() for _ in range(num_names_needed)]
# checking
names[0:10]
len(names)
len(set(names))
# there are dupes, which is ok but to be careful with assignment, we'll de-dupe this list
names = list(set(names))
len(names)

# SPLITS THE NAMES INTO UNIQUE LISTS FOR EACH LEVEL 
# determines the size of each list
lev_1_size = 5
lev_2_size = lev_1_size*5 - 2 # adding some dupes
lev_3_size = lev_2_size*5 - 4
lev_4_size = lev_3_size*5 - 16
lev_5_size = lev_4_size*5 - 64
# instantiating name lists for each level
first_lev = names[:lev_1_size]
second_lev = names[lev_1_size:lev_1_size+lev_2_size]
third_lev = names[lev_1_size+lev_2_size:lev_1_size+lev_2_size+lev_3_size]
fourth_lev = names[lev_1_size+lev_2_size+lev_3_size:lev_1_size+lev_2_size+lev_3_size+lev_4_size]
fifth_lev = names[lev_1_size+lev_2_size+lev_3_size+lev_4_size:lev_1_size+lev_2_size+lev_3_size+lev_4_size+lev_5_size]
# checking
lev_1_size == len(first_lev)
lev_2_size == len(second_lev)
lev_3_size == len(third_lev)
lev_4_size == len(fourth_lev)
lev_5_size == len(fifth_lev)
# adding duplicate names to each list to fill out max possible (won't need all) level requirements
second_lev = second_lev + second_lev[:2]
third_lev = third_lev + third_lev[:4]
fourth_lev = fourth_lev + fourth_lev[:16]
fifth_lev = fifth_lev + fifth_lev[:64]
# checkin final sizes
len(first_lev) == 5
len(second_lev) == 5*len(set(first_lev))
len(third_lev) == 5*len(set(second_lev))
len(fourth_lev) == 5*len(set(third_lev))
len(fifth_lev) == 5*len(set(fourth_lev))

# GENERATES TEST Graph
people_graph = {}
# creates 5 connections for each first level person 
# 1 dupe in second level 
# but dupes will never be connected to the same person in the previous level because lists are orderd
for i in range(len(first_lev)):
  people_graph[first_lev[i]] = second_lev[5*i:5*i+5]

# de-dupes level 2 so we don't assign their 5 level 3 connections twice
second_lev = list(dict.fromkeys(second_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(second_lev)):
  people_graph[second_lev[i]] = third_lev[5*i:5*i+5]

third_lev = list(dict.fromkeys(third_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(third_lev)):
  people_graph[third_lev[i]] = fourth_lev[5*i:5*i+5]

fourth_lev = list(dict.fromkeys(fourth_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(fourth_lev)):
  people_graph[fourth_lev[i]] = fifth_lev[5*i:5*i+5]

# not sure this is necessary but... 
# let's imagine the level 5 people all have 'facebook accounts with no friends' vs. 'not having accounts'
fifth_lev = list(dict.fromkeys(fifth_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(fifth_lev)):
  people_graph[fifth_lev[i]] = []

# checking
len(people_graph) == lev_1_size + lev_2_size + lev_3_size + lev_4_size + lev_5_size

# checking to see that each connection has 0 dupes
true_counter = 0 
for i in people_graph.keys():
  true_counter = true_counter + (len(people_graph[i]) == len(set(people_graph[i])))

true_counter == len(people_graph)
# all set!


# Defines Strand sort function (to sort the list)
# Defines merge of pre-sorted lists first
def my_merge(l1, l2):
  result = []
  while (l1 and l2):
    if (l1[0] <= l2[0]):
        result.append(l1.pop(0))
    else:
        result.append(l2.pop(0))
  # Add the remaining of the lists
  result.extend(l1 if l1 else l2)
  return result

def strandSort(a_list):
  if len(a_list) < 2:
    return a_list 
  result_list = []
  while len(a_list)>0:
    i = 0
    sublist = [a_list.pop(i)]
    while i < len(a_list):
      if a_list[i] > sublist[-1]:
        sublist.append(a_list.pop(i))
      else:
        i = i + 1
    result_list = my_merge(sublist,result_list)
  return result_list

# Instantiates a sorted version of the same list of strings
temp_unsorted_list = unsorted_list.copy
sorted_list = strandSort(temp_unsorted_list)

# Stores 10kth, 30kth, 50kth, 70kth, 90kth, and 100kth strings from each set of test data (unsorted list, set, sorted list)
search_test_names = {}
search_test_names['unsorted_list'] = [unsorted_list[9999], unsorted_list[29999], unsorted_list[49999]
                                    ,unsorted_list[69999], unsorted_list[89999], unsorted_list[99999]]
search_test_names['sorted_list'] = [sorted_list[9999], sorted_list[29999], sorted_list[49999]
                                    ,sorted_list[69999], sorted_list[89999], sorted_list[99999]]


## DEFINES THE LIST SEARCH FUNCTIONS
## Defines the Linear Search Test Function
def linear_search(list, item):
    # to indentify the index
    index = 0
    while index < len(list):
        if list[index] == item:
            return "Index of element is ",index
        else:
            index = index + 1
    # If no more available guesses, item is not in the list
    return None

## Defines the Binary Search Test Function
def binary_search(list, item):
  # lower & upper _limit keep track of which part of the list contain the remaining viable guesses.
  lower_limit = 0
  upper_limit = len(list) - 1

  # While there are still available guesses ...
  while lower_limit <= upper_limit:
    
    # identify the current middle element
    mid_point = (lower_limit + upper_limit) // 2
    guess = list[mid_point]
    
    # If guess is correct
    if guess == item:
      # guess doesn't matter, loop counter demonstrates scaling along with search time
      return mid_point

    # If guess is too high
    if guess > item:
      upper_limit = mid_point - 1

    # If guess is too low
    else:
      lower_limit = mid_point + 1  
    
  # If no more available guesses, item is not in the list
  return None


# Now search for these six names in each of the collections.  
# # TESTING
# instantiates list to capture time test results
time_results = []

# defines 2 functions to time test search method (1 for the lists, 1 for the set)
def list_time_testing(search_function,method_label,test_list,search_for_list):
    indeces = [9999, 29999, 49999, 69999, 89999, 99999]
    for i in range(len(search_for_list)):
        item = search_for_list[i]
        start = time.perf_counter()
        search_function(test_list,item)
        end = time.perf_counter()
        search_time = (end - start)*1000
        time_results.append({'Search Function':method_label
                              ,'Index':indeces[i]
                              ,'Search Time':search_time})

def set_time_testing(test_set,search_for_list):
  for i in range(len(search_for_list)):
      item = search_for_list[i]
      start = time.perf_counter()
      test_set.remove(item)
      end = time.perf_counter()
      search_time = (end - start)*1000
      time_results.append({'Search Function':"Set '.remove()'"
                          ,'Index':'NA'
                          ,'Search Time':search_time})

# conducts the time testing
list_time_testing(linear_search,'Linear Search for Unsorted List',unsorted_list,search_test_names['unsorted_list'])
list_time_testing(binary_search,'Binary Search for Sorted List',sorted_list,search_test_names['sorted_list'])
set_time_testing(unsorted_set,search_test_names['unsorted_list'])
set_time_testing(unsorted_set,search_test_names['sorted_list'])

# organizes results into pandas dataframe for easier exploration
results_df = pd.DataFrame(time_results)
results_df.loc[results_df['Index'] == 'NA', 'Search Time'].mean()

sns.catplot(x="Search Function", y="Search Time"
            , hue = "Index", data=results_df)
plt.show()

sns.catplot(x="Index", y="Search Time"
            , hue = "Search Function", data=results_df)
plt.show()

sns.catplot(x="Search Function", y="Search Time"
            , hue = "Index"
            , data=results_df.loc[results_df['Search Function']!='Linear Search for Unsorted List'])
plt.show()\
    