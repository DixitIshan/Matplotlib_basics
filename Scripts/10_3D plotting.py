from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

##############################################################################
# THE BELOW CODE IS FOR LINE GRAPHING

fig = plt.figure()
ax1 = fig.add_subplot(111, projection = '3d')

x = [1,2,3,4,5,6,7,8,9]
y = [3,4,5,6,7,8,9,0,1]
z = [6,7,8,9,0,1,2,3,4]

ax1.plot_wireframe(x,y,z)

ax1.set_xlabel('X_AXIS')
ax1.set_ylabel('Y_AXIS')
ax1.set_zlabel('Z_AXIS')

plt.show()

###############################################################################
# THE BELOW CODE IS FOR SCATTER PLOTTING

fig = plt.figure()
ax1 = fig.add_subplot(111, projection = '3d')

x = [1,2,3,4,5,6,7,8,9]
y = [3,4,5,6,7,8,9,0,1]
z = [6,7,8,9,0,1,2,3,4]

ax1.scatter(x, y, z, c = 'g', marker = 'o')

ax1.set_xlabel('X_AXIS')
ax1.set_ylabel('Y_AXIS')
ax1.set_zlabel('Z_AXIS')

plt.show()
