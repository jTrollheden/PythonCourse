import numpy as np
import math


# Uppgift 1, läser in, räknar raderna och använder det sedan som ett index för vilken rad koordinaterna motsvarar
def read_coordinate_file(filename):
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


read_coordinate_file('SampleCoordinates.txt')

# Uppgift 2 - Punkterna plottas ut
import matplotlib.pyplot as plt


def plot_points(coord_list):
    fig1 = plt.figure()
    fig1.gca()  # Only needed for the ipython %matplotlib inline to display something
    plt.plot(coord_list, ".b")
    plt.show(block=False)


plot_points(coord_list)


# Uppgift 3 -


def construct_graph_connections(coord_list, radius):
    global indices
    global accDist
    indices = np.array([0, 0])
    accDist = np.array([0])
    for x in np.linspace(1, num_lines - 1, num_lines - 1):

        for k in np.linspace(x + 1, num_lines, num_lines - x):
            dist = np.sqrt(((coord_list[int(k - 1), 0] - coord_list[int(x - 1), 0]) ** 2 + (
                    coord_list[int(k - 1), 1] - coord_list[int(x - 1), 1]) ** 2))

            if dist < radius:
                indices = np.vstack((indices, [x, k]))
                accDist = np.vstack((accDist,dist))


radius = 0.08
construct_graph_connections(coord_list, radius)

indices=np.delete(indices, 0, axis=0)
accDist=np.delete(accDist, 0, axis=0)

# plt.show()
