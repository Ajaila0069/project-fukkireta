from pydub import AudioSegment
import os
from textparse import textparser
import numpy as np
from numpy.fft import rfft, rfftfreq, irfft

tone = 256

parse = textparser()
with open("the funny.txt", "r") as a:
    text = a.read()
    a.close()

path = 'the me'
samples = {}

for name in os.listdir(path):
    if not name.startswith("."):
        fullpath = os.path.join(path, name)
        extension = name.split(".")[1][:3]
        name = name[:-4]
        print(name)
        audio = AudioSegment.from_file(fullpath, format=extension)
        samples[name] = audio

words = parse.parse(text)
print(words)

string = AudioSegment.silent(duration=12)
for word in words:
    print(word)
    word_sound = AudioSegment.silent(duration=12)
    for character in word:
        yf = rfft(samples[character.key()].get_array_of_samples())

        shift = int(tone-440) #
        yf = np.roll(yf, shift)
        if shift > 0:
            yf[:shift] = 0
        else:
            yf[-shift:] = 0
        pitch_shift = samples[character.key()]._spawn(irfft(yf).astype(word_sound.dtype))

        word_sound = word_sound.append(pitch_shift, crossfade = 12)
    string += word_sound

string.export("song.mp3", format="mp3")
