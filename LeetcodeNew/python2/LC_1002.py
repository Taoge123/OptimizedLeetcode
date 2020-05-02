import collections

class Solution:
    def commonChars(self, A):
        res = collections.Counter(A[0])
        for word in A[1:]:
            res &= collections.Counter(word)
        return list(res.elements())



