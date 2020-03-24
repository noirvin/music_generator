#extracts and prepares midi data for MarkovChain


import hashlib
import mido
import argparse

from markov import MarkovChain

class MidiParser:

    def __init__(self, filename):

        self.filename = filename

        self.ticks = None

        self.tempo = 379747

        self.chain = MarkovChain()
        self.parse()

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

                if msg.type is 'set_tempo':
                    self.tempo = msg.tempo

                elif msg.type is 'note_on':
                    if msg.time is 0:
                        curr.append(msg.note)

                    else:
                        self.make_transition(prev,curr,msg.time)
                        prev = curr
                        curr = []


    def make_transition(self,prev,curr,time):
        """
        inserts all state transition possibilities into markov

        """
        print(prev,curr,time)
        for i in prev:
            for j in curr:
                self.chain.add(i,j,self.millisecond(time))



    def millisecond(self,ticks):
        """
        tick to millisecond converter
        """
        try:
            ms = ((ticks / self.ticks) * self.tempo) / 1000
            return int(ms - (ms % 250) + 250)
        except TypeError:
            raise TypeError(
                "Could not read a tempo and ticks_per_beat from midi")

    def get_markov(self):

        return self.chain


if __name__ == "__main__":

    test= MidiParser("chet1001.mid")
    test.parse()
    print(test.chain.get_chain())
