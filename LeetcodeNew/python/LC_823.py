
import collections

class Solution:
    def numFactoredBinaryTrees(self, A) -> int:

        A.sort()
        table = collections.defaultdict(int)
        count = 1
        table[A[0]] = count

        for i in range(1, len(A)):
            count = 1
            for num in table.keys():
                if A[i] % num == 0 and A[i] // num in table:
                    count += table[num] * table[A[i] // num]
            table[A[i]] = count

        res = 0
        for num in table.keys():
            res += table[num]
            res %= (10**9 + 7)
        return res



