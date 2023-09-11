import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_cube(ax, origin, size):
    for s, e in [(origin, origin+size), (origin+[0,size[1],0], origin+size+[0,size[1],0]), 
                 (origin+[0,0,size[2]], origin+size+[0,0,size[2]]), (origin+[size[0],0,0], origin+size+[size[0],0,0]), 
                 (origin+[0,size[1],size[2]], origin+size+[0,size[1],size[2]]), (origin+[size[0],0,size[2]], origin+size+[size[0],0,size[2]])]:
        ax.plot([s[0], e[0]], [s[1], e[1]], [s[2], e[2]], color="k")

def menger_sponge(ax, origin, size, level):
    if level == 0:
        draw_cube(ax, origin, size)
    else:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if not (i == 1 and j == 1 or i == 1 and k == 1 or j == 1 and k == 1):
                        new_origin = origin + size * np.array([i/3, j/3, k/3])
                        new_size = size / 3
                        menger_sponge(ax, new_origin, new_size, level-1)

import numpy as np

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('auto')
    origin = np.array([0, 0, 0])
    size = np.array([1, 1, 1])
    menger_sponge(ax, origin, size, 3)
    plt.show()
