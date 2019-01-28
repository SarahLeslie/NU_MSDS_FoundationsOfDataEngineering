import random
import numpy as np
import pandas as pd
import time
import string
import matplotlib.pyplot as plt
import seaborn as sns

# Defines Search Functions
## Finds the smallest value in an array
def findSmallest(arr):
  # Initializes the index of the smallest value
  smallest_index = 0
  # Initializes the smallest value
  smallest = arr[0]
  
  # Determines the actual small index in the array
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

## Sorts array
def selectionSort(arr):
  # Initializes sorted array
  newArr = []
  
  # Cycles through all elements in the existing unsorted array
  for i in range(len(arr)):
  # while loop is much faster than for loop
  # sorting of test array below was <1 millisecond with while loop, 3 milliseconds with for loop
  #while len(arr) > 0:
      # Finds the smallest element in the existing unsorted array, adds it to the new sorted array, and removes it from the existing unsorted array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

## mini test sort
start_time = time.time_ns()
print(selectionSort([5, 3, 6, 2, 10]))
print((time.time_ns() - start_time)/1000000)


# Generates Real Test Data
sizes = [5000,10000,15000,20000,25000]
test_data = []
for size in sizes:
    np.random.seed(2)
    #not single array?  dict for each size?  
    int_array = list(np.random.randint(1,1000000,size))
    test_data.append(int_array)
    np.random.seed(2)
    dec_array = list(np.random.random(size))
    test_data.append(dec_array)
    np.random.seed(2)
    string5_array = list([''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(size)])
    test_data.append(string5_array)
    np.random.seed(2)
    string15_array = list([''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(size)])
    test_data.append(string15_array)


# Tests & captures results data
## Initializes Results Capture Data Structure
result_rows = []
result_columns = ['Data_Type','Array_Size','SelectionSort_Execution_Time']

## Captures results for arrays of size 5000
start_time = time.time_ns()
selectionSort(test_data[0])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['int',sizes[0],tot_time])

start_time = time.time_ns()
selectionSort(test_data[1])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['dec',sizes[0],tot_time])

start_time = time.time_ns()
selectionSort(test_data[2])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string5',sizes[0],tot_time])

start_time = time.time_ns()
selectionSort(test_data[3])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string15',sizes[0],tot_time])

## Captures results for arrays of size 10000
start_time = time.time_ns()
selectionSort(test_data[4])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['int',sizes[1],tot_time])

start_time = time.time_ns()
selectionSort(test_data[5])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['dec',sizes[1],tot_time])

start_time = time.time_ns()
selectionSort(test_data[6])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string5',sizes[1],tot_time])

start_time = time.time_ns()
selectionSort(test_data[7])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string15',sizes[1],tot_time])

## Captures results for arrays of size 15000
start_time = time.time_ns()
selectionSort(test_data[8])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['int',sizes[2],tot_time])

start_time = time.time_ns()
selectionSort(test_data[9])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['dec',sizes[2],tot_time])

start_time = time.time_ns()
selectionSort(test_data[10])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string5',sizes[2],tot_time])

start_time = time.time_ns()
selectionSort(test_data[11])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string15',sizes[2],tot_time])

## Captures results for arrays of size 20000
start_time = time.time_ns()
selectionSort(test_data[12])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['int',sizes[3],tot_time])

start_time = time.time_ns()
selectionSort(test_data[13])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['dec',sizes[3],tot_time])

start_time = time.time_ns()
selectionSort(test_data[14])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string5',sizes[3],tot_time])

start_time = time.time_ns()
selectionSort(test_data[15])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string15',sizes[3],tot_time])

## Captures results for arrays of size 25000
start_time = time.time_ns()
selectionSort(test_data[16])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['int',sizes[4],tot_time])

start_time = time.time_ns()
selectionSort(test_data[17])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['dec',sizes[4],tot_time])

start_time = time.time_ns()
selectionSort(test_data[18])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string5',sizes[4],tot_time])

start_time = time.time_ns()
selectionSort(test_data[19])
tot_time = (time.time_ns() - start_time)/1000000
result_rows.append(['string15',sizes[4],tot_time])

## Organizes results into pandas dataframe
results = pd.DataFrame(result_rows, columns=result_columns)
results[results['Data_Type'] == 'int']


# Graphs the results
sns.set()
sns.catplot(x="Array_Size", y="SelectionSort_Execution_Time", hue="Data_Type", kind="swarm", data=results)
plt.show()


import timeit
selectionSort(test_data[2])
timeit.timeit(selectionSort(test_data[1]))