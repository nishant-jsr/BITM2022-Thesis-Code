import numpy as np
import pandas as pd

# Defines functions in range [a, b]

# basic y = mx+c line
def line_slope_intercept(a, b, m, c):
    x = np.linspace(a,b, num=100)
    y = m*x + c
    return x, y

# basic y = x^2 parabola
def parabola_basic(a, b):
    x = np.linspace(a, b, num=100)
    y = x * x
    return x, y

#basic cubic curve aka y = x^3
def cubic_basic(a, b):
    x = np.linspace(a, b, num=100)
    y = x*x*x
    return x, y


