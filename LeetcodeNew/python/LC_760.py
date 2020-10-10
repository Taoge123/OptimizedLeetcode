
import collections

class Solution:
    def anagramMappings(self, A, B):
        table = collections.defaultdict(int)
        for i in range(len(B)):
            table[B[i]] = i

        res = [0] * len(A)
        index = 0
        for num in A:
            res[index] = table[num]
            index += 1
        return res



