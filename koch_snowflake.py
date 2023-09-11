import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(x1, y1, x2, y2, iterations):
    if iterations == 0:
        plt.plot([x1, x2], [y1, y2], color='black')
    else:
        dx = x2 - x1
        dy = y2 - y1
        
        x3 = x1 + dx / 3
        y3 = y1 + dy / 3
        
        x4 = x1 + dx * 2 / 3
        y4 = y1 + dy * 2 / 3
        
        angle = np.arctan2(dy, dx) - np.pi / 3
        length = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        
        x5 = x3 + np.cos(angle) * length
        y5 = y3 + np.sin(angle) * length
        
        koch_snowflake(x1, y1, x3, y3, iterations - 1)
        koch_snowflake(x3, y3, x5, y5, iterations - 1)
        koch_snowflake(x5, y5, x4, y4, iterations - 1)
        koch_snowflake(x4, y4, x2, y2, iterations - 1)

if __name__ == '__main__':
    plt.figure(figsize=(8, 8))
    plt.axis('scaled')
    
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 0.5, np.sqrt(3) / 2
    
    koch_snowflake(x1, y1, x2, y2, 4)
    koch_snowflake(x2, y2, x3, y3, 4)
    koch_snowflake(x3, y3, x1, y1, 4)
    
    plt.show()
