from pydub import AudioSegment
import os
from textparse import textparser
import numpy as np

parse = textparser()
text = "hitotsu"

path = 'samples'
samples = {}

for name in os.listdir(path):
    fullpath = os.path.join(path, name)
    extension = name.split(".")[1][:3]
    name = name[:-4]
    audio = AudioSegment.from_file(fullpath, format=extension)
    samples[name] = audio

words = parse.parse(text)

string = AudioSegment.silent(duration=10)
for word in words:
    word_sound = AudioSegment.silent(duration=10)
    for character in word:
        word_sound = word_sound.append(samples[character.key()], crossfade = 10)
    string += word_sound

string.export("phrase.mp3", format="mp3")
