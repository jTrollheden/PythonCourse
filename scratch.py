import numpy as np

#Uppgift 1, läser in, räknar raderna och använder det sedan som ett index för vilken rad koordinaterna motsvarar
def read_coordinate_file(filename):
    global coord_list
    fileid=open(filename, 'r')
    num_lines = sum(1 for line in open(filename))
    coord_list=np.zeros((num_lines,2))
    i=0
    for line in fileid:
        temp=line.split(',')
        x=float(temp[0][1:])
        y=float(temp[1][:-2])
        coord_list[i, :] = [x, y]
        i+=1

#Uppgift 2 - Punkterna plottas ut
import matplotlib.pyplot as plt

def plot_points(coord_list):
    fig1 = plt.figure()
    fig1.gca()  # Only needed for the ipython %matplotlib inline to display something
    plt.plot(coord_list,".b")
    plt.show()



read_coordinate_file('SampleCoordinates.txt')
print(coord_list)

plot_points(coord_list)

#Uppgift 3 -