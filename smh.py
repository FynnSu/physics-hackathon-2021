import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import imageio
from tqdm import tqdm
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas




def make_gif(positionFrames, outPath='movie.gif'):
    images = []
    ymin, ymax = np.min(positionFrames), np.max(positionFrames)
    for i in tqdm(range(len(positionFrames)), desc="Making GIF"):
        fig, ax = plt.subplots()
        plt.ylim(ymin-1, ymax+1)
        ax.plot(range(len(positionFrames[0])), positionFrames[i])
        fname = f"tmp/tmp.png"
        plt.savefig(fname)
        plt.close(fig)
        images.append(imageio.imread(fname))
    imageio.mimsave(outPath, images)

def get_string_plot(frame, ymin, ymax):
    fig, ax = plt.subplots()
    canvas = FigureCanvas(fig)
    plt.ylim(ymin - 1, ymax + 1)
    ax.plot(range(len(frame)), frame)

    width, height = fig.get_size_inches() * fig.get_dpi()
    canvas.draw()
    buf = canvas.buffer_rgba()
    # convert to a NumPy array
    X = np.asarray(buf)
    return X

def make_wizard_gif(positionFrames, outPath='movie.gif'):
    images = []
    X, Y = np.meshgrid(range(len(positionFrames[0])),range(len(positionFrames[0])))
    ymin, ymax = np.min(positionFrames), np.max(positionFrames)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_axis_off()
    canvas = FigureCanvas(fig)
    # Customize the z axis.
    ax.set_zlim(ymin-1, ymax+1)
    for i in tqdm(range(len(positionFrames)), desc="Making GIF"):
        # Plot the surface.
        surf = ax.plot_surface(X, Y, positionFrames[i], cmap=cm.coolwarm,
                               linewidth=0, antialiased=False, vmin=ymin, vmax=ymax)

        # Add a color bar which maps values to colors.
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        canvas.draw()
        im = np.array(canvas.buffer_rgba())
        images.append(im)
        surf.remove()

    imageio.mimsave(outPath, images)


def apply_gravity(theta, t, g, m, k):
    y1, vy1 = theta
    dthetadt = [vy1, -m*g-y1*k]
    return dthetadt


def magic(theta, t, m, k):
    ys, vys = theta[:len(theta)//2], theta[len(theta)//2:]
    ays = [0]
    for i in range(1,len(ys)-1):
        ays.append(m*k*((ys[i-1]-ys[i])+(ys[i+1]-ys[i])))
    ays.append(0)
    return np.append(vys, ays)


def wizardry(theta, t, m, k):
    nRows = int(np.sqrt(len(theta)//2))
    ys, vys = np.array(theta[:len(theta)//2]).reshape(nRows, nRows), np.array(theta[len(theta)//2:])
    ays = [np.zeros(len(ys))]
    for i in range(1, nRows-1):
        row = [0]
        for j in range(1, nRows-1):
            row.append(m*k*((ys[i-1][j]-ys[i][j])+(ys[i+1][j]-ys[i][j])+(ys[i][j-1]-ys[i][j])+(ys[i][j+1]-ys[i][j])))
        row.append(0)
        ays.append(row)
    ays.append(np.zeros(len(ys)))
    return np.append(vys, np.array(ays).flatten())


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


def apply_magic(theta, dt, m=1, k=1):
    t = [0, dt]
    sol = odeint(magic, theta, t, args=(m, k))
    return sol[1]


def main():
    rows = 30
    t = [0,1]
    nframes = 100
    # Make data.
    X = np.linspace(-np.pi, np.pi, rows)
    Y = np.linspace(-np.pi, np.pi, rows)
    X, Y = np.meshgrid(X, Y)
    R = X**2+Y**2
    Z = (np.sin(X)*np.sin(Y)+np.cos(2*X))*np.exp(-R)
    frames = [np.append(Z.flatten(),np.zeros(rows**2))]
    for frame in range(nframes-1):
        frames.append(odeint(wizardry, frames[-1], t, args=(1, 1))[1])
    ys = np.array(frames)[:, :rows**2]
    make_wizard_gif(ys.reshape((nframes, rows, rows)), "wizardry.gif")


    points = 30
    t = [0,1]
    nframes = 100
    frames = [np.append(np.sin(np.linspace(0, 2 * np.pi, points)) + np.sin(np.linspace(0, 4 * np.pi, points)),
                           np.zeros(points))]
    for i in range(nframes):
        theta0 = frames[-1]
        sol = odeint(magic, theta0, t, args=(1, 1))
        noise = np.append(np.append(np.append(0,np.random.uniform(-0.01,0.01, points-2)),0), np.zeros(points))
        frames.append(sol[1]+noise)

    posFrames = np.array(frames)[:,:points]
    make_gif(posFrames)


if __name__ == '__main__':
    main()
