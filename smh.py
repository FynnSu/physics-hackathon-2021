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
        plt.close(fig)
        images.append(imageio.imread(fname))
    imageio.mimsave(outPath, images)


def apply_gravity(theta, t, g, m, k):
    y1, vy1 = theta
    dthetadt = [vy1, -m*g-y1*k]
    return dthetadt


def magic(theta, t, m, k, dx=1):
    ys, vys = theta[:len(theta)//2], theta[len(theta)//2:]
    ays = [0]
    for i in range(1,len(ys)-1):
        ays.append(m*k*((ys[i-1]-ys[i])+(ys[i+1]-ys[i])))
    ays.append(0)
    return np.append(vys,ays)


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
        sintheta = np.sin((curdisp - ldisp)/dx)
        sinpsi = np.sin((curdisp - rdisp)/dx)
        # Now we have that the equation of motion is m(acc) = -T(sintheta + sinpsi)
        # acc = -T/m * (sintheta + sinpsi)
        acc = -T/m * (sintheta + sinpsi)
        v = acc * dt
        s = curdisp*velocities(i) + 0.5 * acc * (dt**2)
        new_positions[i] = s
        new_velocities[i] = v 

    new_positions.append(0)
    new_velocities.append(0)

    return new_positions, new_velocities

def main():
    # print("Hello World")
    # g = 10
    # m = 1
    # k = 1
    # t = np.linspace(0,5,20)
    # theta0 = (-5,0)

    # sol = odeint(apply_gravity, theta0, t, args=(g, m, k))
    # fig, ax = plt.subplots()
    # ax.plot(t, sol[:, 0], label="position1")
    # plt.legend()
    # plt.show()
    #
    #
    # madeuppositions = np.random.uniform(-1,1,[20,30])
    # make_gif(madeuppositions)
    # # Here I am creating the initial positions for 30 beads
    # dx = 1
    # dt = 0.002
    # T = 0.01
    # m = 0.001
    # pos = []
    # for i in range(30):
    #     pos.append(np.sin((2*np.pi * i)/(30*dx)))

    # dx = 1
    # dt = 0.002
    # T = 0.01
    # m = 0.001
    # pos = []
    # velocs = np.zeros(30)
    # for i in range(30):
    #     pos.append(np.sin((2*np.pi * i)/(30*dx)))
    # for j in range(20):
    #     poss,velocss = apply_physics(pos,velocs, dx, dt, m, T)
    #     pos = poss
    #     velocs = velocss
    #
    # # madeuppositions = np.random.uniform(-1,1,[20,30])
    # make_gif(pos)
    # # Here I am creating the initial positions for 30 beads


    # points = 30
    # t = np.linspace(0,10,100)
    # theta0 = np.append(np.sin(np.linspace(0,2 * np.pi,points))+np.sin(np.linspace(0, 4 * np.pi,points)), np.zeros(points))
    # sol = odeint(magic, theta0, t, args=(1,1,1))
    # make_gif(sol[:,:len(sol[0])//2])

    points = 30
    t = [0,1]
    nframes = 100
    frames = [np.append(np.sin(np.linspace(0, 2 * np.pi, points)) + np.sin(np.linspace(0, 4 * np.pi, points)),
                           np.zeros(points))]

    for i in range(nframes):
        theta0 = frames[-1]
        sol = odeint(magic, theta0, t, args=(1, 1, 1))
        noise = np.append(np.append(np.append(0,np.random.uniform(-0.01,0.01, points-2)),0), np.zeros(points))
        frames.append(sol[1]+noise)

    make_gif(np.array(frames)[:,:points])


if __name__ == '__main__':
    main()
