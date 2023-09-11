import matplotlib.pyplot as plt
import numpy as np

def cantor_dust(x, y, side_length, iterations):
    if iterations == 0:
        plt.gca().add_patch(plt.Rectangle((x, y), side_length, side_length, fc='black'))
        return
    new_side = side_length / 3
    cantor_dust(x, y, new_side, iterations - 1)
    cantor_dust(x + 2 * new_side, y, new_side, iterations - 1)
    cantor_dust(x, y + 2 * new_side, new_side, iterations - 1)
    cantor_dust(x + 2 * new_side, y + 2 * new_side, new_side, iterations - 1)
    cantor_dust(x + new_side, y + new_side, new_side, iterations - 1)

if __name__ == '__main__':
    plt.figure(figsize=(6, 6))
    plt.axis('scaled')
    cantor_dust(0, 0, 1, 4)
    plt.show()
