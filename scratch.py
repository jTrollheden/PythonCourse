import numpy as np
import math
import time



def user_input():
    global radius
    global start_node
    global end_node
    inp = input("What txt file do you want to read: Germany, Hungary or SampleCoordinates - Possible inputs: g, h and s")
    if inp == "g" or inp == "G":
        radius = 0.0025
        start_node = 1573
        end_node = 10584
        return "GermanyCities.txt"
    elif inp == "h" or inp == "H":
        radius = 0.005
        start_node = 311
        end_node = 702
        return "HungaryCities.txt"
    elif inp == "s" or inp == "S":
        radius = 0.08
        start_node = 0
        end_node = 5
        return "SampleCoordinates.txt"


comptime = []
starttime_tot=time.time()

filename=user_input()
print(filename)

# Uppgift 1, läser in, räknar raderna och använder det sedan som ett index för vilken rad koordinaterna motsvarar
def read_coordinate_file(filename):
    starttime=time.time()
    global coord_list
    global num_lines
    fileid = open(filename, 'r')
    num_lines = sum(1 for line in open(filename))
    coord_list = np.zeros((num_lines, 2))
    i = 0
    for line in fileid:
        temp = line.split(',')
        x = float(temp[1][:-2]) * math.pi / 180
        y = math.log(math.tan(math.pi / 4 + float(temp[0][1:]) * math.pi / 360))
        coord_list[i, :] = [x, y]
        i += 1
    fileid.close()
    endtime = "Computational time for reading the txt file: {}".format(time.time() - starttime)
    comptime.append(endtime)


read_coordinate_file(filename)

# Uppgift 2 - Punkterna plottas ut
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors

def plot_points(coord_list, connections, path):
    starttime=time.time()
    #uppgift 5
    lines = []
    the_way=[]
    for x in range(0,connections.shape[0]):
        line=[]
        for k in range(0,2):
            pointer = connections[x, k]
            line.append((coord_list[int(pointer), 0], coord_list[int(pointer), 1]))
        lines.append(line)

    #Uppgift 8
    for x in range(0,len(path)-1):
        node=[]
        for k in range(x,x+2):
            pointer = path[k]
            node.append((coord_list[pointer, 0], coord_list[pointer, 1]))

        the_way.append(node)
    reco_path = LineCollection(the_way, linewidths=(5), color='r')
    line_segments = LineCollection(lines, linewidths=(0.3), color='cornflowerblue')

    fig1 = plt.figure()
    plt.axes().set_aspect('equal', 'datalim')
    ax = fig1.gca() # Only needed for the ipython %matplotlib inline to display something

    plt.scatter(coord_list[:, 0],coord_list[:,1], c="black", linewidths=0.5)
    ax.add_collection(line_segments)
    ax.add_collection(reco_path)

    plt.show(block=False)

    endtime = "Computational time for plotting points: {}".format(time.time() - starttime)
    comptime.append(endtime)



# Uppgift 3 -


def construct_graph_connections(coord_list, radius):
    starttime=time.time()
    indices = np.array([0, 0])
    accDist = np.array([0])
    for x in range(1,num_lines):
        for k in range(x+1, num_lines+1):
            dist = np.sqrt(((coord_list[int(k - 1), 0] - coord_list[int(x - 1), 0]) ** 2 + (
                    coord_list[int(k - 1), 1] - coord_list[int(x - 1), 1]) ** 2))
            if dist < radius:
                indices = np.vstack((indices, [x, k]))
                accDist = np.vstack((accDist,dist))
    indices = indices-1    #så att indexerna blir korrekta gentemot python syntaxen
    indices = np.delete(indices, 0, axis=0)
    for x in range(0, len(indices)):
        indices = np.vstack((indices, [indices[x, 1], indices[x, 0]]))
        accDist = np.vstack((accDist, accDist[x]))
    accDist = np.delete(accDist, 0, axis=0)

    endtime = "Computational time for constructing the graph connections: {}".format(time.time() - starttime)
    comptime.append((endtime))
    return indices, accDist


#indices, accDist = construct_graph_connections(coord_list, radius)

# här påkallas construct_graph_connections men den har kommenterats bort då den ger samma output som den snabbare


# Uppgift 10
import scipy.spatial as ss

def construct_fast_graph_connections(coord_list, radius):
    starttime = time.time()
    temp = ss.cKDTree(coord_list)
    indices_fast = np.array([0, 0])
    dist_fast = np.array([0])
    for x in range(len(temp.data)):
        in_range = (temp.query_ball_point(coord_list[x], radius))
        in_range.remove(x)
        for k in range(len(in_range)):
            temp_indices = [x, in_range[k]]
            indices_fast = np.vstack((indices_fast, temp_indices))

            dist = np.sqrt(((coord_list[x, 0] - coord_list[in_range[k], 0]) ** 2 + (
                    coord_list[x, 1] - coord_list[in_range[k], 1]) ** 2))
            dist_fast = np.vstack((dist_fast, dist))

    indices_fast = np.delete(indices_fast, 0, axis=0)
    dist_fast = np.delete(dist_fast, 0, axis=0)

    endtime = "Computational time for constructing the fast graph connections: {}".format(time.time() - starttime)
    comptime.append((endtime))
    return indices_fast, dist_fast


indices, accDist = construct_fast_graph_connections(coord_list, radius)



# Uppgift 4
N = len(coord_list)

def construct_graph(indices, accdist, N):
    starttime=time.time()
    from scipy.sparse import csr_matrix
    row = np.array(indices[:, 0])
    col = np.array(indices[:, 1])
    data = np.array(accdist[:, 0])

    endtime = "Computational time for constructing the graph: {}".format(time.time() - starttime)
    comptime.append((endtime))

    return csr_matrix((data, (row, col)), shape=(N, N)).toarray()

# 0 = rad, 1 = kolumn, 2 = data

sparse = construct_graph(indices, accDist, N)

#NxN matris som innehåller information om distanser mellan olika koordinater


# Uppgift 5


# Uppgift 6

from scipy.sparse.csgraph import dijkstra

starttimedijk = time.time()
dijk = dijkstra(sparse, return_predecessors=True, directed=False, indices=start_node, unweighted=False)
endtimedijk = endtime = "Computational time for dijkstra: {}".format(time.time() - starttimedijk)
comptime.append((endtimedijk))


# Uppgift 7
def compute_path(predecessor_matrix, start_node, end_node):
    #Då start_node redan blir indexerat i dijkstra för att spara tid så används inte start_node i denna funktion.
    # Möjligheten att inkorporera start_node finns men skulle bara förlänga processtiden.
    starttime=time.time()
    steps=[]
    pos=end_node
    while pos!=-9999:
        steps.insert(0, pos)
        pos=predecessor_matrix[pos]
    endtime = "Computational time for computing the path: {}".format(time.time() - starttime)
    comptime.append((endtime))
    return steps


shortest_info = [compute_path(dijk[1], start_node, end_node), dijk[0][end_node]]
print("The shortest path is: {} with a total distance of: {}".format(shortest_info[0], shortest_info[1]))

# Uppgift 8


plot_points(coord_list, indices, shortest_info[0])

# Uppgift 9

endtime_tot = "Computational time for the whole program: {}".format(time.time() - starttime_tot)
comptime.append(endtime_tot)
print(comptime)

plt.show()