import collections

class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K-1)

    def atMostK(self, A, K):
        count = collections.defaultdict(int)
        start = 0
        res = 0
        for j in range(len(A)):
            count[A[j]] += 1
            while len(count) > K:
                count[A[start]] -= 1
                if count[A[start]] == 0:
                    del count[A[start]]
                start += 1
            res += j - start + 1
        return res
