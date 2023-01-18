# Dijkstra Algorithm

# Define sets
nodes = [1, 2, 3, 4, 5, 6, 7, 8]

# Define time and energy matrices
time = [[999, 1, 1, 999, 999, 999, 999, 999],
        [999, 999, 999, 4, 999, 999, 999, 999],
        [999, 999, 999, 2, 999, 999, 999, 999],
        [999, 999, 999, 999, 5, 999, 999, 999],
        [999, 999, 999, 999, 999, 1, 1, 999],
        [999, 999, 999, 999, 999, 999, 4, 999],
        [999, 999, 999, 999, 999, 999, 999, 4],
        [999, 999, 999, 999, 999, 999, 999, 999]]

energy = [[999, 0, 0, 999, 999, 999, 999, 999],
          [999, 999, 999, 0, 999, 999, 999, 999],
          [999, 999, 999, 1, 999, 999, 999, 999],
          [999, 999, 999, 999, 3, 999, 999, 999],
          [999, 999, 999, 999, 999, 0, 0, 999],
          [999, 999, 999, 999, 999, 999, 0, 999],
          [999, 999, 999, 999, 999, 999, 999, 0],
          [999, 999, 999, 999, 999, 999, 999, 999]]

# Set variables
ORIGIN_NODE = 1
DESTINATION_NODE = 8
AVAILABLE_TIME = 13
AVAILABLE_ENERGY = 4

# Initialize values
distance = [999] * len(nodes)
predecessor = [None] * len(nodes)
visited = [False] * len(nodes)

# Set starting node
distance[ORIGIN_NODE - 1] = 0

# Implement algorithm
while (False in visited):
    # Find node with minimum distance
    minDist = 9999
    minIndex = None
    for i in range(len(nodes)):
        if (not visited[i] and distance[i] < minDist):
            minDist = distance[i]
            minIndex = i

    # Mark node as visited
    visited[minIndex] = True

    # Update values
    for i in range(len(nodes)):
        if (not visited[i] and time[minIndex][i] != 999 
        and distance[i] > distance[minIndex] + time[minIndex][i] 
        and energy[minIndex][i] <= AVAILABLE_ENERGY):
            distance[i] = distance[minIndex] + time[minIndex][i]
            predecessor[i] = minIndex

energySpent = 0
for i in range(len(nodes)):
    if (predecessor[i] != None):
        energySpent += energy[predecessor[i]][i]

# Check if a solution exists
if (distance[DESTINATION_NODE - 1] > AVAILABLE_TIME or energySpent > AVAILABLE_ENERGY):
    print("No path can be found with the specified values")
    exit()

print("A path has been found with a total time of " +
      str(distance[DESTINATION_NODE - 1]) + " minutes")
print("The total energy spent is " + str(energySpent))

# Print route
route = []
current = DESTINATION_NODE - 1
while (current != None):
    route.append(current + 1)
    current = predecessor[current]
print("The route is: " + str(route[::-1]))