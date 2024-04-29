# Solution 2

import string

# Delete all punctuations
def strip_punctuation(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line

# Import text file
filepath = ''

word_count = {}

