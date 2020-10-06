
"""
We use a dictionary to map words with their similar words and simply look up the dictionary when we compare pairs of words in words1 and words2 by checking if the second word is in the first word's similar word set.

For this pairs of words, the following dict is generated:

[["a", "b"], ["a", "c"], ["b", "d"]]

{
  "a": set(["b", "c"]),
  "b": set(["a", "d"]),
  "c": set(["a"]),
  "d": set(["b"]),
}

"""

import collections


class Solution1:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        table = collections.defaultdict(set)
        for word1, word2 in pairs:
            table[word1].add(word2)
            table[word2].add(word1)
        for word1, word2 in zip(words1, words2):
            if word1 != word2 and word2 not in table[word1]:
                return False
        return True



class Solution2:
    def areSentencesSimilar(self, words1, words2, pairs) -> bool:
        if len(words1) != len(words2):
            return False

        sets = set()
        for a, b in pairs:
            sets.add((a, b))

        for w, v in zip(words1, words2):
            if w != v and (w, v) not in sets and (v, w) not in sets:
                return False
        return True


