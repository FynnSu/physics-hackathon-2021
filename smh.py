import numpy as np
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


def apply_physics(positions, velocities, density, dt):
    pass


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

    # images = []
    # ymin, ymax = np.min(sol[:,0]), np.max(sol[:,0])
    # for i in range(len(sol)):
    #     fig, ax = plt.subplots()
    #     plt.ylim(ymin-1, ymax+1)
    #     ax.scatter(0, sol[i][0], label="position1")
    #     plt.legend()
    #     fname = f"tmp/tmp.png"
    #     plt.savefig(fname)
    #     images.append(imageio.imread(fname))
    # imageio.mimsave('movie.gif', images)


if __name__ == '__main__':
    main()
