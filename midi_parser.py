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

    
