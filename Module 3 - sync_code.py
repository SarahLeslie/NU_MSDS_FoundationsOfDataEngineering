#import inspect
import sys
import random 
import time

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

fact_rec(5)
fact_iter(5)

# Generates test data
# Chose integers from 100-900 instead of 100-500 to show greater time differences
random.seed(4)
test_data = [random.randint(100, 900) for _ in range(10)]
test_data.sort()
test_data

sys.getrecursionlimit()
## sys.setrecursionlimit(5000) DANGEROUS!!

for test_int in test_data:
    print("Factorial of", test_int)

    time.sleep(1)

    recu_start = time.time_ns()
    fact_rec(test_int)
    #result_rec = fact_rec(test_int)
    recu_end = time.time_ns()
    print("Recursive Method Time: ", ((recu_end - recu_start)/1000000), " ms")

    time.sleep(1)

    iter_start = time.time_ns()
    fact_iter(test_int)
    #result_iter = fact_iter(test_int)
    iter_end = time.time_ns()
    print("For-Loop Method Time: ", ((iter_end - iter_start)/1000000), " ms\n")

#print (result_rec == result_iter)

# In this Extra Credit Assignment, 
# please modify the recursive factorial function 
# to allow numbers greater than this limit set by python 
# without modifying the system recursion limit in python.  
# By this I mean you should not change sys.setrecursionlimit() .  
