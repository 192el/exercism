"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    vocab = [vocab_words[0]]
    for x in range(len(vocab_words) - 1):
        vocab.append(vocab_words[0] + vocab_words[x + 1])
    return ' :: '.join(item for item in vocab)



def remove_suffix_ness(word):
    return word[:-5] + 'y' if word.endswith('iness') else word[:-4]



def adjective_to_verb(sentence, index):
    verb = ''.join(sentence.split()[index])
    return verb[:-1] + 'en' if verb.endswith('.') else verb + 'en'
