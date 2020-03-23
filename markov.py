import random
from dictogram import Dictogram


class MarkovChain:

    def __init__(self, midi_data):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(midi_data)
         self.first_note = list(self.markov_chain.keys())[0]

    def build_markov(self, midi_data):
        markov_chain = {}


        #get the current word and the word after
        current_note = midi_data[0]
        next_note = midi_data[1]
        time = midi_data[2]
        if current_note in markov_chain.keys(): #already there
            #get the histogram for that word in the chain
            histogram = markov_chain[current_note]
            #add to count
            histogram.dictionary_histogram[next_note] = histogram.dictionary_histogram.get(next_note, 0) + 1
        else: #first entry
            markov_chain[current_note] = Dictogram(midi_data)

        return markov_chain

    def generate_music(self, num_notes):

        with mido.midifiles.MidiFile() as midi:
            track = mido.MidiTrack()
            note = list(self.markov_chain.keys())[random.randrange(len(self.markov_chain)-1)]

        for _ in range(num_notes,out_filename):
            chain = self.markov_chain[note]
            next_note = chain.gen_rand_note(note)
            track.extend(next_note)
            note = next_note

        midi.tracks.append(track)
        midi.save(out_filename)






    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)
