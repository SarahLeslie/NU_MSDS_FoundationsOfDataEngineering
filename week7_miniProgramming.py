# The image below shows possible routes to take on a road trip.  RoadTrip_NYC_to_L.A.JPG
# The nodes represent city names and vertices are the assumed hours the drive would take.
# First, use the breadth-first algorithm to find the quickest way to get to L.A from NYC 
# and calculate the time that it will take to get to L.A. from NYC using the breadth first algorithm 
# (use the weights assigned to the routes even though breadth-first works on unweighted edges 
# but you should calculate on the side).
# Print the route e.g. NYC -> DC -> ATL etc -> L.A.
# Then use Dijkstra's algorithm to find the most optimal route to get to L.A from NYC, 
# capture the time that it will take to get to L.A (use the weights in the algorithm assigned to the routes)
# Print the route e.g. NYC -> DC -> ATL etc -> L.A.
# Compare time of Breadth-first algorithm with Dijkstra's algorithm in terms of trip time and stops.
# Use Python (matplotlib or Seaborn) or JavaScript (D3) visualization tools to illustrate algorithm performance.

# IMPORTS REQUIRED PACKAGES
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# GENERATES THE GRAPH
graph = {}

# the nodes
nodes = ['NYC', 'DC', 'Atlanta', 'New Orleans', 'Dallas'
        , 'Indianapolis', 'Kansas City', 'Denver'
        , 'Pittsburg', 'Cincinnati', 'St Louis', 'Oklahoma City'
        , 'Salt Lake City', 'Albuquerque', 'Phoenix', 'Las Vegas', 'San Diego', 'Los Angeles']

# instatiate the nodes in the graph
for node in nodes:
    graph[node] = {}

# create the driving hours vertices for each node
# NYC
graph["NYC"]["DC"] = 2
graph["NYC"]["Indianapolis"] = 11
graph["NYC"]["Pittsburg"] = 7

# DC
graph["DC"]["Atlanta"] = 2

# Atlanta
graph["Atlanta"]["New Orleans"] = 2

# New Orleans
graph["New Orleans"]["Dallas"] = 2

# Dallas
graph["Dallas"]["Albuquerque"] = 2

# Indianapolis
graph["Indianapolis"]["Kansas City"] = 8

# Kansas City
graph["Kansas City"]["Denver"] = 7

# Denver
graph["Denver"]["Salt Lake City"] = 6

# Pittsburg
graph["Pittsburg"]["Cincinnati"] = 6

# Cincinnati
graph["Cincinnati"]["St Louis"] = 8

# St Louis
graph["St Louis"]["Oklahoma City"] = 7

# Oklahoma City
graph["Oklahoma City"]["Albuquerque"] = 9

# Salt Lake City
graph["Salt Lake City"]["Las Vegas"] = 9

# Albuquerque
graph["Albuquerque"]["Phoenix"] = 2

# Phoenix
graph["Phoenix"]["Las Vegas"] = 2
graph["Phoenix"]["San Diego"] = 5

# Las Vegas
graph["Las Vegas"]["San Diego"] = 2
graph["Las Vegas"]["Los Angeles"] = 5

# San Diego
graph["San Diego"]["Los Angeles"] = 2

graph.keys()

# checking
for node in graph.keys():
    for connection in graph[node].keys():
        print(node, " to ", connection, " is ", graph[node][connection], " hours")
# all set!


# DEFINES GRAPH SEARCH FUNCTIONS
# Breadth-First Search
def breadth_first_search(starting_city, ending_city):
  # instantiates 'connection counter' to track how far into the graph we're currently searching
  connect_counter = 1
  degree_incre_token = 'Degree Increment Token Here!'
  # instantiates the data structures to keep tracking of which nodes we have to search...
  # and which we've already searched for
  searched = [degree_incre_token]
  to_search = list(graph[starting_city])
  to_search.append(degree_incre_token)
  while to_search:
    city = to_search.pop(0)
    if city == degree_incre_token:
      connect_counter += 1
      to_search.append(city)
    if city not in searched:
      if city == ending_city:
        return connect_counter
      else:
        searched.append(city)
        to_search += list(graph[city])
  return False

# testing BFS
breadth_first_search('NYC', 'Los Angeles')

# Dijkstra's Algorithm
# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)

# testing Dijkstra


# TESTING
# instantiates list to capture time test results
results = []

# defines 2 functions to time test search method (1 for the lists, 1 for the set)
def graph_time_testing(name_to_search):
  start = time.perf_counter()
  graph_level = breadth_first_search('level_0_start', name_to_search)
  end = time.perf_counter()
  search_time = (end - start)*1000
  results.append({'Name':name_to_search
                      ,'Graph Level':str(graph_level)
                      ,'Search Time':search_time})

# runs time testing
for i in people_to_search_for:
  graph_time_testing(i)

# organizes results into pandas dataframe for easier exploration
results_df = pd.DataFrame(results)

sns.set(style="darkgrid")
sns.catplot(x="Graph Level", y="Search Time"
            , hue = "Graph Level", data=results_df, kind='swarm')
plt.show()
