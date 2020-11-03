import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]





