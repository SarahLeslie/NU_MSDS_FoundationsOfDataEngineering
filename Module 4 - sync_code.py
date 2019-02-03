# IMPORTS REQUIRED PACKAGES
import random
import string
import pandas as pd

import sys
import Person_pb2
import binascii


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


# LEFTOVER FROM PROF STARTER CODE
# Creates test person object with username, fav number, and interest attributes
person_obj = Person_pb2.Person()
person_obj.user_name = 'Martin'
person_obj.favorite_number = 1337
person_obj.interests.extend(['daydreaming','hacking'])

# Not 100% sure yet what this does but i'll figure it out!
binascii.hexlify(person_obj.SerializeToString())
person_obj.SerializeToString()






