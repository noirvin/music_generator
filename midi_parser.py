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

        self.chain = None

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
                        print(prev,curr,msg.time)
                        self.make_transition(prev,curr,self.millisecond(msg.time))
                    prev = curr
                    curr = []


    def make_transition(self,prev,curr,time):
        """
        inserts all state transition possibilities into markov

        """

        for i in prev:
            for j in curr:
                midi_data= [i,j,self.millisecond(time)]
                self.chain=MarkovChain(midi_data)


    def millisecond(self,ticks):
        """
        tick to millisecond converter
        """
        milli = ((ticks / self.ticks) * self.tempo) / 1000
        return int(milli - (milli % 250) + 250)


if __name__ == "__main__":

    test= MidiParser("mozart_eine_kleine.mid")
    test.parse()
