import numpy as np

def audio(distance, length, time_frames):
    x_pos_list = np.linspace(0, length, length(time_frames))

    r_list = np.sqrt((x_pos_list - length/2)**2 + distance**2)

    return (time_frames/(np.full((len(time_frames), len(r_list)), r_list)**2))

'''
a1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
a3 = np.array([1, 2, 3, 4])

a2 = np.full((len(a1), len(a3)), a3)

print(a2/(a1**2))

print(np.a2/(a1**2))

#np.transpose(a1)-a2'''