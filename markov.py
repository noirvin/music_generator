import random
from dictogram import Dictogram
from collections import Counter, defaultdict, namedtuple

Note = namedtuple('Note', ['note', 'duration'])

class MarkovChain:


    def __init__(self):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = defaultdict(Counter)
         self.sums = defaultdict(int)



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

    def add(self, from_note, to_note, duration):
        self.markov_chain[from_note][self.get_tuple(to_note, duration)] += 1
        self.sums[from_note]+=1


    def get_tuple(self, note, duration):
        return Note(note, duration)




    def next_note(self, first_note):
        if first_note ==  None or first_note not in self.markov_chain:
            random_chain = self.markov_chain[random.choice(list(self.markov_chain.keys()))]
            return random.choice(list(random_chain.keys()))
        next_note_counter = random.randint(0, self.sums[first_note])
        for note, frequency in self.markov_chain[first_note].items():
            next_note_counter -= frequency
            if next_note_counter <= 0:
                return note





    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)
