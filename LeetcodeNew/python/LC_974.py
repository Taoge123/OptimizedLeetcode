import collections


class Solution:
    def subarraysDivByK(self, A, K):
        table = collections.defaultdict(int)
        table[0] = 1
        res = 0
        summ = 0

        for num in A:
            summ = (summ + num) % K
            res += table[summ]
            table[summ] += 1

        return res




