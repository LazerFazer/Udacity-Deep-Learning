"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np


def softmax(x):
    return np.exp(x)/sum(np.exp(x))

def numerical_stability():
    x = 1e9

    for i in range(1000000):
        x += 1e-6
    x -= 1e9

    print(x)

numerical_stability()