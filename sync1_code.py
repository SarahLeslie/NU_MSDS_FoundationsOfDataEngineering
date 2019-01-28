# Imports Key Packages
import numpy as np
import pandas as pd
from random import seed
from random import random
import time


# Defines the Search Functions
## Defines the Linear Search Test Function
def linear_search(list, item):
    # to count the loop interation number
    loop_counter = 0
    
    while loop_counter < len(list):
        if list[loop_counter] == item:
            loop_counter = loop_counter + 1
            # guess doesn't matter, loop counter demonstrates scaling along with search time
            return loop_counter

        else:
            loop_counter = loop_counter + 1
    
    # If no more available guesses, item is not in the list
    return None

## Defines the Binary Search Test Function
def binary_search(list, item):
  # to count the loop interation number
  loop_counter = 0

  # lower & upper _limit keep track of which part of the list contain the remaining viable guesses.
  lower_limit = 0
  upper_limit = len(list) - 1

  # While there are still available guesses ...
  while lower_limit <= upper_limit:
    # advances the loop counter by 1
    loop_counter = loop_counter + 1
    
    # identify the current middle element
    mid_point = (lower_limit + upper_limit) // 2
    guess = list[mid_point]
    
    # If guess is correct
    if guess == item:
      # guess doesn't matter, loop counter demonstrates scaling along with search time
      return loop_counter

    # If guess is too high
    if guess > item:
      upper_limit = mid_point - 1

    # If guess is too low
    else:
      lower_limit = mid_point + 1  
    
  # If no more available guesses, item is not in the list
  return None


# Generates Test Data
## Initializes literals to generate five arrays of length 512, 1024, 2048, 4096, and 8192, 
## of randomly generated uniformly distributed integers from 1 to 10000
MIN_GENERATED_VAL = -100000
MAX_GENERATED_VAL = 100000
VERY_SMALL_SIZE = 512
SMALL_SIZE = 1024
MEDIUM_SIZE = 2048
BIG_SIZE = 4096
VERY_BIG_SIZE = 8192
EVEN_BIGGER_SIZE = 8192*2

## Uses a common random number seed
np.random.seed(2)
very_small_list = np.random.randint(MIN_GENERATED_VAL,MAX_GENERATED_VAL,VERY_SMALL_SIZE)
np.random.seed(2)
small_list = np.random.randint(MIN_GENERATED_VAL,MAX_GENERATED_VAL,SMALL_SIZE)
np.random.seed(2)
medium_list = np.random.randint(MIN_GENERATED_VAL,MAX_GENERATED_VAL,MEDIUM_SIZE)
np.random.seed(2)
big_list = np.random.randint(MIN_GENERATED_VAL,MAX_GENERATED_VAL,BIG_SIZE)
np.random.seed(2)
very_big_list = np.random.randint(MIN_GENERATED_VAL,MAX_GENERATED_VAL,VERY_BIG_SIZE)
np.random.seed(2)
even_bigger_list = np.random.randint(MIN_GENERATED_VAL,MAX_GENERATED_VAL,EVEN_BIGGER_SIZE)

## Construct list of lists to test
list_of_test_lists = [very_small_list, small_list, medium_list, big_list, very_big_list, even_bigger_list]


# Testing
## Construct data structures for data capture
list_lengths = []
sort_times = []
linear_search_iteration_counts = []
binary_search_iteration_counts = []
linear_search_times = []
binary_search_times = []

## Records list lenghts
for test_list in list_of_test_lists:
  list_lengths.append((len(test_list)))

## Runs multiple sorts and records average of 10 trials per list
### Initializes individual trial sort times llist
trial_sort_times = []

### Records trial sort times
sort_start_trial1 = time.time_ns()
sorted_list = np.sort(very_small_list)
trial_sort_times.append((time.time_ns() - sort_start_trial1)/1000000) # to get milliseconds from nanoseconds


# Defines Results Capture Function
def search_test_results_capture(list_to_test):
  # to capture sort time
  sort_start_time = timeit.default_timer()
  sorted_list = np.sort(list_to_test)
  sort_time = (timeit.default_timer() - sort_start_time)/1000000 # to get milliseconds from nanoseconds

  # to capture linear interation count & search time
  linear_search_start_time = timeit.default_timer()
  linear_search_iteration_count = linear_search(sorted_list, sorted_list[-1])
  linear_search_time = (timeit.default_timer() - linear_search_start_time)/1000000 # to get milliseconds from nanoseconds

  # to capture binary interation count & search time
  binary_search_start_time = timeit.default_timer()
  binary_search_iteration_count = binary_search(sorted_list, sorted_list[-1])
  binary_search_time = (timeit.default_timer() - binary_search_start_time)/1000000 # to get milliseconds from nanoseconds

  # to capture sort + linear search time, and separately, sort + binary search time
  sort_plus_linear_time = sort_time + linear_search_time
  sort_plus_binary_time = sort_time + binary_search_time

  #returns all pertinant results
  return [len(list_to_test)
          , sort_time
          , linear_search_iteration_count
          , binary_search_iteration_count
          , linear_search_time
          , binary_search_time
          , sort_plus_linear_time
          , sort_plus_binary_time]


