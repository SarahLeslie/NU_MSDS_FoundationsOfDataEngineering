# Loads required packages
import sys
import random 
import time

# Defines the two main factorial functions
def fact_rec(x):
  if x == 1:
    return 1
  else:
    return x * fact_rec(x-1)

def fact_iter(x):
    ans = 1
    for i in range(1,x+1): 
        ans = ans * i 
    return ans

# Tests said functions
fact_rec(5)
fact_iter(5)

# Generates test data
# Chose integers from 100-900 instead of 100-500 to show greater time differences
random.seed(5)
test_data = [random.randint(100, 950) for _ in range(10)]
test_data.sort()
test_data

# Determines Python recursion limit on this machine
sys.getrecursionlimit()
## sys.setrecursionlimit(5000) DANGEROUS!!

# VERSION 1: time tests each function once for each test_int value
#Initializes Results Data Capture Lists
fact_results_v1 = []
recur_time_results_v1 = []
iter_time_results_v1 = []

# Captures factorial results & function run times
for test_int in test_data:
    #print("Factorial of", test_int)
    fact_results_v1.append(fact_iter(test_int))

    time.sleep(1)
    rec_start = time.time()
    fact_rec(test_int)
    rec_end = time.time()
    #print("Recursive Method Time: ", ((end - start)/1000000), " ms")
    recur_time_results_v1.append((rec_end - rec_start)*1000)

    time.sleep(1)
    iter_start = time.time()
    fact_iter(test_int)
    iter_end = time.time()
    #print("For-Loop Method Time: ", ((end - start)/1000000), " ms\n")
    iter_time_results_v1.append((iter_end - iter_start)*1000)


# time results were too variable/weird from run to run, so decided to run 10 times and average
# VERSION 2: time tests each function 10 times for each test_int value and averages the times recorded
fact_results_v2 = []
recur_time_results_v2 = []
iter_time_results_v2 = []

# Captures factorial results & function run times
for test_int in test_data:
    #print("Factorial of", test_int)
    fact_results_v2.append(fact_iter(test_int))

    rec_temp_time_results = []
    for i in range(10):
        time.sleep(1)
        rec_start = time.time()
        fact_rec(test_int)
        rec_end = time.time()
        rec_temp_time_results.append((rec_end - rec_start)*1000)
    
    #print("Recursive Method Time: ", ((end - start)/1000000), " ms")
    recur_time_results_v2.append(sum(rec_temp_time_results)/len(rec_temp_time_results))

    iter_temp_time_results = []
    for i in range(10):
        time.sleep(1)
        iter_start = time.time()
        fact_iter(test_int)
        iter_end = time.time()
        iter_temp_time_results.append((iter_end - iter_start)*1000)
    
    #print("For-Loop Method Time: ", ((end - start)/1000000), " ms\n")
    iter_time_results_v2.append(sum(iter_temp_time_results)/len(iter_temp_time_results))

# VERSION 3: thanks ethan
def test_loop(f):
    fact_results = []
    time_results = []
    for test_int in test_data:
        start = time.perf_counter()
        fact = f(test_int)
        end = time.perf_counter()
        fact_results.append(fact)
        time_results.append(end - start)
    return fact_results, time_results

recur_fact_results_v3, recur_time_results_v3 = test_loop(fact_rec)
iter_fact_results_v3, iter_time_results_v3 = test_loop(fact_iter)

# Examines results
recur_fact_results_v3 == iter_fact_results_v3
fact_results_v1 == fact_results_v2

recur_time_results_v1
iter_time_results_v1

recur_time_results_v2
iter_time_results_v2

recur_time_results_v3
iter_time_results_v3

#print (result_rec == result_iter)

# In this Extra Credit Assignment, 
# please modify the recursive factorial function 
# to allow numbers greater than this limit set by python 
# without modifying the system recursion limit in python.  
# By this I mean you should not change sys.setrecursionlimit() .  
