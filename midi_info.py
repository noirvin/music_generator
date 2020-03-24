import mido

midi = mido.MidiFile("chet1001.mid")

for i, track in enumerate(midi.tracks):

    for msg in track:

        if msg.type == 'set_tempo':
            print(msg.tempo)
