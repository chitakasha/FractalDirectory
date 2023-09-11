import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(x1, y1, x2, y2, x3, y3, iterations):
    if iterations == 0:
        plt.fill([x1, x2, x3, x1], [y1, y2, y3, y1], color='black')
    else:
        xm1, ym1 = (x1 + x2) / 2, (y1 + y2) / 2
        xm2, ym2 = (x2 + x3) / 2, (y2 + y3) / 2
        xm3, ym3 = (x3 + x1) / 2, (y3 + y1) / 2
        
        sierpinski_triangle(x1, y1, xm1, ym1, xm3, ym3, iterations - 1)
        sierpinski_triangle(xm1, ym1, x2, y2, xm2, ym2, iterations - 1)
        sierpinski_triangle(xm3, ym3, xm2, ym2, x3, y3, iterations - 1)

if __name__ == '__main__':
    plt.figure(figsize=(8, 8))
    plt.axis('scaled')
    
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 0.5, np.sqrt(3) / 2
    
    sierpinski_triangle(x1, y1, x2, y2, x3, y3, 4)
    
    plt.show()
