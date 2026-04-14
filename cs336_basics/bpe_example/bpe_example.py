import numpy as np
import regex as re

SPECIAL_TOKENS = [re.escape("<|endoftext|>")]


def get_pair_stats(vocab):
    pass


def apply_merge(best_pair, vocab):
    pass


# read the a txt file
with open("bpe_test_corpus.txt") as f:
    text = f.read()
    print(text)

text = re.split("|".join(SPECIAL_TOKENS), text)

print(text)
