"""
dictgen.py

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

def main():
    """
    Step through the functions and produce results, informing the user along
    the way.
    """
    print("Hello World!")

def generate_word_permute():
    """
    Given a number of letters, generate a list of every possible word
    combination using every letter in the alphabet to the desired "length".

    Upper and lower case.
    """
    return []

def generate_num_permute():
    """
    Given a number of nums, generate a list of every possible combination of
    numbers to the desired length.
    """
    return []

def generate_special_chars_permute():
    """
    Given a number of special characters, generate a list of every possible
    combination of special characters to the desired length.
    """
    return []

if __name__ == "__main__":
    main()
