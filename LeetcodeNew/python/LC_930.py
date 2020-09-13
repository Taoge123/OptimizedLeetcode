

"""

X X X X [i X X j] X X X
sum[i:j] -> prefix[j] - prefix[i-1] = S
prefix[i-1] = prefix[j] - S
"""

import collections

class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        table = collections.defaultdict(int)
        table[0] = 1
        summ = 0
        res = 0

        for i in range(len(A)):
            summ += A[i]
            if (summ - S) in table:
                res += table[summ - S]
            table[summ] += 1
        return res



