# IMPORTS REQUIRED PACKAGES
import random
import string
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# DEFINES VARIOUS SORT FUNCTIONS
# Defines quicksort function
def quickSort(list_of_dicts, key):  
  # base case, arrays with 0 or 1 element are already "sorted"
  if len(list_of_dicts) < 2:
    return list_of_dicts
  else:
    # assigns pivot element
    pivot_element = list_of_dicts[0]
    # creates sub-array of all the elements less than the identified pivot
    less = [i for i in list_of_dicts[1:] if i[key] <= pivot_element[key]]
    # creates sub-array of all the elements greater than the identified pivot
    greater = [i for i in list_of_dicts[1:] if i[key] > pivot_element[key]]
    # recursive call of quicksort on the less-than and greater-than arrays (nesting the pivot in between)
    return quickSort(less,key) + [pivot_element] + quickSort(greater,key)

# Uses version of selection sort function from Week 2
def selectionSort(list_of_dicts, key):
  for i in range(len(list_of_dicts)): 
    min_index = i 
    min_value = list_of_dicts[i][key]
    # cycles through remaining array to find next min value
    for j in range(i+1, len(list_of_dicts)): 
        if list_of_dicts[j][key] < min_value: 
            min_index = j 
            min_value = list_of_dicts[j][key]
    # Swap the first element and the minimum element within the remaining unsorted portion of the array
    list_of_dicts[i], list_of_dicts[min_index] = list_of_dicts[min_index], list_of_dicts[i] 
  return list_of_dicts

# Defines Bubble sort function (from geeksforgeeks.org)
def bubbleSort(list_of_dicts,key): 
  n = len(list_of_dicts) 
  # Traverse through all array elements 
  for i in range(n): 
      # Last i elements are already in place 
      for j in range(0, n-i-1): 
          # traverse the array from 0 to n-i-1 
          # Swap if the element found is greater 
          # than the next element 
          if list_of_dicts[j][key] > list_of_dicts[j+1][key] : 
              list_of_dicts[j], list_of_dicts[j+1] = list_of_dicts[j+1], list_of_dicts[j] 
  return list_of_dicts

# Defines Insertion sort function (from geeksforgeeks.org)
def insertionSort(list_of_dicts, key): 
  # Traverse through 1 to len(arr) 
  for i in range(1, len(list_of_dicts)): 
      comp_element = list_of_dicts[i]
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position 
      j = i-1
      while j >=0 and comp_element[key] < list_of_dicts[j][key] : 
              list_of_dicts[j+1] = list_of_dicts[j] 
              j -= 1
      list_of_dicts[j+1] = comp_element 
  return list_of_dicts

# Defines Strand sort function (drafted myself from online pseudo-code)
# Defines merge of pre-sorted lists first
def my_merge(l1, l2, key):
  result = []
  while (l1 and l2):
    if (l1[0][key] <= l2[0][key]):
        result.append(l1.pop(0))
    else:
        result.append(l2.pop(0))
  # Add the remaining of the lists
  result.extend(l1 if l1 else l2)
  return result

def strandSort(list_of_dicts,key):
  if len(list_of_dicts) < 2:
    return list_of_dicts 
  result_list_of_dicts = []
  while len(list_of_dicts)>0:
    i = 0
    sublist = [list_of_dicts.pop(0)]
    while i < len(list_of_dicts):
      if list_of_dicts[i][key] > sublist[-1][key]:
        sublist.append(list_of_dicts.pop(i))
      else:
        i = i + 1
    result_list_of_dicts = my_merge(sublist,result_list_of_dicts,key)
  return result_list_of_dicts

# Defines Gnome sort function (from geeksforgeeks.org with slight tweaks)
def gnomeSort(list_of_dicts,key): 
  index = 1
  while index < len(list_of_dicts): 
    if index == 0: 
        index = index + 1
    if list_of_dicts[index][key] >= list_of_dicts[index - 1][key]: 
        index = index + 1
    else: 
        list_of_dicts[index], list_of_dicts[index-1] = list_of_dicts[index-1], list_of_dicts[index] 
        index = index - 1
  return list_of_dicts 

# Functional testing of quicksort, bubblesort, gnomesort, insertionsort, selectionsort, and strandsort functions
test_list_of_dicts = [{'first_name':'Sarah', 'last_name':'Martin', 'city':'NYC'}
                       , {'first_name':'Rachel', 'last_name':'Martin', 'city':'Berlin'}
                       , {'first_name':'David', 'last_name':'Martin', 'city':'Stamford'}]
quickSort(test_list_of_dicts,'city')

