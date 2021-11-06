import numpy as np

test_a = np.array([1, 2, 3, 4])

print(np.roll(test_a, 1))

def functional(sites):
    '''Functional that computes the energy for a given function.'''
    return np.sum((sites - np.roll(sites))**2)

