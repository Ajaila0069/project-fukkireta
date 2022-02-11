from pydub import AudioSegment
import os
from textparse import textparser
import numpy as np

parse = textparser()
with open("the funny.txt", "r") as a:
    text = a.read()
    a.close()

#text = "zutto soba de miteru yo BAKKUAPPU wa makasete hidari kara migi e to dekigoto ga acchi kocchi docchi kimi wa koko ni iru no? BAASUDEI mada saki desho? ii kagen ni koyubi kara  mienai ito shuchou shinai"
path = 'when the'
samples = {}

for name in os.listdir(path):
    fullpath = os.path.join(path, name)
    extension = name.split(".")[1][:3]
    name = name[:-4]
    audio = AudioSegment.from_file(fullpath, format=extension)
    samples[name] = audio

words = parse.parse(text)
print(words)

string = AudioSegment.silent(duration=12)
for word in words:
    print(word)
    word_sound = AudioSegment.silent(duration=12)
    for character in word:
        word_sound = word_sound.append(samples[character.key()], crossfade = 12)
    string += word_sound

string.export("phrase.mp3", format="mp3")
