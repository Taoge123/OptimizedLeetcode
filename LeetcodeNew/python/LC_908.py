
class Solution:
    def smallestRangeI(self, A, K: int) -> int:
        A = sorted(A)
        if A[0] + K < A[-1] - K:
            return (A[-1] - K) - (A[0] + K)
        else:
            return 0



class Solution2:
    def smallestRangeI(self, A, K: int) -> int:
        mini, maxi = min(A), max(A)
        if mini + K < maxi - K:
            return (maxi - K) - (mini + K)
        else:
            return 0



