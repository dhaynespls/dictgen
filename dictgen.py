"""
dictgen.py

This is not efficient on memory at all.

The WPA2 password hint is as follows:

1) It contains two words/acronyms, one with 3 letters and the other with 4
letters. Each letter can be upper or lower case. The two words are separated.

2) It contains 4 consecutive digits.

3) It contains two special characters, the ones above the numbers on the
keyboard. The characters are separated.

4) The orders of the words, digits, and special characters can be arbitrary.

You need to generate a dictionary according to the hint.

1) One of the special character is @.

2) The four-letter word is cyse, but each letter can be upper or lower case.

3) You should be able to find the four digits on my personal website or ECE website. Note that there can be multiple possibilities of the four digits.
"""
# Future Imports for py2 backwards compat.
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python std. lib.
import itertools

def main():
    """
    Step through the functions and produce results, informing the user along
    the way.
    """
    # Every upper and lower case combination of 'cyse'
    word_one = ['cyse', 'cysE', 'cySe', 'cySE', 'cYse', 'cYsE', 'cYSe', 'cYSE',
                'Cyse', 'CysE', 'CySe', 'CySE', 'CYse', 'CYsE', 'CYSe', 'CYSE']
    # Every permutation of all 26 letters of the alphabet in upper and lower
    # case
    word_two = generate_word_permute(3)
    with open('word_two.txt', 'w') as f:
        for permute in word_two:
            f.write(''.join(permute) + '\n')
    # All 4 digit numbers from:
    # https://ece.gmu.edu/people/full-time-faculty/kai-zeng
    # http://ece.gmu.edu/~kzeng2/
    digits = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
              '2014', '2015', '2016', '2017', '3252', '1000', '1200', '5933',
              '3100', '4400', '4444', '1569', '1601', '1981']
    # Include the '@' character
    special_char_one = ['@']
    # Every possible single special character 
    special_char_two = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                        ')', '-', '_', '=', '+']

    with open('out.txt', 'w') as outfile:
        # For every permutation, also print out all combinations
        print("Hello World")

def generate_word_permute(length):
    """
    Given a number of letters, generate a list of every possible word
    combination using every letter in the alphabet to the desired "length".

    Upper and lower case.
    """
    letters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return itertools.permutations(letters, length)

if __name__ == "__main__":
    main()
