import numpy as np
import math
import time
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import scipy.spatial as ss


def user_input():
    inp = input("What txt file do you want to read: Germany, Hungary or SampleCoordinates - Possible inputs: g, h and s")
    if inp == "g" or inp == "G":
        radius = 0.0025
        start_node = 1573
        end_node = 10584
        return "GermanyCities.txt", radius, start_node, end_node
    elif inp == "h" or inp == "H":
        radius = 0.005
        start_node = 311
        end_node = 702
        return "HungaryCities.txt", radius, start_node, end_node
    elif inp == "s" or inp == "S":
        radius = 0.08
        start_node = 0
        end_node = 5
        return "SampleCoordinates.txt", radius, start_node, end_node


def read_coordinate_file(filename):
    # Uppgift 1, läser in, splitar, stripar och därefter räknar om från latitud och longitud till x och y koordinater
    # enligt mercator projektion mha giva formler från PDF Computer Assignment 1.
    starttime=time.time()
    fileid = open(filename, 'r')
    coords = []
    for line in fileid:
        temp = line.split(',')
        x = float(temp[1].strip('}\n')) * math.pi / 180
        y = math.log(math.tan(math.pi / 4 + float(temp[0].strip('{')) * math.pi / 360))
        coords.append([x, y])
    fileid.close()
    coords = np.array(coords)
    endtime = "Computational time for reading the txt file: {}".format(time.time() - starttime)
    comptime.append(endtime)
    return coords


def plot_points(coord_list, connections, path):
    # Uppgift 2, 5 och 8 - punkterna, alla connections och den optimala vägen från start till slut plottas ut
    starttime=time.time()

    line_segments = LineCollection(coord_list[connections], zorder=0, color='cornflowerblue', linewidth=(1))
    path=np.array([path[:-1], path[1:]]).T
    reco_path = LineCollection(coord_list[path], linewidths=(2), color='r')

    fig1 = plt.figure()
    plt.axes().set_aspect('equal', 'datalim')
    ax = fig1.gca() # Only needed for the ipython %matplotlib inline to display something

    plt.scatter(coord_list[:, 0],coord_list[:,1], c="black", s=8)
    ax.add_collection(line_segments)
    ax.add_collection(reco_path)

    plt.show(block=False)

    endtime = "Computational time for plotting points: {}".format(time.time() - starttime)
    comptime.append(endtime)


# Uppgift 3 -


def construct_graph_connections(coord_list, radius):
    # Uppgift 3: Enumerate looparna används för att räkna ut distanserna mellan varje punkt för att sedan
    # jämföra dem med radien. De omvandlas sedan till numpy arrays för att kunna användas i construct graph funktionen.
    starttime=time.time()
    d = ss.distance.squareform(np.array(ss.distance.pdist(coord_list, metric='euclidean')))
    d[d > radius] = 0
    indices=np.array(np.nonzero(d)).T
    accdist = (d[indices[:,0],indices[:,1]])
    endtime = "Computational time for constructing the graph connections: {}".format(time.time() - starttime)
    comptime.append((endtime))
    return indices, accdist



def construct_fast_graph_connections(coord_list, radius):
    # Uppgift 10
    starttime = time.time()
    temp = ss.cKDTree(coord_list)
    indices_fast = temp.query_pairs(radius, output_type = "ndarray")
    indices_fast = np.vstack((indices_fast, (np.array(list(zip((indices_fast[:,1]), (indices_fast[:,0])))))))
    dist_fast = (np.sqrt((coord_list[indices_fast[:, 0]][:, 0] - coord_list[indices_fast[:, 1]][:, 0])**2 +
    (coord_list[indices_fast[:, 0]][:, 1] - coord_list[indices_fast[:, 1]][:, 1])**2))
    endtime = "Computational time for constructing the fast graph connections: {}".format(time.time() - starttime)
    comptime.append((endtime))
    return indices_fast, dist_fast


def construct_graph(indices, accdist, N):
    # Uppgift 4
    # Konstruerar en sparse matris (nollor där ingen data finns) baserad på distanserna mellan de koordinater som
    # ligger inom den givna radien för respektive .txt fil
    starttime=time.time()
    matrix = csr_matrix((accdist, (indices[:, 0], indices[:, 1])), shape=(N, N))
    endtime = "Computational time for constructing the graph: {}".format(time.time() - starttime)
    comptime.append(endtime)
    return matrix



def dijk(sparse):
    # Uppgift 6

    # I denna del matas en matris med dimensionerna (NxN) där N är antalet koordinater vi har fått inmatat från starten.
    # (i,j) i matrisen har värdet = distansen mellan koordinat i och j om den är mindre än radien (beroende på .txt fil)
    # Dijkstra kopplar samman alla dessa värden så att man har den kortaste distansen från en koordinat till alla andra
    # koordinater istället för endast till de som är innanför radien (som construct_graph gör)
    starttimedijk = time.time()
    dijk = dijkstra(sparse, return_predecessors=True, directed=True, indices=(start_node), unweighted=False)
    endtimedijk = "Computational time for dijkstra: {}".format(time.time() - starttimedijk)
    comptime.append((endtimedijk))
    return dijk


def compute_path(predecessor_matrix, end_node):
    # Uppgift 7
    # Då start_node redan blir indexerat i dijkstra för att spara tid så används inte start_node i denna funktion.
    # Möjligheten att inkorporera start_node finns men skulle bara förlänga processtiden.
    # I denna del används predecessor matrisen från dijksta algoritmen för att identifiera hur vägen ser ut. Funktionen
    # går steg för steg igenom predecessor och skapar en lista med "best path"
    starttime=time.time()
    steps=[]
    pos=end_node
    while pos!=-9999:
        steps.append(pos)
        pos=predecessor_matrix[pos]
    steps.reverse()
    endtime = "Computational time for computing the path: {}".format(time.time() - starttime)
    comptime.append((endtime))
    return steps


# Här körs funktionerna
comptime = []
a = user_input()
starttime_tot=time.time()
filename = a[0]
radius = a[1]
start_node = a[2]
end_node = a[3]

print(filename)

coord_list = read_coordinate_file(filename)

indices, accdist = construct_graph_connections(coord_list, radius)

indices, accdist = construct_fast_graph_connections(coord_list, radius)

N = len(coord_list)

sparse = construct_graph(indices, accdist, N)

dijk = dijk(sparse)

shortest_info = [compute_path(dijk[1], end_node), dijk[0][end_node]]
# Resultatet från compute_path tillsammans med total distans = shortest_info
print("The shortest path is: {} with a total distance of: {}".format(shortest_info[0], shortest_info[1]))

plot_points(coord_list, indices, shortest_info[0])

endtime_tot = "Computational time for the whole program: {}".format(time.time() - starttime_tot)
comptime.append(endtime_tot)
print(comptime)

plt.show()