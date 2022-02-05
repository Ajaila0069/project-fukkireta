from pydub import AudioSegment
import os
from textparse import textparser
import numpy as np

parse = textparser()
text = ""

path = 'samples'
samples = {}

for name in os.listdir(path):
    fullpath = os.path.join(path, name)
    extension = name.split(".")[1][:3]
    name = name[:-4]
    audio = AudioSegment.from_file(name, format=extension)
    samples[name] = audio

words = parse.parse(text)

string = AudioSegment()
for word in words:
    word = AudioSegment()
    for character in word:
        word = word.append(samples[character.key()], crossfade=100)
    string += word
