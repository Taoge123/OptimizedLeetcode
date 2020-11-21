import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        return sorted(set(word1)) == sorted(set(word2)) and sorted(count1.values()) == sorted(count2.values())




