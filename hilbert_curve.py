import matplotlib.pyplot as plt
import numpy as np

def hilbert_curve(x, y, dx, dy, n):
    if n == 0:
        plt.plot([x + dx / 2], [y + dy / 2], marker='o', markersize=3, color='black')
    else:
        dx /= 2
        dy /= 2
        hilbert_curve(x, y, dy, dx, n - 1)
        hilbert_curve(x + dx, y + dy, dy, -dx, n - 1)
        hilbert_curve(x + dx + dy, y + dy - dx, dy, dx, n - 1)
        hilbert_curve(x + dx + dy - dx, y + dy - dx - dy, -dy, -dx, n - 1)

if __name__ == '__main__':
    plt.figure(figsize=(8, 8))
    plt.axis('scaled')
    hilbert_curve(0, 0, 1, 0, 4)
    plt.show()
