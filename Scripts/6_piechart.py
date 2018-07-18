import matplotlib.pyplot as plt

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,7,8]
activities = ['sleeping','eating','working','playing']
colors = ['m','c','r','b']

plt.pie(
        slices,
        labels = activities,
        colors = colors,
        startangle =180,
        shadow = True,
        counterclock = True,
        explode = (0,0.1,0,0),
        autopct = '%1.1f%%'
        )

plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')

plt.show()
