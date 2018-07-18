import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 55, 88, 5, 12, 4, 57, 9, 105, 6, 32, 4, 72, 94, 26, 59, 16, 53, 86, 10, 45, 34, 65, 85, 25, 35, 25, 14, 16, 36, 17, 27, 38, 49, 56, 10, 64]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(population_ages, bins, histtype = 'bar', rwidth = .2)

plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')

plt.title('HISTOGRAM PLOTTING')

#plt.legend()

plt.show()
