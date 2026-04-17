import regex as re

SPECIAL_TOKENS = [re.escape("<|endoftext|>")]

# read the a txt file
with open("bpe_test_corpus.txt") as f:
    text = f.read()

text = re.split("|".join(SPECIAL_TOKENS), text)
text = text[0]

# pre-tokenization

split_text = text.split()
pre_tokenized_dict = {}
for pre_tokens in split_text:
    pre_tokenized_dict[tuple([c for c in pre_tokens])] = split_text.count(pre_tokens)

print(pre_tokenized_dict)


# Single Merge
# print("Single Merge: ")
# print("######")

def merge_pair(tokenized_dict):

    pairs_dict = {}

    def get_pair_count(pre_token_tuple, pairs_dict):
        for i in range(len(pre_token_tuple) - 1):
            pair = (pre_token_tuple[i], pre_token_tuple[i + 1])
            if pair in pairs_dict:
                pairs_dict[pair] += tokenized_dict[pre_token_tuple]
            else:
                pairs_dict[pair] = tokenized_dict[pre_token_tuple]
        return pairs_dict

    for pre_token_tuple in tokenized_dict.keys():
        pairs_dict = get_pair_count(pre_token_tuple, pairs_dict)
    print("Pairs and their counts: ")
    print(pairs_dict)
    # Determine the most frequent pair, if clash use lexicographical greater
    most_frequent_pair = max(pairs_dict, key=lambda x: (pairs_dict[x], x))

    # update the tokenized dict by merging the most frequent pair
    new_tokenized_dict = {}
    for token_tuple, token_count in tokenized_dict.items():
        merged_token = []
        i = 0
        while i < len(token_tuple):
            if i < len(token_tuple) - 1 and (token_tuple[i], token_tuple[i + 1]) == most_frequent_pair:
                merged_token.append(token_tuple[i] + token_tuple[i + 1])
                i += 2
            else:
                merged_token.append(token_tuple[i])
                i += 1

        merged_token = tuple(merged_token)
        if merged_token in new_tokenized_dict:
            new_tokenized_dict[merged_token] += token_count
        else:
            new_tokenized_dict[merged_token] = token_count

    return new_tokenized_dict, most_frequent_pair


# print(merge_pair(pre_tokenized_dict))
# print("######")
# perform 6 merges
tokenized_dict = pre_tokenized_dict
for i in range(6):
    print(f"Merge {i + 1}: ")
    tokenized_dict, most_frequent_pair = merge_pair(tokenized_dict)
    print("Tokenized dict after merge: ")
    print(tokenized_dict)
    print(f"Most frequent pair: {most_frequent_pair}")
    print("######")
