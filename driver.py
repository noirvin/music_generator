from markov import MarkovChain

import random
import mido
import sys
from midi_parser import MidiParser



def write_messages(chain, note):
        return [
            mido.Message('note_on', note=note.note, velocity=127,
                         time=0),
            mido.Message('note_off', note=note.note, velocity=0,
                         time=note.duration)
        ]

def generate_music(chain, num_notes, out_filename):
    with mido.midifiles.MidiFile() as midi:
        track = mido.MidiTrack()
        last_note = None

        for i in range(num_notes):
            new_note = chain.next_note(last_note)
            track.extend(write_messages(chain,new_note))
        midi.tracks.append(track)
        midi.save(out_filename)

if __name__ == "__main__":

    chain = MidiParser(sys.argv[1]).get_markov()

    generate_music(chain,100,"test3.mid")
