# IMPORTS REQUIRED PACKAGES
import random
import string
import pandas as pd
#import sys
#import Person_pb2
#import binascii


# DEFINES VARIOUS SORT FUNCTIONS
# Defines quicksort function
def quicksort(array):
  
  # base case, arrays with 0 or 1 element are already "sorted"
  if len(array) < 2:
    return array

  else:
    # assigns pivot element
    pivot = array[0]
    # creates sub-array of all the elements less than the identified pivot
    less = [i for i in array[1:] if i <= pivot]
    # creates sub-array of all the elements greater than the identified pivot
    greater = [i for i in array[1:] if i > pivot]
    # recursive call of quicksort on the less-than and greater-than arrays (nesting the pivot in between)
    return quicksort(less) + [pivot] + quicksort(greater)

# Uses version of selection sort function from Week 2
def selectionSort(arr):
  for i in range(len(arr)): 
    min_index = i 
    min_value = arr[i]
    # cycles through remaining array to find next min value
    for j in range(i+1, len(arr)): 
        if arr[j] < min_value: 
            min_index = j 
            min_value = arr[j]
    # Swap the first element and the minimum element within the remaining unsorted portion of the array
    arr[i], arr[min_index] = arr[min_index], arr[i] 
  return arr

# Defines Bubble sort function (from geeksforgeeks.org)
def bubbleSort(arr): 
  n = len(arr) 
  # Traverse through all array elements 
  for i in range(n): 
      # Last i elements are already in place 
      for j in range(0, n-i-1): 
          # traverse the array from 0 to n-i-1 
          # Swap if the element found is greater 
          # than the next element 
          if arr[j] > arr[j+1] : 
              arr[j], arr[j+1] = arr[j+1], arr[j] 
  return arr

# Defines Insertion sort function (from geeksforgeeks.org)
def insertionSort(arr): 
  # Traverse through 1 to len(arr) 
  for i in range(1, len(arr)): 
      key = arr[i] 
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position 
      j = i-1
      while j >=0 and key < arr[j] : 
              arr[j+1] = arr[j] 
              j -= 1
      arr[j+1] = key 
  return arr

# Defines Strand sort function (drafted myself from online pseudo-code)
# Defines merge of pre-sorted lists first
def my_merge(l1, l2):
  result = []
  while (l1 and l2):
    if (l1[0] <= l2[0]):
        result.append(l1.pop(0))
    else:
        result.append(l2.pop(0))
  # Add the remaining of the lists
  result.extend(l1 if l1 else l2)
  return result

def strandSort(arr):
  if len(arr) < 2:
    return arr 
  result_arr = []
  while len(arr)>0:
    i = 0
    #sublist = []
    sublist = [arr.pop(0)]
    while i < len(arr):
      if arr[i] > sublist[-1]:
        sublist.append(arr.pop(i))
      else:
        i = i + 1
    result_arr = my_merge(sublist,result_arr)
  return result_arr

# Defines Gnome sort function (from geeksforgeeks.org with slight tweaks)
def gnomeSort(arr): 
  index = 1
  while index < len(arr): 
    if index == 0: 
        index = index + 1
    if arr[index] >= arr[index - 1]: 
        index = index + 1
    else: 
        arr[index], arr[index-1] = arr[index-1], arr[index] 
        index = index - 1
  return arr 

# Functional testing of quicksort, bubblesort, gnomesort, insertionsort, selectionsort, and strandsort functions
test_list = [1,10,6,5,2,9,7,4,3,8]
quicksort(test_list)

test_list = [1,10,6,5,2,9,7,4,3,8]
bubbleSort(test_list)

test_list = [1,10,6,5,2,9,7,4,3,8]
gnomeSort(test_list)

test_list = [1,10,6,5,2,9,7,4,3,8]
insertionSort(test_list)

test_list = [1,10,6,5,2,9,7,4,3,8]
selectionSort(test_list)

test_list = [1,10,6,5,2,9,7,4,3,8]
strandSort(test_list)


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

# Combines lists into dictionary and then converts to pandas dataframe
persons_dict = {'first_name':first_names, 'last_name':last_names, 'address':states}
persons_df = pd.DataFrame(persons_dict)
persons_df


# TESTS 1. QUICK SORT, 2. BUBBLE SORT, 3. GNOME SORT, 4. INSERTION SORT, 5. SELECTION SORT, AND 6. STRAND SORT

# # # LEFTOVER FROM PROF STARTER CODE
# # Creates test person object with username, fav number, and interest attributes
# person_obj = Person_pb2.Person()
# person_obj.user_name = 'Martin'
# person_obj.favorite_number = 1337
# person_obj.interests.extend(['daydreaming','hacking'])

# # Not 100% sure yet what this does but i'll figure it out!
# binascii.hexlify(person_obj.SerializeToString())
# person_obj.SerializeToString()
