# IMPORTS REQUIRED PACKAGES
import random
import string
import time
# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# GENERATES TEST DATA
# Instantiates (unsorted) list of 100,000 10-character strings
random.seed(6)
unsorted_list = ["".join(random.choices(string.ascii_lowercase, k=10)) for _ in range(100000)]

# Instantiates a set of the same strings
unsorted_set = set(unsorted_list)
# Checks to see there are no dupes within the list/set
len(unsorted_list) == len(unsorted_set)
# confirmed!

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
# Use linear search for the unsorted list, 
# binary search for the sorted list, 
# and use the set.remove() builtin for the set.  
# Capture the time it takes using all three algorithms.

# # TESTS 1. QUICK SORT, 2. BUBBLE SORT, 3. GNOME SORT, 4. INSERTION SORT, 5. SELECTION SORT, AND 6. STRAND SORT
# due to in-place sorting or elimination of the original data,
# I'll create copies of the test data for each sort function for 2 sorts
persons_list_quick1 = persons_list.copy()
persons_list_bubble1 = persons_list.copy()
persons_list_gnome1 = persons_list.copy()
persons_list_insertion1 = persons_list.copy()
persons_list_selection1 = persons_list.copy()
persons_list_strand1 = persons_list.copy()

persons_list_quick2 = persons_list.copy()
persons_list_bubble2 = persons_list.copy()
persons_list_gnome2 = persons_list.copy()
persons_list_insertion2 = persons_list.copy()
persons_list_selection2 = persons_list.copy()
persons_list_strand2 = persons_list.copy()

# instantiates list to capture time test results
time_results = []

def time_testing(sort_method,method_label,data1,data2):
  start1 = time.perf_counter()
  by_last_name = sort_method(data1,'last_name')
  end1 = time.perf_counter()
  start2 = time.perf_counter()
  by_address = sort_method(data2,'address')
  end2 = time.perf_counter()
  first_sort_time = (end1 - start1)*1000
  second_sort_time = (end2 - start2)*1000
  time_results.append({'Method':method_label
                      ,'Sort Key':'Last Name'
                      ,'Sort Time':first_sort_time})
  time_results.append({'Method':method_label
                      ,'Sort Key':'Address'
                      ,'Sort Time':second_sort_time})
  time_results.append({'Method':method_label
                      ,'Sort Key':'Average'
                      ,'Sort Time':(first_sort_time + second_sort_time)/2})
  return by_last_name, by_address

time_testing(quickSort,'Quick Sort',persons_list_quick1,persons_list_quick2)
time_testing(bubbleSort,'Bubble Sort',persons_list_bubble1,persons_list_bubble2)
time_testing(gnomeSort,'Gnome Sort',persons_list_gnome1,persons_list_gnome2)
time_testing(insertionSort,'Insertion Sort',persons_list_insertion1,persons_list_insertion2)
time_testing(selectionSort,'Selection Sort',persons_list_selection1,persons_list_selection2)
time_testing(strandSort,'Strand Sort',persons_list_strand1,persons_list_strand2)

results_df = pd.DataFrame(time_results)

sns.catplot(x="Sort Key", y="Sort Time"
            , hue = "Method", data=results_df)
plt.show()

sns.catplot(x="Sort Key", y="Sort Time"
            , hue = "Method", jitter = False
            , data=results_df.loc[~results_df['Method'].isin(['Gnome Sort','Bubble Sort'])])
plt.show()
