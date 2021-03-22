import pydub
from pydub import AudioSegment
import os
from textparse import textparser

path = 'samples'

samples = {}

for name in os.listdir(path):
    fullpath = os.path.join(path, name)
    extension = name.split(".")[1][:3]
    name = name[:-4]
    audio = AudioSegment.from_file(name, format=extension)
    samples[name] = audio
