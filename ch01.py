import nltk
from nltk.draw import dispersion
# nltk.download()
import numpy
import matplotlib
# pip install matplotlib

from nltk.book import *
#text1: Moby Dick by Herman Melville 1851
#text2: Sense and Sensibility by Jane Austen 1811
#text3: The Book of Genesis
#text4: Inaugural Address Corpus
#text5: Chat Corpus
#text6: Monty Python and the Holy Grail
#text7: Wall Street Journal
#text8: Personals Corpus
#text9: The Man Who Was Thursday by G . K . Chesterton 1908
print(text1)

def header(text):
    print(f"\n*** {text} ***\n")

# searching text
header('concordance')
text1.concordance("monstrous") # words in context
text2.concordance("monstrous") # words in context

# Similar
text1.similar("monstrous")
text2.similar("monstrous")
header("Common contexts")
text1.common_contexts(['monstrous','contemptible'])
text2.common_contexts(['monstrous','very'])
header('Dispersion plot')
# Dispersion plot
#text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America']) # numpy, matplotlib
# https://books.google.com/ngrams

header('Text generation')
text3.generate()

header('Vocabulary')
print(f"Length of text3: {len(text3)}")
# Token = sequence of characters to be grouped 
sortedSet = sorted(set(text3));
print(f"Sorted set text3: {sortedSet}")
print(f"Sorted set length of text3: {len(sortedSet)}")

print(f"Sorted set: {type(sortedSet)}")
print(f"text3: {type(text3)}")

# python slicing
myarray = ['only', 'through', 'me', 'can', 'you', 'come', 'to', 'the', 'father']

print(myarray[1:4]) # upper bound exclusive
print(myarray[-2:]) # the father

fdt2 = FreqDist(text2)
print(fdt2)
print(fdt2.most_common(50))
print(fdt2['Marianne'])

fdt2.plot(50, cumulative=True)

print(fdt2.hapaxes()) # single instance words ie unique
vocab = set(text2)
longWords = [w for w in vocab if(len(w)) >  15]
print(sorted(longWords))

# longer frequent words
header('Longer frequent words')
fdist5 = FreqDist(text5)
ft5 = sorted(w for w in set(text5) if(len(w) > 7 and fdist5[w] > 7))
print(ft5)

# Collocations
# Sequence occuring together. Resistant to substition with similes
# e.g. maroon wine

list()