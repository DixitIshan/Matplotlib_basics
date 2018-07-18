import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [7, 2, 7, 9, 16]

x1 = [1,3,5,7,9]
y1 = [7,8,2,4,6]

plt.bar(x, y, label = 'FIRST', color = 'c')
plt.bar(x1, y1, label = 'SECOND', color = 'r')

plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')

plt.title('BARCHART PLOTTING')

plt.legend()

plt.show()
