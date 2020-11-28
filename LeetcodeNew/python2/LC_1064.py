
class Solution:
    def fixedPoint(self, A) -> int:
        for i in range(len(A)):
            if i == A[i]:
                return i
        return -1

