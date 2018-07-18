import matplotlib.pyplot as plt
import csv
import numpy as np

##############  PART 1  ##############
#READING FROM A LOCAL TEXT FILE USING CSV METHOD

x = []
y = []

'''
with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label = 'Loaded from file')
'''

'''
with open('example.txt') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    x, y = zip(*plots)
'''

##############  PART 2  ##############
#READING FROM A LOCAL TEXT FILE USING NUMPY ! ! !


'''
x, y = np.loadtxt('example.txt', delimiter = ',', unpack = True)

plt.plot(x, y, label = 'Loaded from file')
'''

plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')

plt.legend()

plt.show()
