INPUT: a sentence
STEP 1: split into words
STEP 2: for each word (ignore words that include non-letter characters like gəl-get, 2005-ci, etc.)
    SUBSTEP 1: get possible options and their probabilitie (normalize to [0-1] range; doesn't matter how you get them, use deep ensembles or use symspell and convert the order to probabilities)
    SUBSTEP 2: continue with beam search to find the MOST LIKELY SENTENCE
    # idk how specifically this is supposed to work, you need to figure out the algorithm

RETURN the final sentence


- clean the sentence (,.:?!, etc), preprocessing
- ignore words that include non-letter characters like gəl-get, 2005-ci, etc.
- replace symspell w deep ensemble
- check ngram also
- somehow include probabilities from spelling correction part, limit with N
- merge words together in its initial form with punctuations at the end