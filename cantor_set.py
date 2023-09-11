import matplotlib.pyplot as plt

def cantor_set(x, y, length, iterations):
    if iterations == 0:
        plt.plot([x, x + length], [y, y], color='black', lw=5)
        return
    new_length = length / 3
    cantor_set(x, y, new_length, iterations - 1)
    cantor_set(x + 2 * new_length, y, new_length, iterations - 1)
    y -= 10  # Move down for the next iteration
    cantor_set(x, y, new_length, iterations - 1)
    cantor_set(x + 2 * new_length, y, new_length, iterations - 1)

if __name__ == '__main__':
    plt.figure(figsize=(12, 8))
    plt.axis('scaled')
    cantor_set(0, 0, 1, 4)
    plt.show()
