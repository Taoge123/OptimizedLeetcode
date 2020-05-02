"""
Intuition:
There is only one way to filp A[0],
and A[0] will tell us if we need to filp the range A[0] ~ A[K -1].
So we start from the leftmost one by one using a greedy idea to solve this problem.


Solution 1
Explanation
Create a new array isFlipped[n].
isFlipped[i] = 1 iff we flip K consecutive bits starting at A[i].

We maintain a variable flipped and flipped = 1 iff the current bit is flipped.

If flipped = 0 and A[i] = 0, we need to flip at A[i].
If flipped = 1 and A[i] = 1, we need to flip at A[i].

Complexity
O(N) time for one pass
O(N) extra space for isFlipped[n].
"""



class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        res = 0
        flip = 0
        flipped = [0] * len(A)
        for i in range(len(A)):
            if i >= K:
                flip ^= flipped[i - K]

            if A[i] ^ flip == 0:
                if i + K > len(A):
                    return -1
                res += 1
                flip ^= 1
                flipped[i] = 1

        return res


class SolutionTLE1:
    def minKBitFlips(self, A, K: int) -> int:
        res = 0
        for i in range(len(A) - K + 1):
            if A[i] == 1:
                continue
            res += 1

            for j in range(K):
                A[i + j] ^= 1

        for i in range(len(A) - K + 1, len(A)):
            if A[i] == 0:
                return -1

        return res




class SolutionTLE:
    def minKBitFlips(self, A, K: int) -> int:

        if K > len(A):
            for i in range(A):
                if A[i] == 0:
                    return -1
            return 0

        res = 0
        for i in range(len(A) - K + 1):
            if A[i] == 0:
                self.flip(A, K, i)
                res += 1

        for j in range(len(A) - K, len(A)):
            if A[j] == 0:
                return -1

        return res

    def flip(self, A, K, pos):
        for i in range(pos, pos + K):
            A[i] = A[i] ^ 1







