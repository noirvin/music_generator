import mido
def get_tempo(file):
    midi = mido.MidiFile(file)

    for i, track in enumerate(midi.tracks):

        for msg in track:

            if msg.type == 'set_tempo':
                return msg.tempo
