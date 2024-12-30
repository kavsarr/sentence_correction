from symspell import transition_function, max_length
from ngram import scoring_function
from beam import beam_search

start = -1
beam_width = 10

result = beam_search(start, transition_function, scoring_function, beam_width, max_length)

print(result)

# print(transition_function(2))