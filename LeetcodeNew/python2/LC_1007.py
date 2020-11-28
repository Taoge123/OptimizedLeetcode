"""
Count the frequency of each number in A and B, respectively;
Count the frequency of A[i] if A[i] == B[i];
If countA[i] + countB[i] - same[i] == A.length, we find a solution; otherwise, return -1;
min(countA[i], countB[i]) - same[i] is the answer.
"""

import collections

class Solution:
    def minDominoRotations(self, A, B) -> int:

        if len(A) != len(B):
            return -1
        same = collections.Counter()
        countA = collections.Counter(A)
        countB = collections.Counter(B)

        for a, b in zip(A, B):
            if a == b:
                same[a] += 1
        # countA[i] + countB[i] - same[i] is like finding the union of two set A and set B <=> A + B - (A & B)
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                return min(countA[i], countB[i]) - same[i]

        return -1









