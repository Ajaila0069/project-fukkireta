from mido import MidiFile

mid = MidiFile("haruhi.mid")

key = 0
switch = {1:8,
          2:7,
          3:6,
          4:5,
          5:4,
          6:3,
          7:2,
          8:1,
          9:12,
          10:11,
          11:10,
          12:9}

start = list(range(1,89))
transp = [switch[(i%12)+1]+int(i//12) for i in start]

#def
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
