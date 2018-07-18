import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

x1 = [10, 11, 12]
y1 = [13, 14, 15]

x2 = [20, 21, 22]
y2 = [23, 24, 25]

#NOMENCLATURE OF THE AXIS
plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')

#PLOTTING OF GRAPHS OF ABOVE ARRAY
plt.plot(x, y, label = 'First')
plt.plot(x1, y1, label = 'Second')
plt.plot(x2, y2, label = 'Third')

#NAME OF THE TITLE TO SHOW
plt.title('FIRST EVER MATPLOTLIB GRAPH')

#DIFFERENTIATION OF 3 GRAPHS
plt.legend()

#DISPLAY OF PLOTTED GRAPHS
plt.show()
