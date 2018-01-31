import numpy as np
import numpy.linalg as lalg


def read_coordinate_file(filename):
    global coordinates
    fileid=open(filename, 'r')
    num_lines = sum(1 for line in open(filename))
    coordinates=np.zeros((num_lines,2))
    i=0
    for line in fileid:
        temp=line.split(',')
        x=float(temp[0][1:])
        y=float(temp[1][:-2])
        coordinates[i, :] = [x, y]
        i+=1


read_coordinate_file('SampleCoordinates.txt')


print(coordinates)
