# Imports required packages
import sys
import Person_pb2
import binascii

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

# Creates test person object with username, fav number, and interest attributes
person_obj = Person_pb2.Person()
person_obj.user_name = 'Martin'
person_obj.favorite_number = 1337
person_obj.interests.extend(['daydreaming','hacking'])

# Not 100% sure yet what this does but i'll figure it out!
binascii.hexlify(person_obj.SerializeToString())
person_obj.SerializeToString()






