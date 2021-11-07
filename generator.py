from smh import wizardry
import numpy as np
import argparse
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def parse_args():
    parser = argparse.ArgumentParser(description='Magical String Simulation.')
    parser.add_argument('-n', type=int, default=50, help="number of particles in the string")
    parser.add_argument('-b', type=int, default=1, help="beta")
    parser.add_argument('-dt', type=float, default=1, help="timestep")
    parser.add_argument('-m', type=float, default=1, help="mass unit")
    parser.add_argument('-k', type=float, default=1, help="spring constant")
    parser.add_argument('-f', type=int, default=100, help="number of frames")
    parser.add_argument('-noise', type=int, default=10, help="number of times to add noise per step")

    return parser.parse_args()


def genSurface(theta0, rows, dt, k=1, m=1):
    X, Y = np.meshgrid(np.linspace(0, 1, rows), np.linspace(0, 1, rows))
    t = [0, dt]
    fig, ax = plt.subplots(figsize=(10,10), subplot_kw={"projection": "3d"})
    ax.patch.set_facecolor("grey")
    ax.set_axis_off()
    canvas = FigureCanvas(fig)
    zmin, zmax = np.min(theta0[:rows**2]), np.max(theta0[:rows**2])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(zmin-1, zmax+1)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    # Customize the z axis.
    while True:
        # Plot the surface.
        zs = np.array(theta0)[:rows**2].reshape((rows, rows))
        if np.min(zs)<zmin: zmin = np.min(zs)
        if np.max(zs)<zmin: zmax = np.max(zs)
        surf = ax.plot_surface(X, Y, zs, cmap=cm.gist_gray,
                               linewidth=0, antialiased=False, vmin=zmin, vmax=zmax)

        canvas.draw()
        # yield current image
        yield np.array(canvas.buffer_rgba())
        surf.remove()
        # compute new position
        theta0 = odeint(wizardry, theta0, t, args=(m, k))[1]


def main():
    import cv2
    rows = 30
    t = [0,1]
    nframes = 100
    # Make data.
    X = np.linspace(-np.pi, np.pi, rows)
    Y = np.linspace(-np.pi, np.pi, rows)
    X, Y = np.meshgrid(X, Y)
    R = X**2+Y**2
    Z = (np.sin(X)*np.sin(Y)+np.cos(2*X))*np.exp(-R)

    theta0 = np.append(Z.flatten(),np.zeros(rows**2))
    mygenerator = genSurface(theta0, rows, 1)

    for thing in mygenerator:
        cv2.imshow("frame", thing)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()