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

[~] => aircrack-ng seven-01.cap -w /home/dhaynes/development/dictgen/out.txt

      [00:26:53] 3993012/5406699 keys tested (2511.41 k/s)

      Time left: 9 minutes, 22 seconds                          73.85%

                         KEY FOUND! [ CySE2017@GMu) ]


      Master Key     : 78 BC DE 0B 28 9E DA 47 E7 01 86 C2 83 0E 23 D8
                       17 45 0E DF 50 39 75 DE 4D 01 AA E9 A7 18 15 F5

      Transient Key  : 1C 91 9C DE 07 4F CB CB 5C FD 85 BC 7A 30 85 91
                       C0 71 E6 48 B2 7C E5 30 74 63 FF A5 35 CE 73 73
                       6C 31 88 A6 5D 79 FC 05 D2 B1 F1 34 58 B8 4C 16
                       B0 5F 51 C2 1C 75 8D 5E F6 01 C2 F1 BC 5A 2F AA

      EAPOL HMAC     : 3B A0 60 05 C7 A9 28 59 02 9F 38 E7 14 D5 21 A9
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
    # Every permutation of GMU
    word_two = ['gmu', 'gmU', 'gMu', 'gMU', 'Gmu', 'GmU', 'GMu', 'GMU']

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

    # The dictionary text file we will write to
    with open('out.txt', 'w') as outfile:
        # For every product, also print out all permutations
        for product in itertools.product(word_one,
                                         ['gmu', 'gmU', 'gMu', 'gMU', 'Gmu', 'GmU', 'GMu', 'GMU'],
                                         digits, special_char_one,
                                         special_char_two):
            for permute in itertools.permutations(product, len(product)):
                outfile.write(''.join(permute) + '\n')

if __name__ == "__main__":
    main()
