#import inspect
import sys
import random 
import numpy as np
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
np.random.seed(3)
test_data = np.sort(np.random.randint(100,900,10))
test_data

sys.getrecursionlimit()
## sys.setrecursionlimit(5000) DANGEROUS!!

target = 998

start_time = time.time_ns()
#fact_rec(target)
result_rec = fact_rec(target)
end_time = time.time_ns()
print((end_time - start_time)/1000000)

start_time = time.time_ns()
#fact_iter(target)
result_iter = fact_iter(target)
end_time = time.time_ns()
print((end_time - start_time)/1000000)

print (result_rec == result_iter)

# In this Extra Credit Assignment, 
# please modify the recursive factorial function 
# to allow numbers greater than this limit set by python 
# without modifying the system recursion limit in python.  
# By this I mean you should not change sys.setrecursionlimit() .  