# Testing v2
results_v2 = pd.concat([pd.DataFrame([search_test_results_capture(test_list)]
                                    , columns=['list_size'
                                              , 'sort_time'
                                              , 'linear_search_iteration_count'
                                              , 'binary_search_iteration_count'
                                              , 'linear_search_time'
                                              , 'binary_search_time'
                                              , 'sort_plus_linear_search_time'
                                              , 'sort_plus_binary_search_time']) for test_list in list_of_test_lists]
                      , ignore_index=True)

results_v2

search_test_results_capture(very_small_list)

for i in test_list_of_test_lists:
  # to capture sort time
  sort_start_time = time.time_ns()
  sorted_list = np.sort(i)
  sort_time = (time.time_ns() - sort_start_time)/1000000 # to get milliseconds from nanoseconds

  # to capture linear interation count & search time
  linear_search_start_time = time.time_ns()
  linear_search_iteration_count = linear_search(sorted_list, sorted_list[-1])
  linear_search_time = (time.time_ns() - linear_search_start_time)/1000000 # to get milliseconds from nanoseconds

  # to capture binary interation count & search time
  binary_search_start_time = time.time_ns()
  binary_search_iteration_count = binary_search(sorted_list, sorted_list[-1])
  binary_search_time = (time.time_ns() - binary_search_start_time)/1000000 # to get milliseconds from nanoseconds

  # to capture sort + linear search time, and separately, sort + binary search time
  sort_plus_linear_time = sort_time + linear_search_time
  sort_plus_binary_time = sort_time + binary_search_time

  #returns all pertinant results
  print([len(i)
  , sort_time
  , linear_search_iteration_count
  , binary_search_iteration_count
  , linear_search_time
  , binary_search_time
  , sort_plus_linear_time
  , sort_plus_binary_time])

import timeit

def search_test_results_capture2(list_to_test):
  # to capture sort time
  sort_start_time = timeit.default_timer()
  sorted_list = np.sort(list_to_test)
  sort_time = (timeit.default_timer() - sort_start_time)*1000 # to get milliseconds from nanoseconds

  # to capture linear interation count & search time
  linear_search_start_time = timeit.default_timer()
  linear_search_iteration_count = linear_search(sorted_list, sorted_list[-1])
  linear_search_time = (timeit.default_timer() - linear_search_start_time)*1000 # to get milliseconds from nanoseconds

  # to capture binary interation count & search time
  binary_search_start_time = timeit.default_timer()
  binary_search_iteration_count = binary_search(sorted_list, sorted_list[-1])
  binary_search_time = (timeit.default_timer() - binary_search_start_time)*1000 # to get milliseconds from nanoseconds

  # to capture sort + linear search time, and separately, sort + binary search time
  sort_plus_linear_time = sort_time + linear_search_time
  sort_plus_binary_time = sort_time + binary_search_time

  #returns all pertinant results
  return [len(list_to_test)
          , sort_time
          , linear_search_iteration_count
          , binary_search_iteration_count
          , linear_search_time
          , binary_search_time
          , sort_plus_linear_time
          , sort_plus_binary_time]

# to capture sort time
sort_start_time = timeit.default_timer()
sorted_list = np.sort(big_list)
sort_time = (timeit.default_timer() - sort_start_time)*1000 # to get milliseconds from nanoseconds

# to capture linear interation count & search time
linear_search_start_time = timeit.default_timer()
linear_search_iteration_count = linear_search(sorted_list, sorted_list[-1])
linear_search_time = (timeit.default_timer() - linear_search_start_time)*1000 # to get milliseconds from nanoseconds

# to capture binary interation count & search time
binary_search_start_time = timeit.default_timer()
binary_search_iteration_count = binary_search(sorted_list, sorted_list[-1])
binary_search_time = (timeit.default_timer() - binary_search_start_time)*1000 # to get milliseconds from nanoseconds

# to capture sort + linear search time, and separately, sort + binary search time
sort_plus_linear_time = sort_time + linear_search_time
sort_plus_binary_time = sort_time + binary_search_time

#returns all pertinant results
print([len(big_list)
, sort_time
, linear_search_iteration_count
, binary_search_iteration_count
, linear_search_time
, binary_search_time
, sort_plus_linear_time
, sort_plus_binary_time])

search_test_results_capture2(big_list)
