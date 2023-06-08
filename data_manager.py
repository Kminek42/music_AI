from mido import MidiFile

file = MidiFile("raw_midi/Boku no Sensou.mid")
file = file.tracks[0]
start = 0
action = str(file[start]).split()
while action[0] != "note_on":
    start += 1
    action = str(file[start]).split()

i = 0
data = []
while start < len(file) - 1:
    if action[0] == "note_on" and action[3] == "velocity=0":
        i += 1
        data.append([int(action[2].split("=")[1]), int(action[4].split("=")[1])])
    start += 1
    action = str(file[start]).split()

print(data)
