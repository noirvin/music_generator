#extracts and prepares midi data for MarkovChain


import hashlib
import mido
import argparse

from markov import MarkovChain

class MidiParser:

    def __init__(self, filename):

        self.filename = filename

        self.ticks = None

        self.tempo = None

        self.markov_chain = MarkovChain

    def parse(self):

        """
        reads midi and makes markov insertions

        """

        midi = mido.MidiFile(self.filename)
        self.ticks = midi.ticks_per_beat

        prev = []
        curr = []

        for track in midi.tracks:

            for msg in track:
                if False:
                    print(msg)

                if msg.type is "set_tempo":
                    self.tempo = msg.tempo

                elif msg.type is "note_on":
                    if msg.time is 0:
                        curr.append(msg.note)
                    else:
                        self.make_transition(prev,curr,msg.time)

    def make_transition(prev,curr,time):
        """
        inserts alk state transition possibilities into markov

        """
