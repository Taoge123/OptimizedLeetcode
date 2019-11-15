
from itertools import permutations

class Solution:
    def getPermutation(self, n, k):

        permutation = permutations(range(1, n+1))
        while k>0:
            res = next(permutation)
            k -= 1
        return ''.join([str(i) for i in res])



