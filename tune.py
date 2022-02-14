from pydub import AudioSegment
import os
from textparse import textparser
import numpy as np
from numpy.fft import rfft, rfftfreq, irfft
import matplotlib.pyplot as plt

path = 'when the'
target_path = 'the me'
samples = {}

for name in os.listdir(path):
    if not name.startswith("."):
        fullpath = os.path.join(path, name)
        extension = name.split(".")[1][:3]
        name = name[:-4]
        print(name)
        audio = AudioSegment.from_file(fullpath, format=extension)
        samples[name] = audio

print("loaded")

for name, sound in samples.items():
    print(name)
    sample = sound.get_array_of_samples()
    sample = np.array(sample)
    datatype = sample.dtype
    N = len(sound) * (sound.frame_rate // 1000)
    T = 1.0 / sound.frame_rate
    yf = rfft(sample)
    xf = rfftfreq(N, T)[:N//2]

    index = min(range(len(xf)), key=lambda i: abs(xf[i]-400))
    i = sorted(((value, index) for index, value in enumerate(yf[:index])), reverse=True)[0][1]
    fund = list(zip(yf, xf))[i][1]

    shift = int(440-int(fund)) #
    yf = np.roll(yf, shift)
    if shift > 0:
        yf[:shift] = 0
    else:
        yf[-shift:] = 0
    print(fund, i, shift)
    """
    fig, ax = plt.subplots()
    #ax.set_xscale('log')
    ax.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    ax.set_title(name)
    ax.grid()
    plt.show()
    """
    pitch = irfft(yf)
    shifted_sound = sound._spawn(pitch.astype(np.int16))
    shifted_sound.export(os.path.join(target_path, name + ".mp3"), format="mp3")
