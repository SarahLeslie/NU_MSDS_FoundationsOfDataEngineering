#import inspect
import sys
import random 
import numpy as np
import time

def fact_rec(x):
  if x == 1:
    return 1
  else:
    return (x * fact_rec(x-1))

def fact_iter(x):
    ans = 1
    for i in range(1,x+1): 
        ans = ans * i 
    return ans

fact_rec(5)
fact_iter(5)

# Generates test data
# Chose integers from 100-900 instead of 100-500 to show greater time differences
np.random.seed(3)
test_data = np.sort(np.random.randint(10, 100, 10, dtype='int64'))
test_data

sys.getrecursionlimit()
## sys.setrecursionlimit(5000) DANGEROUS!!

for i in range(10):
    test_int = test_data[i]
    
    print("\nFactorial of", test_int)

    time.sleep(1.5)

    recu_start = time.time_ns()
    fact_rec(test_int)
    #result_rec = fact_rec(test_int)
    recu_end = time.time_ns()
    print("Recursive Method Time: ", ((recu_end - recu_start)/1000000), " ms")

    time.sleep(1.5)

    iter_start = time.time_ns()
    fact_iter(test_int)
    #result_iter = fact_iter(test_int)
    iter_end = time.time_ns()
    print("For-Loop Method Time: ", ((iter_end - iter_start)/1000000), " ms")

#print (result_rec == result_iter)

fact_rec(24)
test_int = 24
fact_rec(test_int)

for i in range(10,50):    
    print("\nFactorial of", i)

    time.sleep(1.5)

    recu_start = time.time_ns()
    fact_rec(i)
    recu_end = time.time_ns()
    print("Recursive Factorial: ", ((recu_end - recu_start)/1000000), " ms")

    time.sleep(1.5)

    iter_start = time.time_ns()
    fact_iter(i)
    iter_end = time.time_ns()
    print("For-Loop Factorial: ", ((iter_end - iter_start)/1000000), " ms")



# In this Extra Credit Assignment, 
# please modify the recursive factorial function 
# to allow numbers greater than this limit set by python 
# without modifying the system recursion limit in python.  
# By this I mean you should not change sys.setrecursionlimit() .  
