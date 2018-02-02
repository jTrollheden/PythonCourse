import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.collections
from scipy.sparse.csgraph import dijkstra
import time
from scipy import spatial

#input to program
file_to_read = input('What country do you wish to travel in(g,h,s):')
stad_1 = input('From which city do you want to travel:')
stad_2 = input('To which city do you want to travel:')

if file_to_read == 'g':
    file_to_read = 'GermanyCities.txt'
    radius_search = 0.0025
elif file_to_read == 'h':
    file_to_read = 'HungaryCities.txt'
    radius_search = 0.005
else:
    file_to_read = 'SampleCoordinates.txt'
    radius_search = 0.08

start_time = time.time()

#Reads coordinates from file
def read_coordinate_file(file_name):
    file1 = open(file_name, 'r')
    coordinate_list_up = ([])

    for line in file1:
        coordinate_list_up.append(line)
    file1.close()
    return coordinate_list_up

#Plots the things, the cities, the cities that are connected, and the path between two chosen cities
def plot_points(coord_list, connected_cities, path):

    all_coords = ([])

    for i_1 in range(len(connected_cities)):
        temp_coords = [(coord_list[connected_cities[i_1][1]]), (coord_list[connected_cities[i_1][0]])]
        all_coords.append(temp_coords)
    lines1 = all_coords
    lc1 = matplotlib.collections.LineCollection(lines1, linestyles="-", linewidth=0.3)
    fig, ax = plt.subplots()
    ax.add_collection(lc1)

    all_coords2 = ([])
    for i_2 in range(len(path)-1):
        temp_coords = [(coord_list[path[i_2]]), (coord_list[path[i_2+1]])]
        all_coords2.append(temp_coords)
    lc2 = matplotlib.collections.LineCollection(all_coords2, linestyles="-", linewidth=1.2, colors='red')
    ax.add_collection(lc2)

    for j in range(len(coord_list)):
        plt.scatter(coord_list[j][0], coord_list[j][1], c='black')
    plt.show()


#Calculate what cities ae connected given a radius
def construct_fast_graph_connections(coord_list, radius):
    place = ([])
    distance_btw = ([])
    tree = spatial.cKDTree(coords)

    for i in range(len(coords)):
        placce = tree.query_ball_point([coords[i][0], coords[i][1]], radius_search)
        placce.remove(i)
        for j in range(len(placce)):
            place.append([i, placce[j]])
            temp_dist = [math.sqrt(
                math.pow(coords[i][0] - coords[placce[j]][0], 2) + math.pow(coords[i][1] - coords[placce[j]][1], 2))]
            distance_btw.append(temp_dist)

    return place, distance_btw

#Constracts matrix with distances between connected cities
def construct_graph(indices, distances, n):
    x_coords = []
    y_coords = []
    range_right = []
    for i_7 in range(len(indices)):
        x_coords.append(indices[i_7][0])
        y_coords.append(indices[i_7][1])
        range_right.append(distances[i_7][0])

    row = np.array(x_coords)
    col = np.array(y_coords)
    data = np.array(range_right)
    end_matrix = csr_matrix((data, (row, col)), shape=(n, n)).toarray()

    return end_matrix

#Calculates the path/route to take from start til' end
def compute_path(predecessor_matrix, start_node, end_node):
    done = 1
    run_node = end_node
    final_path = ([])
    final_path.append(end_node)
    while done != 0:
        #final_path.append(predecessor_matrix[start_node, run_node])
        final_path.append(predecessor_matrix[run_node])
        run_node = final_path[-1]
        if final_path[-1] == start_node:
            done = 0

    return final_path


#Calculates the total distance traveled
def total_distance_traveled(coordinate_list, route_traveled):
    total_distance_done=0
    for i_99 in range(len(route_traveled)-1):
        total_distance_done=total_distance_done+math.sqrt(math.pow(coordinate_list[route_traveled[i_99]][0]-coordinate_list[route_traveled[i_99+1]][0],2)+math.pow(coordinate_list[route_traveled[i_99]][1]-coordinate_list[route_traveled[i_99+1]][1],2))
    return total_distance_done


time_to_read = time.time()
coordinate_list = read_coordinate_file(file_to_read)



#Removes unwanted stuff from read file and creates a list with coordinates of all cities
coords = ([])

for i in range(len(coordinate_list)):

    coordinate_list_split = coordinate_list[i].split(',')
    coordinate_list_split[0] = coordinate_list_split[0].replace("{", "")
    coordinate_list_split[1] = coordinate_list_split[1].replace("}", "")
    coordinate_list_split[1] = coordinate_list_split[1].replace("\n", "")
    coordinate_list_split[1] = coordinate_list_split[1].replace(" ", "")
    coordinate_list_split[0] = math.log(math.tan(math.pi/4+math.pi*float(coordinate_list_split[0])/360))
    coordinate_list_split[1] = float(coordinate_list_split[1])*math.pi/180

    coordinate_list_split_temp = coordinate_list_split[0]
    coordinate_list_split[0] = coordinate_list_split[1]
    coordinate_list_split[1] = coordinate_list_split_temp
    coords.append(coordinate_list_split)

time_to_read = time.time() - time_to_read

time_to_connections = time.time()
placements, distance = construct_fast_graph_connections(coords, radius_search)
time_to_connections = time.time() - time_to_connections

time_to_matrix = time.time()
matrix = construct_graph(placements, distance, len(coords))
time_to_matrix = time.time() - time_to_matrix


time_to_dijkstra = time.time()
a, b = dijkstra(matrix, directed=False, indices=stad_1, return_predecessors=True, unweighted=False, limit=9999)
time_to_dijkstra = time.time()-time_to_dijkstra

time_to_path = time.time()
route = compute_path(b, int(stad_1), int(stad_2))
time_to_path = time.time()-time_to_path

time_to_plot = time.time()
plot_points(coords, placements, route)
time_to_plot = time.time()-time_to_plot

program_total_time = (time.time()-start_time) - time_to_plot

absolute_distance = total_distance_traveled(coords,route)

print("The time it takes for the whole program except plotting is: %4.3f \n"
        "The time it takes to plot is: %4.3f \n"
        "The time it takes to read coordinates from file is: %4.3f\n"
        "The time it takes to construct connections is: %4.3f\n"
        "The time it takes to construct the matrix is: %4.3f\n"
        "The time it takes to find the shortest path, Dijkstas algorithm: %4.3f\n"
        "The time it takes to find which path that should be taken: %4.3f\n"
        "The total distance traveled: %4.3f\n"
        % (program_total_time, time_to_plot, time_to_read, time_to_connections, time_to_matrix, time_to_dijkstra,
         time_to_path, absolute_distance))

print(route)