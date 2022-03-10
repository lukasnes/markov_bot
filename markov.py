"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    content = open(file_path).read()
    return content


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    split_text = text_string.split()
    for i in range(len(split_text) -2):
        tuple = (split_text[i],split_text[i+1])
        if tuple in chains:
            chains[tuple].append(split_text[i+2])
        else:
            chains[tuple] = [split_text[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    chains_list = list(chains)
    key_to_search = chains_list[0]
    
    def attach_words(key):
        words.append(key[0])
        words.append(key[1])
        chosen_word = choice(chains[key])
        words.append(chosen_word)
        key_to_search = (key[1],chosen_word)
        if key_to_search == key or key_to_search not in chains:
            return
        attach_words(key_to_search)
    
    attach_words(key_to_search)


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
