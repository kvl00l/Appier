# Solution 2

import string

# Delete all punctuations
def strip_punctuation(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line

# Import text file
filepath = 'D:\DATA Science\Appier\Text file.txt'

word_count = {}

with open(filepath, 'r') as fi:
    # Each line
    for line in fi:
        # Remove punctuation
        line = strip_punctuation(line)
        # Seperate words into a list
        words = line.split()

        # Each word in words
        for word in words:
            # Convert the word too lowercase
            word = word.lower()
            # Check if it isn't Not in the dictionary
            if word not in word_count:
                # If not, create new entry
                word_count[word] = 0
            # Then, increment it's count by 1
            word_count[word] += 1

# List 10 of the words
list(word_count.keys())[:10]

# Traverse those 5 words and print count
five_words = list(word_count.keys())[:10]
for word in five_words:
    # Words minimal take up to 15 spaces; count take minimum 8 words
    print("{0:15}{1:8}".format(word, word_count[word]))

# Values of the key
def order_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        # (dictionary[key], key)
        sorted_values.append((dictionary[key], key))
    # Sort the tuples based on values
    sorted_values = sorted(sorted_values)
    # Reverse the order
    sorted_values = sorted_values[::-1]
    return sorted_values

# Top word
top_words = order_dict_by_freq(word_count)[:10]
for tuple_freq in top_words:
    count, word = tuple_freq
    print("{0:15}{1:8}".format(word, count))