import numpy as np


def read_coordinate_file(filename):
    fileid=open(filename,'r')
    for line in fileid:
        tempCord=line.split
        coordinates=tempCord.float

read_coordinate_file('SampleCoordinates.txt')



