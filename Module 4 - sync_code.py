# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:07:05 2019

@author: dev2
"""

def quicksort(array):
    
  print("Sorting array: {0}".format(array))  
    
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    
    print("{0} <{1}> {2}".format(less, pivot, greater))
    
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 13, 7, 8, 1, 15, 12, 8]))



import sys
sys.path.append('C:/Users/dev2/Documents/Teaching/Northwestern/Instruction/2019WI_MSDS_432-DL_SEC56/2019WI_MSDS_432-DL_SEC56/module4/')
import Person_pb2

person_obj = Person_pb2.Person()
person_obj.user_name = 'Martin'
person_obj.favorite_number = 1337
person_obj.interests.extend(['daydreaming','hacking'])

import binascii

binascii.hexlify(person_obj.SerializeToString())
person_obj.SerializeToString()






