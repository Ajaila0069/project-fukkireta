from pydub import AudioSegment
import os
from tqdm import tqdm

name = "shelter"
try:
    os.mkdir(name)
except:
    pass

song = AudioSegment.from_mp3(f"{name}.mp3")
#song = AudioSegment.from_wav("song.wav")

offset = 49642
bpm = 100

ms_per_beat = 60000 // bpm

segments = {}

song = song[offset:]

i=0
while i < len(song):
    segments[str(i)+".mp3"] = song[i:i+ms_per_beat]
    i += ms_per_beat

for stamp, clip in tqdm(segments.items()):
    clip.export(name + "/" + stamp, format="mp3")
