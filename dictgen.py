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
    word_one = generate_word_permute(3)
    word_two = generate_word_permute(4)
    digits = generate_num_permute(4)
    special_chars = generate_special_chars_permute(2)
    # https://stackoverflow.com/a/4233765
    l = [word_one, word_two, digits, special_chars]
    final_dict = [''.join(s) for s in itertools.product(*l)]
    print(str(final_dict))

def generate_word_permute(length):
    """
    Given a number of letters, generate a list of every possible word
    combination using every letter in the alphabet to the desired "length".

    Upper and lower case.
    """
    letters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return [''.join(permute) for permute in itertools.permutations(letters, length)]

def generate_num_permute(length):
    """
    Given a number of nums, generate a list of every possible combination of
    numbers to the desired length.
    """
    numbers = '0123456789'
    return [''.join(permute) for permute in itertools.permutations(numbers, length)]

def generate_special_chars_permute(length):
    """
    Given a number of special characters, generate a list of every possible
    combination of special characters to the desired length.
    """
    special_chars = '~`!@#$%^&*()-_=+'
    return [''.join(permute) for permute in itertools.permutations(special_chars, length)]

if __name__ == "__main__":
    main()
