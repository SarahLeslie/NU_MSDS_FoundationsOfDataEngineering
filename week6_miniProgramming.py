# IMPORTS REQUIRED PACKAGES
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

fake = Faker()

# GENERATES LIST OF 3K FAKE NAMES TO SAMPLE FROM
num_names_needed = 5 + 5**2 + 5**3 + 5**4 + 5**5
fake.seed(7)
names = [fake.name() for _ in range(num_names_needed)]
# checking
names[0:10]
len(names)
len(set(names))
# there are dupes, which is ok but to be careful with assignment, we'll de-dupe this list
names = list(set(names))
len(names)


# SPLITS THE NAMES INTO UNIQUE LISTS FOR EACH LEVEL 
# determines the size of each list
lev_1_size = 5
lev_2_size = lev_1_size*5 - 2 # adding some dupes
lev_3_size = lev_2_size*5 - 4
lev_4_size = lev_3_size*5 - 16
lev_5_size = lev_4_size*5 - 64
# instantiating name lists for each level
first_lev = names[:lev_1_size]
second_lev = names[lev_1_size:lev_1_size+lev_2_size]
third_lev = names[lev_1_size+lev_2_size:lev_1_size+lev_2_size+lev_3_size]
fourth_lev = names[lev_1_size+lev_2_size+lev_3_size:lev_1_size+lev_2_size+lev_3_size+lev_4_size]
fifth_lev = names[lev_1_size+lev_2_size+lev_3_size+lev_4_size:lev_1_size+lev_2_size+lev_3_size+lev_4_size+lev_5_size]
# checking
lev_1_size == len(first_lev)
lev_2_size == len(second_lev)
lev_3_size == len(third_lev)
lev_4_size == len(fourth_lev)
lev_5_size == len(fifth_lev)
# adding duplicate names to each list to fill out max possible (won't need all) level requirements
second_lev = second_lev + second_lev[:2]
third_lev = third_lev + third_lev[:4]
fourth_lev = fourth_lev + fourth_lev[:16]
fifth_lev = fifth_lev + fifth_lev[:64]
# checkin final sizes
len(first_lev) == 5
len(second_lev) == 5*len(set(first_lev))
len(third_lev) == 5*len(set(second_lev))
len(fourth_lev) == 5*len(set(third_lev))
len(fifth_lev) == 5*len(set(fourth_lev))

# GENERATES TEST Graph
people_graph = {}

# we'll want a starting point...
people_graph['level_0_start'] = list(first_lev)

# creates 5 connections for each first level person 
# 1 dupe in second level 
# but dupes will never be connected to the same person in the previous level because lists are orderd
for i in range(len(first_lev)):
  people_graph[first_lev[i]] = second_lev[5*i:5*i+5]

# de-dupes level 2 so we don't assign their 5 level 3 connections twice
second_lev = list(dict.fromkeys(second_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(second_lev)):
  people_graph[second_lev[i]] = third_lev[5*i:5*i+5]

third_lev = list(dict.fromkeys(third_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(third_lev)):
  people_graph[third_lev[i]] = fourth_lev[5*i:5*i+5]

fourth_lev = list(dict.fromkeys(fourth_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(fourth_lev)):
  people_graph[fourth_lev[i]] = fifth_lev[5*i:5*i+5]

# not sure this is necessary but... 
# let's imagine the level 5 people all have 'facebook accounts with no friends' vs. 'not having accounts'
fifth_lev = list(dict.fromkeys(fifth_lev)) # preserves order vs using set.  not that it matters much
for i in range(len(fifth_lev)):
  people_graph[fifth_lev[i]] = []

# checking
len(people_graph) == lev_1_size + lev_2_size + lev_3_size + lev_4_size + lev_5_size + 1

# checking to see that each connection has 0 dupes
true_counter = 0 
for i in people_graph.keys():
  true_counter = true_counter + (len(people_graph[i]) == len(set(people_graph[i])))

true_counter == len(people_graph)
# all set!


# lastly, let's create a list of the people to search for
people_to_search_for = []
random.seed(7)
people_to_search_for.append(first_lev[random.randint(0,lev_1_size-1)])
people_to_search_for += [second_lev[i] for i in random.sample(range(lev_2_size), 2)]
people_to_search_for += [third_lev[i] for i in random.sample(range(lev_3_size), 3)]
people_to_search_for += [fourth_lev[i] for i in random.sample(range(lev_3_size), 4)]
people_to_search_for += [fifth_lev[i] for i in random.sample(range(lev_3_size), 5)]


# DEFINES BREADTH-FIRST SEARCH FUNCTION
def search(starter_name, search_for_name):
  # instantiates 'connection counter' to track how far into the graph we're currently searching
  connect_counter = 1
  degree_incre_token = 'Degree Increment Token Here!'
  # instantiates the data structures to keep tracking of who we have to search (and what their degree is)...
  # (could use dict on my pc since python 3.7 preserves ordering of keys based on insert, 
  # but in case this is run with another version of python..)
  # and who we've already searched for
  searched = [degree_incre_token]
  to_search = list(people_graph[starter_name])
  to_search.append(degree_incre_token)
  while to_search:
    person = to_search.pop(0)
    # if person == "Karen Holland":
    #   return('stop')
    if person == degree_incre_token:
      connect_counter += 1
      to_search.append(person)
    if person not in searched:
      if person == search_for_name:
        return("We found " + person + "!  They are in level " + str(connect_counter) + " of the graph.")
      else:
        searched.append(person)
        to_search += list(people_graph[person])
  return("Can't find " + search_for_name + ".  :(")

# testing the initial search function
for i in people_to_search_for:
  search('level_0_start', i)


# TESTING
# instantiates list to capture time test results
time_results = []

# defines 2 functions to time test search method (1 for the lists, 1 for the set)
def list_time_testing(search_function,method_label,test_list,search_for_list):
    indeces = [9999, 29999, 49999, 69999, 89999, 99999]
    for i in range(len(search_for_list)):
        item = search_for_list[i]
        start = time.perf_counter()
        search_function(test_list,item)
        end = time.perf_counter()
        search_time = (end - start)*1000
        time_results.append({'Search Function':method_label
                              ,'Index':indeces[i]
                              ,'Search Time':search_time})

def set_time_testing(test_set,search_for_list):
  for i in range(len(search_for_list)):
      item = search_for_list[i]
      start = time.perf_counter()
      test_set.remove(item)
      end = time.perf_counter()
      search_time = (end - start)*1000
      time_results.append({'Search Function':"Set '.remove()'"
                          ,'Index':'NA'
                          ,'Search Time':search_time})

# organizes results into pandas dataframe for easier exploration
results_df = pd.DataFrame(time_results)
results_df.loc[results_df['Index'] == 'NA', 'Search Time'].mean()

sns.catplot(x="Search Function", y="Search Time"
            , hue = "Index", data=results_df)
plt.show()

sns.catplot(x="Index", y="Search Time"
            , hue = "Search Function", data=results_df)
plt.show()

sns.catplot(x="Search Function", y="Search Time"
            , hue = "Index"
            , data=results_df.loc[results_df['Search Function']!='Linear Search for Unsorted List'])
plt.show()\
    