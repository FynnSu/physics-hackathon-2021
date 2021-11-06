import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import imageio


def make_gif(positionFrames, outPath='movie.gif'):
    images = []
    ymin, ymax = np.min(positionFrames), np.max(positionFrames)
    for i in range(len(positionFrames)):
        fig, ax = plt.subplots()
        plt.ylim(ymin-1, ymax+1)
        ax.plot(range(len(positionFrames[0])), positionFrames[i])
        fname = f"tmp/tmp.png"
        plt.savefig(fname)
        images.append(imageio.imread(fname))
    imageio.mimsave(outPath, images)



def apply_gravity(theta, t, g, m, k):
    y1, vy1 = theta
    dthetadt = [vy1, -m*g-y1*k]
    return dthetadt


def apply_physics(positions, velocities, dx, dt, m, T):
    # Take an input array of positions, apply the physics on each point, and determine
    # the new positions after a time dt
    n = len(positions)
    new_positions = [0,0] # the second zero will be changed
    new_velocities = [0,0] # the second zero will be changed
    for i in range(2,n-1):
        # Find displacement on right/left side
        ldisp = positions(i-1)
        rdisp = positions(i+1)
        curdisp = positions(i)
        # Next compute the gradients. We will not use the approximation!
        sintheta = np.arcsin((curdisp - ldisp)/dx)
        sinpsi = np.arcsin((curdisp - rdisp)/dx)
        # Now we have that the equation of motion is m(acc) = -T(sintheta + sinpsi)
        # acc = -T/m * (sintheta + sinpsi)
        acc = -T/m * (sintheta + sinpsi)
        v = acc * dt
        s = curdisp*velocities(i) + 0.5 * acc * (dt**2)
        new_positions[i] = s
        new_velocities[i] = v 

    new_positions.append(0)
    new_velocities.append(0)

def main():
    print("Hello World")
    g = 10
    m = 1
    k = 1
    t = np.linspace(0,5,20)
    theta0 = (-5,0)

    sol = odeint(apply_gravity, theta0, t, args=(g, m, k))
    fig, ax = plt.subplots()
    ax.plot(t, sol[:, 0], label="position1")
    plt.legend()
    plt.show()


    madeuppositions = np.random.uniform(-1,1,[20,30])
    make_gif(madeuppositions)
    # Here I am creating the initial positions for 30 beads
    dx = 1
    dt = 0.002
    T = 0.01
    m = 0.001
    pos = []
    for i in range(30):
        pos.append(np.sin((2*np.pi * i)/(30*dx)))



if __name__ == '__main__':
    main()
