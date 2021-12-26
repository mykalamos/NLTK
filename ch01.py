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