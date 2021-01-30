from spellchecker import  SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))

from Levenshtein import distance as levenshtein_distance
from fastDamerauLevenshtein import damerauLevenshtein

dist=levenshtein_distance('aaa_cb','aaa_bc')

print(dist)
dist2=damerauLevenshtein('aaa_cb', 'aaa_bc', similarity=False)
print(dist2)