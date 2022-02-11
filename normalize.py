from pydub import AudioSegment
import os

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

path = "me when"
target_path = "when the"

for name in os.listdir(path):
    print(name)
    fullpath = os.path.join(path, name)
    sound = AudioSegment.from_file(fullpath, "mp3")
    normalized_sound = match_target_amplitude(sound, -20.0)
    normalized_sound.export(os.path.join(target_path, name), format="mp3")
