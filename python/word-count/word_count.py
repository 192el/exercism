import re
from collections import Counter
def count_words(sentence):
    return Counter(re.findall(r"[^\W_]+(?:'[^\W_]+)?", sentence.lower()))
