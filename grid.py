import numpy as np

def generate_grid():
    base = np.random.permutation(np.arange(1, 7))
    array = np.array([
        np.roll(base, 0),
        np.roll(base, -2),
        np.roll(base, -4),
        np.roll(base, -1),
        np.roll(base, -3),
        np.roll(base, -5),
    ])
    return array
