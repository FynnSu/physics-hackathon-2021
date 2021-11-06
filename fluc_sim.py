import numpy as np
import random
import matplotlib.pyplot as plt


def energy_functional(sites):
    '''Functional that computes the energy for a given function.'''
    return np.sum((sites - np.roll(sites, 1)) ** 2)


def apply_change(to_sites, site, change):
    
    # Function to apply a change to some site
    to_sites[site] += change

    return to_sites


def one_step(sites, beta):
    # Function that applies the metropolis algorithm once

    # Picking site
    focus_site = random.randint(1, len(sites)-2)

    change = random.choice([-1, 1])

    # Creating sites after applying the change
    potential_sites = apply_change(sites.copy(), focus_site, change)

    # Getting the change in energy
    energy_diff = energy_functional(potential_sites) - energy_functional(sites)

    # Now we apply the metropolis algorithm
    if energy_diff <= 0:  # Case where the energy of the surface is smaller
        return potential_sites
    else:  # Case where the energy of the surface is greater
        if random.random() < np.exp(-beta * energy_diff):
            return potential_sites
        else:
            return sites


############################
# TESTING
L_val = 50

all_sites = np.zeros(L_val)

for i in range(1000000):
    all_sites = one_step(all_sites, 1)

print(all_sites)

plt.plot(all_sites)
plt.show()
