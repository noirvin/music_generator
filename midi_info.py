import mido

midi = mido.MidiFile("mozart_eine_kleine.mid")

for i, track in enumerate(midi.tracks):

    for msg in track:

        print(msg)
