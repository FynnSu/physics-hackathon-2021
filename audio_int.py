import numpy as np
from scipy.io.wavfile import write
from main import *



def audio(distance, length, time_frames):
    '''Function that creates an array for the audio signal at every time-step.'''
    r_list = np.sqrt((np.linspace(0, length, len(time_frames)) - length/2)**2 + distance**2)

    return (time_frames/(np.full((len(time_frames), len(r_list)), r_list)**2))




def exp_wav(
    sample,         # Array with the wave shape
    resolution      # Time between step (most likely 44100)
    ):
    '''Function that ouputs a .wav file given the list above.'''
    # seems to format it for .wav format
    waveform_quiet = sample * 0.3
    waveform_integers = np.int16(waveform_quiet * 32767)
    write("audiofile.wav", resolution, waveform_integers)
    return 

def main():
    args = parse_args()

    nPoints = args.n
    # theta0 = np.append(np.sin(np.linspace(0, 2 * np.pi, nPoints)) + np.sin(np.linspace(0, 4 * np.pi, nPoints)),
    #                        np.zeros(nPoints))

    theta0 = np.append(3*np.random.random(nPoints),
                            np.zeros(nPoints))

    frames = compute_motion(theta0, args.b, args.f, nPoints, args.dt, args.noise)
    print([1, 2, 3, 4])
    exp_wav(
        audio(
            1,
            1,
            frames[len(frames)//2:]
        ),
        44100
    )

    #make_gif(frames, "magical.gif")

if __name__ == '__main__':
    main()