test_list_of_dicts = [{'first_name':'Sarah', 'last_name':'Martin', 'city':'NYC'}
                       , {'first_name':'Rachel', 'last_name':'Martin', 'city':'Berlin'}
                       , {'first_name':'David', 'last_name':'Martin', 'city':'Stamford'}]
bubbleSort(test_list_of_dicts,'city')

test_list_of_dicts = [{'first_name':'Sarah', 'last_name':'Martin', 'city':'NYC'}
                       , {'first_name':'Rachel', 'last_name':'Martin', 'city':'Berlin'}
                       , {'first_name':'David', 'last_name':'Martin', 'city':'Stamford'}]
gnomeSort(test_list_of_dicts,'city')

test_list_of_dicts = [{'first_name':'Sarah', 'last_name':'Martin', 'city':'NYC'}
                       , {'first_name':'Rachel', 'last_name':'Martin', 'city':'Berlin'}
                       , {'first_name':'David', 'last_name':'Martin', 'city':'Stamford'}]
insertionSort(test_list_of_dicts,'city')

test_list_of_dicts = [{'first_name':'Sarah', 'last_name':'Martin', 'city':'NYC'}
                       , {'first_name':'Rachel', 'last_name':'Martin', 'city':'Berlin'}
                       , {'first_name':'David', 'last_name':'Martin', 'city':'Stamford'}]
selectionSort(test_list_of_dicts,'city')

test_list_of_dicts = [{'first_name':'Sarah', 'last_name':'Martin', 'city':'NYC'}
                       , {'first_name':'Rachel', 'last_name':'Martin', 'city':'Berlin'}
                       , {'first_name':'David', 'last_name':'Martin', 'city':'Stamford'}]
strandSort(test_list_of_dicts,'city')


# GENERATES TEST DATA
# Instantiates (currently sorted) list of state abbrebiations
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Randomly shuffles states list
random.seed(2)
random.shuffle(states)

# Generates 50 randomly generated 10-character string as 'first names' and separately, 'last names'
random.seed(3)
first_names = ["".join(random.choices(string.ascii_lowercase, k=10)) for _ in range(50)]
random.seed(4)
last_names = ["".join(random.choices(string.ascii_lowercase, k=10)) for _ in range(50)]

# Checks to see there are no dupes with the names
len(first_names) == len(set(first_names))
len(last_names) == len(set(last_names))
# confirmed!

# Combines lists into dictionary and then converts to list of dictionaries
persons_dict = {'first_name':first_names, 'last_name':last_names, 'address':states}
persons_list = pd.DataFrame(persons_dict).to_dict('records')


# TESTS 1. QUICK SORT, 2. BUBBLE SORT, 3. GNOME SORT, 4. INSERTION SORT, 5. SELECTION SORT, AND 6. STRAND SORT
# due to in-place sorting or elimination of the original data,
# I'll create copies of the test data for each sort function for 2 sorts
persons_list_quick1 = persons_list
persons_list_bubble1 = persons_list
persons_list_gnome1 = persons_list
persons_list_insertion1 = persons_list
persons_list_selection1 = persons_list
persons_list_strand1 = persons_list

persons_list_quick2 = persons_list
persons_list_bubble2 = persons_list
persons_list_gnome2 = persons_list
persons_list_insertion2 = persons_list
persons_list_selection2 = persons_list
persons_list_strand2 = persons_list

# instantiates list to capture time test results
time_results = []

def time_testing(sort_method,method_label,data1,data2):
  start1 = time.perf_counter()
  sort_method(data1,'last_name')
  end1 = time.perf_counter()
  start2 = time.perf_counter()
  sort_method(data2,'address')
  end2 = time.perf_counter()
  first_sort_time = (end1 - start1)*1000
  second_sort_time = (end2 - start2)*1000
  time_results.append({'Method':method_label
                      ,'One Sort Time':(first_sort_time+second_sort_time)/2
                      ,'Two Sort Time':first_sort_time+second_sort_time})

time_testing(quickSort,'Quick Sort',persons_list_quick1,persons_list_quick2)
time_testing(bubbleSort,'Bubble Sort',persons_list_bubble1,persons_list_bubble2)
time_testing(gnomeSort,'Gnome Sort',persons_list_gnome1,persons_list_gnome2)
time_testing(insertionSort,'Insertion Sort',persons_list_insertion1,persons_list_insertion2)
time_testing(selectionSort,'Selection Sort',persons_list_selection1,persons_list_selection2)
time_testing(strandSort,'Strand Sort',persons_list_strand1,persons_list_strand2)

results_df = pd.DataFrame(time_results)
