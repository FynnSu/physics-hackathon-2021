import numpy as np
from scipy.io.wavfile import write

def audio(distance, length, time_frames):
    '''Function that creates an array for the audio signal at every time-step.'''
    r_list = np.sqrt((np.linspace(0, length, length(time_frames)) - length/2)**2 + distance**2)

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

