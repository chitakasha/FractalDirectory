import matplotlib.pyplot as plt
import numpy as np

def dragon_curve(x, y, angle, length, iterations, direction=1):
    if iterations == 0:
        x_end = x + np.cos(angle) * length
        y_end = y + np.sin(angle) * length
        plt.plot([x, x_end], [y, y_end], color='black')
        return x_end, y_end
    else:
        angle1 = angle + direction * np.pi / 4
        length1 = length / np.sqrt(2)
        x, y = dragon_curve(x, y, angle1, length1, iterations - 1, 1)
        
        angle2 = angle - direction * np.pi / 4
        length2 = length / np.sqrt(2)
        x, y = dragon_curve(x, y, angle2, length2, iterations - 1, -1)
        
        return x, y

if __name__ == '__main__':
    plt.figure(figsize=(8, 8))
    plt.axis('scaled')
    dragon_curve(0, 0, 0, 1, 10)
    plt.show()
