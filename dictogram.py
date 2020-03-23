#!python
from __future__ import division, print_function
import random # Python 2 and 3 compatibility


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        self.dictionary_histogram = dict()
        if word_list is not None:
            for word in word_list:

                self.add_count(word)



    def add_count(self, word, count=1):
        """ increase the frequency of a word by count"""
        if word in self.dictionary_histogram:
            self.dictionary_histogram[word] += count
        else:
            self.dictionary_histogram[word] = count
            self.types += 1

        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self.dictionary_histogram.keys():
            return self.dictionary_histogram[word]
        else:
            return 0
    def gen_rand_note(self):

        random_weight = random.randint(0,(weight_sum(self.dictionary_histogram)))
        threshold = 0
        for key, value in self.dictionary_histogram.items():

            threshold += value
            if threshold >= random_weight:
                return key


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def weight_sum(dictogram):
    sum=0
    for key, val in dictogram.items():
        sum+=val
    print(sum)
    return sum

def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
        dict_test = Dictogram(woodchuck_text.split())

        random_word = dict_test.gen_rand_word()
        print(random_word)


if __name__ == '__main__':
    main()
