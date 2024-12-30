from itertools import islice
from symspellpy import SymSpell, Verbosity

sym_spell = SymSpell()

dictionary_path = "unigrams.txt"

with open(dictionary_path, "r", encoding="utf-8") as dictionary_file:
    sym_spell._load_dictionary_stream(dictionary_file, term_index=0, count_index=1)

with open('input.txt', 'r', encoding='utf8') as file:
    input_sentence = file.read().strip()

words = input_sentence.split(" ")
max_length = len(words)

def transition_function(state):
    state += 1

    word = words[state]

    suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2, include_unknown=True)
    term_list = [i.term for i in suggestions]

    return [(term, state) for term in term_list]