import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [7,8,9,1,2,1]

plt.title("SCATTER PLOTTING")

plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')

plt.scatter(x, y, s = 100, color = 'cyan', label = "SCATTER PLOT")

plt.legend()

plt.show()
