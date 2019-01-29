# Loads required packages
import sys
import random 
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# Chose integers from 100-950 instead of 100-500 to (TRY to) show greater time differences
random.seed(5)
test_data = [random.randint(100, 2900) for _ in range(10)]
# sorted the data to make it easier to spot check the eventual time test results
test_data.sort()
test_data

# Determines Python recursion limit on this machine
sys.getrecursionlimit()
## sys.setrecursionlimit(5000) DANGEROUS!!

# Creates time test function applicable with various different time capture functions
def test_loop(fact_function,time_function):
    fact_results = []
    time_results = []
    for test_int in test_data:
        start = time_function()
        fact = fact_function(test_int)
        end = time_function()
        fact_results.append(fact)
        time_results.append((end - start)*1000)
    return fact_results, time_results


# VERSION 1: Uses regular time.time() function
recur_fact_results_vtime, recur_time_results_vtime = test_loop(fact_rec, time.time)
iter_fact_results_vtime, iter_time_results_vtime = test_loop(fact_iter, time.time)

# Examines Version 1 results
recur_fact_results_vtime == iter_fact_results_vtime
recur_time_results_vtime
iter_time_results_vtime


# VERSION 2: Uses time.thread_time() function
recur_fact_results_vthread, recur_time_results_vthread = test_loop(fact_rec, time.thread_time)
iter_fact_results_vthread, iter_time_results_vthread = test_loop(fact_iter, time.thread_time)

# Examines Version 2 results
recur_fact_results_vthread == iter_fact_results_vthread
recur_time_results_vthread
iter_time_results_vthread


# VERSION 3: Uses time.monotonic() function
recur_fact_results_vmonotonic, recur_time_results_vmonotonic = test_loop(fact_rec, time.monotonic)
iter_fact_results_vmonotonic, iter_time_results_vmonotonic = test_loop(fact_iter, time.monotonic)

# Examines Version 3 results
recur_fact_results_vmonotonic == iter_fact_results_vmonotonic
recur_time_results_vmonotonic
iter_time_results_vmonotonic


# VERSION 4: Uses time.process_time() function
recur_fact_results_vprocess, recur_time_results_vprocess = test_loop(fact_rec, time.process_time)
iter_fact_results_vprocess, iter_time_results_vprocess = test_loop(fact_iter, time.process_time)

# Examines Version 4 results
recur_fact_results_vprocess == iter_fact_results_vprocess
recur_time_results_vprocess
iter_time_results_vprocess


# VERSION 5: Uses time.perf_counter() function
recur_fact_results_vperfCounter, recur_time_results_vperfCounter = test_loop(fact_rec, time.perf_counter)
iter_fact_results_vperfCounter, iter_time_results_vperfCounter = test_loop(fact_iter, time.perf_counter)

# Examines Version 5 results
recur_fact_results_vperfCounter == iter_fact_results_vperfCounter
recur_time_results_vperfCounter
iter_time_results_vperfCounter


# Confirms all factorial results match
recur_fact_results_vtime == recur_fact_results_vthread == recur_fact_results_vmonotonic == recur_fact_results_vprocess == recur_fact_results_vperfCounter

# Organizes all results into a single dataframe
results_dict = {'Input_Number':test_data
                ,'Factorial_Results':iter_fact_results_vtime
                ,'ForLoop_TimeFunction_Time':iter_time_results_vtime
                ,'Recursion_TimeFunction_Time':recur_time_results_vtime
                ,'ForLoop_ThreadFunction_Time':iter_time_results_vthread
                ,'Recursion_ThreadFunction_Time':recur_time_results_vthread
                ,'ForLoop_MonotonicFunction_Time':iter_time_results_vmonotonic
                ,'Recursion_MonotonicFunction_Time':recur_time_results_vmonotonic
                ,'ForLoop_ProcessFunction_Time':iter_time_results_vprocess
                ,'Recursion_ProcessFunction_Time':recur_time_results_vprocess
                ,'ForLoop_PerfCounterFunction_Time':iter_time_results_vperfCounter
                ,'Recursion_PerfCounterFunction_Time':recur_time_results_vperfCounter}
results = pd.DataFrame(results_dict)

# Adds an average of the time results across all time function options for each factorial method (curiosity)
results['ForLoop_AVERAGE_Time'] = results[['ForLoop_TimeFunction_Time'
                                            ,'ForLoop_ThreadFunction_Time'
                                            ,'ForLoop_MonotonicFunction_Time'
                                            ,'ForLoop_ProcessFunction_Time'
                                            ,'ForLoop_PerfCounterFunction_Time'
                                            ]].mean(axis=1)

results['Recursion_AVERAGE_Time'] = results[['Recursion_TimeFunction_Time'
                                            ,'Recursion_ThreadFunction_Time'
                                            ,'Recursion_MonotonicFunction_Time'
                                            ,'Recursion_ProcessFunction_Time'
                                            ,'Recursion_PerfCounterFunction_Time'
                                            ]].mean(axis=1)

# Basic summary of the results
results.info()
results.describe()

# Graphs the (various) results
def my_custom_plot(ycol1,ycol2,time_func):
    sns.set()
    ax1 = sns.scatterplot(x="Input_Number", y=ycol1
                            ,data=results
                            ,color='b', marker='o', s=50
                            ,label = ' '.join(['for-loop', time_func, 'results']))
    sns.scatterplot(x="Input_Number", y=ycol2
                    ,data=results, ax=ax1
                    ,color='r', marker='x', s=55
                    ,label = ' '.join(['recursion', time_func, 'results']))
    ax1.set_xlabel('Input_Number')
    ax1.set_ylabel('Time in ms')
    ax1.set_title('Run Times for Factorial Calculation Functions')
    #ax1.legend(loc='upper left',fontsize='x-small')
    ax1.legend(bbox_to_anchor=(.45, .85) ,fontsize='x-small')
    plt.show()

my_custom_plot("ForLoop_TimeFunction_Time","Recursion_TimeFunction_Time",'.time()')
my_custom_plot("ForLoop_ThreadFunction_Time","Recursion_ThreadFunction_Time",'.thread_time()')
my_custom_plot("ForLoop_MonotonicFunction_Time","Recursion_MonotonicFunction_Time",'.monotonic()')
my_custom_plot("ForLoop_ProcessFunction_Time","Recursion_ProcessFunction_Time",'.process_time()')
my_custom_plot("ForLoop_PerfCounterFunction_Time","Recursion_PerfCounterFunction_Time",'.perf_counter()')
my_custom_plot("ForLoop_AVERAGE_Time","Recursion_AVERAGE_Time",'Averaged')


# Extra Credit:
# modifies the recursive factorial function to allow numbers greater python's existing recursion limit

def fact_semi_rec(u,l=1):
    if u==l:
        return u
    else:
        m = (u + l)//2
        first_half = fact_semi_rec(u,m+1)
        second_half = fact_semi_rec(m,l)
        return first_half * second_half

fact_semi_rec(sys.getrecursionlimit()**2)