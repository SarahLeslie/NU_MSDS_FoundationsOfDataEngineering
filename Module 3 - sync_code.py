# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 07:57:21 2019

@author: dev2
"""

import inspect
import sys

def fact(x):
    
    ## Added by Lance ##
    print("Function fact has been called with parameter x: {0} at memory location: {1}".format(x, inspect.currentframe()))
    print(sys._getframe(0))
    ## Added by Lance ##
    
    if x == 1:
        
        ## Added by Lance ##
        print("    Found 1!  Returning 1")
        ## Added by Lance ##
        
        return 1
    else:
        
        ## Added by Lance ##
        #print("  Now we will return {0} * fact({1})".format(x, x-1))
        print("  Have not found 1.  Calculating res...")
        res = fact(x-1) * x
        print("  Now we will return {0} * fact({1}) = {2} from the location: {3}".format(x, x-1, res, sys._getframe(0)))
        ## Added by Lance ##
        
        return res

print(fact(5))


def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

def fact_iter(x):
    ans = 1
    for i in range(1,x+1): 
        ans = ans * i 
    return ans
        
import time
import sys

target = 2950

sys.getrecursionlimit()
## sys.setrecursionlimit(5000) DANGEROUS!!

start_time = time.time()
fact(target)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
fact_iter(target)
end_time = time.time()
print(end_time - start_time)


