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
    # instantiates the data structures to keep tracking of which nodes we have to search...
    # and which we've already searched for
    searched = [starting_city]
    to_search = []
    # instantiates separator string to print formatted path
    seperator = ' -> '
    
    # gets neighbor nodes from starting point
    neighbors = graph[starting_city].keys()
    for neighbor in neighbors:
        # for each neighbor, create path from starting point to neighbor
        new_path = list([starting_city])
        new_path.append(neighbor)
        # if we found the ending point, calculate the driving time based on the path...
        # and return the path, driving time, and number of stops
        if neighbor == ending_city:
            driving_time = 0 
            for first in range(len(new_path)-1) :
                driving_time += graph[new_path[first]][new_path[first+1]]
            formatted_path = seperator.join(new_path)
            return(formatted_path + " takes " + str(driving_time) + " hours in " + str(len(new_path)-1) + " stops.")
        else:
            # else, append the full path to the search queue to continue searching
            to_search.append(new_path)
    
    # while stilll paths to search
    while to_search:
        # get the next path
        path = to_search.pop(0)
        # find the last city in that path
        city = path[-1]
        # if the city's neighbors have yet to be checked
        if city not in searched:
            # get the city's neighbors
            neighbors = graph[city].keys()
            for neighbor in neighbors:
                # for each neighbor, extend the current path to that neighbor
                new_path = list(path)
                new_path.append(neighbor)
                # if we found the ending point, calculate the driving time based on the path...
                # and return the path, driving time, and number of stops
                if neighbor == ending_city:
                    driving_time = 0 
                    for first in range(len(new_path)-1) :
                        driving_time += graph[new_path[first]][new_path[first+1]]
                    formatted_path = seperator.join(new_path)
                    return formatted_path, driving_time, (len(new_path)-1)
                    #return(formatted_path + " takes " + str(driving_time) + " hours in " + str(len(new_path)-1) + " stops.")
                else :
                    # else, append the full path to the search queue to continue searching
                    to_search.append(new_path)
                    # and add that city to 'searched' to indicated that its neighbors have been checked
                    searched.append(city)
    return False

# testing BFS
breadth_first_search('NYC', 'Los Angeles')

# Dijkstra's Algorithm - lowest cost function
def find_lowest_cost_node(costs, processed):
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
    return lowest_cost_node, lowest_cost

# Rest of Dijkstra's Algorithm
def dijkstras(starting_city, ending_city):
    # instantiates the costs and parents tables
    costs = {}
    parents = {}

    # adds infinity for all nodes' costs...
    # and adds 'None's for all nodes' parents
    infinity = float("inf")
    for no in graph.keys():
        costs[no] = infinity
        parents[no] = None

    # adds costs and parents for starting point's neighbor nodes
    for connection in graph[starting_city].keys():
        costs[connection] = graph[starting_city][connection]
        parents[connection] = starting_city
    
    # instantiates list of already processed nodes
    processed = [starting_city]

    # Find the lowest-cost node that you haven't processed yet.
    node, cost = find_lowest_cost_node(costs, processed)
    # If you've processed all the nodes, the 'lowest cost node' will be None
    while node is not None:
        # Go through all the neighbors of this node.
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if new_cost < costs[n]:
                # ... update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
        # Mark the node as processed.
        processed.append(node)
        # Find the next node to process, and loop.
        node, cost = find_lowest_cost_node(costs, processed)
    
    # constructs outputs
    separator = " -> "
    path = []
    current = ending_city
    while parents[current] is not None:
        path = [current] +  path
        current = parents[current]
    if path:
        path = [current] +  path
        formatted_path = separator.join(path)
        #return(formatted_path + " takes " + str(costs[ending_city]) + " hours in " + str(len(path)-1) + " steps.")
        return formatted_path, costs[ending_city], (len(path)-1)
    else :
        return None

# testing Dijkstra
dijkstras('NYC', 'Los Angeles')

# RESULTS CAPTURE
# instantiates list to capture time test results
results = []
bfs = breadth_first_search('NYC', 'Los Angeles')
d = dijkstras('NYC', 'Los Angeles')
results.append({'Method Used':'Breadth-First Search'
                ,'Path':bfs[0]
                ,'Total Driving Time':bfs[1]
                ,'Number of Stops':bfs[2]})
results.append({'Method Used':'Dijkstra\'s Algorithm'
                ,'Path':d[0]
                ,'Total Driving Time':d[1]
                ,'Number of Stops':d[2]})

# organizes results into pandas dataframe for easier exploration
results_df = pd.DataFrame(results)
results_melted = pd.melt(results_df, id_vars='Method Used'
                        , var_name="Result Type", value_vars=["Number of Stops", "Total Driving Time"]
                        , value_name="Values")

sns.set(style="darkgrid")
ax = sns.barplot(x="Result Type", y="Values", hue = "Method Used", data=results_melted)
for col in ax.patches:
    height = col.get_height()
    ax.text(col.get_x()+col.get_width()/2., height + 1.5,
            int(height), ha="center") 
plt.show()
