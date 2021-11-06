from fluc_sim import one_step
from smh import apply_magic, make_gif
import numpy as np
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Magical String Simulation.')
    parser.add_argument('-n', type=int, default=50, help="number of particles in the string")
    parser.add_argument('-b', type=int, default=1, help="beta")
    parser.add_argument('-dt', type=float, default=1, help="timestep")
    parser.add_argument('-f', type=int, default=100, help="number of frames")

    return parser.parse_args()


def compute_motion(theta0, beta, nFrames, nPoints, dt):
    thetas = [theta0]
    for frame in range(nFrames):
        step1 = apply_magic(thetas[-1], dt=dt)
        step2 = one_step(step1, beta, 10)
        thetas.append(step2)

    return np.array(thetas)[:, :nPoints]


def main():
    args = parse_args()

    nPoints = args.n
    theta0 = np.append(np.sin(np.linspace(0, 2 * np.pi, nPoints)) + np.sin(np.linspace(0, 4 * np.pi, nPoints)),
                           np.zeros(nPoints))

    # theta0 = np.append(np.random.random(nPoints),
    #                        np.zeros(nPoints))

    frames = compute_motion(theta0, args.b, args.f, nPoints, args.dt)

    make_gif(frames, "magical.gif")


if __name__ == '__main__':
    main()
