import numpy as np
import random
import matplotlib.pyplot as plt


def energy_functional(sites):
    '''Functional that computes the energy for a given function.'''
    return np.sum((sites - np.roll(sites, 1)) ** 2)

def energy_functional_2d(sites):
    '''Functional for 2D surface'''
    return np.sum((sites - np.roll(np.array(sites), 1, axis=0))**2 + (sites - np.transpose(np.roll(np.transpose((np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))), 1, axis=0))))**2


def apply_change(to_sites, site, change):
    
    # Function to apply a change to some site
    to_sites[site] += change

    return to_sites

def apply_change_2d(to_sites, site_a1, site_a2, change):
    
    # Function to apply a change to some site
    to_sites[site_a1][site_a2] += change

    return to_sites  

def one_step_2d(sites, beta, iters=1):
    # Function that applies the metropolis algorithm once (to a number of different sites)
    for siteidx in np.random.choice(range(1,len(sites)-1), iters, replace=True):
        for siteidy in np.random.choice(range(1,len(sites[0])-1), iters, replace=True):
            # Picking site
            

            # change = random.choice([-1, 1])
            change = np.random.normal(0, 1)

            # Creating sites after applying the change
            potential_sites = apply_change(sites.copy(), siteidx, siteidy,  change)

            # Getting the change in energy
            energy_diff = energy_functional(potential_sites) - energy_functional(sites)

            # Now we apply the metropolis algorithm
            if energy_diff <= 0:  # Case where the energy of the surface is smaller
                sites = potential_sites
            else:  # Case where the energy of the surface is greater
                if random.random() < np.exp(-beta * energy_diff):
                    sites = potential_sites

    return sites

def one_step(sites, beta, iters=1):
    # Function that applies the metropolis algorithm once (to a number of different sites)
    for siteidx in np.random.choice(range(1,len(sites)-1), iters, replace=True):
        # Picking site
        focus_site = siteidx

        # change = random.choice([-1, 1])
        change = np.random.normal(0, 1)

        # Creating sites after applying the change
        potential_sites = apply_change(sites.copy(), focus_site, change)

        # Getting the change in energy
        energy_diff = energy_functional(potential_sites) - energy_functional(sites)

        # Now we apply the metropolis algorithm
        if energy_diff <= 0:  # Case where the energy of the surface is smaller
            sites = potential_sites
        else:  # Case where the energy of the surface is greater
            if random.random() < np.exp(-beta * energy_diff):
                sites = potential_sites

    return sites


    # # Picking site
    # focus_site = random.randint(1, len(sites)-2)
    #
    # # change = random.choice([-1, 1])
    # change = np.random.normal(0, 1)
    #
    # # Creating sites after applying the change
    # potential_sites = apply_change(sites.copy(), focus_site, change)
    #
    # # Getting the change in energy
    # energy_diff = energy_functional(potential_sites) - energy_functional(sites)
    #
    # # Now we apply the metropolis algorithm
    # if energy_diff <= 0:  # Case where the energy of the surface is smaller
    #     return potential_sites
    # else:  # Case where the energy of the surface is greater
    #     if random.random() < np.exp(-beta * energy_diff):
    #         return potential_sites
    #     else:
    #         return sites


def main():
    ############################
    # TESTING
    '''
    L_val = 50

    all_sites = np.zeros(L_val)

    for i in range(1000):
        all_sites = one_step(all_sites, 100)

    print(all_sites)

    plt.plot(all_sites)
    plt.show()
    '''
    [[1, 2, 3], [4, 5, 6], [ 7, 8, 9]][1][2]

    


if __name__ == '__main__':
    main()
