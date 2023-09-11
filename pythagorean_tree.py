import matplotlib.pyplot as plt
import numpy as np

def pythagorean_tree(x, y, angle, length, iterations):
    if iterations == 0:
        return
    else:
        x1 = x + np.cos(angle) * length
        y1 = y + np.sin(angle) * length
        plt.plot([x, x1], [y, y1], color='black')
        
        angle1 = angle + np.pi / 4
        length1 = length / np.sqrt(2)
        pythagorean_tree(x1, y1, angle1, length1, iterations - 1)
        
        angle2 = angle - np.pi / 4
        length2 = length / np.sqrt(2)
        pythagorean_tree(x1, y1, angle2, length2, iterations - 1)

if __name__ == '__main__':
    plt.figure(figsize=(8, 8))
    plt.axis('scaled')
    pythagorean_tree(0, 0, np.pi / 2, 1, 10)
    plt.show()
