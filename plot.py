import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def line(a, b):
    x = np.linspace(a,b, num=100)
    y = x
    plt.plot(x, y, '-r', label='y=x')
    plt.title('Graph of y=x')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
