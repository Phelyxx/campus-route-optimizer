# Dijkstra Algorithm

# Define sets
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


# 30x30 time matrix
time = [[999] * 30 for i in range(30)]
time[0][1] = 1
time[0][2] = 1
time[1][3] = 4
time[2][3] = 2
time[3][4] = 3
time[3][9] = 4
time[3][28] = 4
time[3][22] = 4
time[3][25] = 4
time[3][24] = 5
time[4][5] = 1
time[4][6] = 1
time[5][7] = 2
time[6][7] = 2
time[7][8] = 1
time[8][12] = 1
time[9][10] = 1
time[9][11] = 1
time[10][12] = 6
time[11][12] = 4
time[12][13] = 1
time[12][14] = 1
time[13][15] = 2
time[14][15] = 3
time[15][16] = 1
time[17][16] = 3
time[17][18] = 2
time[18][19] = 1
time[19][20] = 1
time[20][21] = 1
time[21][22] = 2
time[22][23] = 1
time[24][19] = 2
time[24][16] = 3
time[25][19] = 1
time[26][15] = 3
time[26][21] = 2
time[27][22] = 1
time[28][4] = 1
time[28][9] = 2
time[28][27] = 1
time[29][15] = 3
time[29][16] = 3


# 30x30 energy matrix
energy = [[999] * 30 for i in range(30)]
energy[0][1] = 0
energy[0][2] = 0
energy[1][3] = 0
energy[2][3] = 2
energy[3][4] = 2
energy[3][9] = 2
energy[3][28] = 1
energy[3][22] = 3
energy[3][25] = 3
energy[3][24] = 3
energy[4][5] = 0
energy[4][6] = 0
energy[5][7] = 0
energy[6][7] = 1
energy[7][8] = 1
energy[8][12] = 1
energy[9][10] = 0
energy[9][11] = 0
energy[10][12] = 0
energy[11][12] = 3
energy[12][13] = 1
energy[12][14] = 1
energy[13][15] = 1
energy[14][15] = 1
energy[15][16] = 1
energy[17][16] = 0
energy[17][18] = 2
energy[18][19] = 0
energy[19][20] = 0
energy[20][21] = 0
energy[21][22] = 1
energy[22][23] = 1
energy[23][20] = 1
energy[23][16] = 3
energy[24][20] = 1
energy[25][16] = 2
energy[25][21] = 1
energy[26][23] = 1
energy[27][4] = 1
energy[27][28] = 1
energy[27][9] = 1
energy[27][26] = 1
energy[28][29] = 1
energy[29][15] = 2
energy[29][16] = 2


# Set variables
SOURCE_NODE = 1
DESTINATION_NODE = 17
AVAILABLE_TIME = 11
AVAILABLE_ENERGY = 7


# Initialize values
distance = [999] * len(nodes)
predecessor = [None] * len(nodes)
visited = [False] * len(nodes)

# Set the starting node
distance[SOURCE_NODE - 1] = 0

# Implement the algorithm
while (False in visited):
    # Find the node with the minimum distance
    minDist = 9999
    minIndex = None
    for i in range(len(nodes)):
        if (not visited[i] and distance[i] < minDist):
            minDist = distance[i]
            minIndex = i

    # Mark the node as visited
    visited[minIndex] = True
    
    # Update the values
    for i in range(len(nodes)):
        if (not visited[i] and time[minIndex][i] != 9999 
        and distance[i] > distance[minIndex] + time[minIndex][i] + energy[minIndex][i] 
        and energy[minIndex][i] <= AVAILABLE_ENERGY):
            distance[i] = distance[minIndex] + time[minIndex][i] 
            predecessor[i] = minIndex

energySpent = 0
for i in range(len(nodes)):
    if (predecessor[i] != None):
        energySpent += energy[predecessor[i]][i]


print("A path with a total time of " + str(distance[DESTINATION_NODE - 1]) + " minutes has been found")
print("The total energy spent is " + str(energySpent))

# Print route
route = []
current = DESTINATION_NODE - 1
while (current != None):
    route.append(current + 1)
    current = predecessor[current]
print("The route is: " + str(route[::-1]))