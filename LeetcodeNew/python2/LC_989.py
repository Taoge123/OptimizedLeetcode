
class Solution:
    def addToArrayForm(self, A, K):
        for i in range(len(A ) -1, -1, -1):
            A[i] += K
            K = A[i] // 10
            A[i] %= 10

        while K > 0:
            A.insert(0, K% 10)
            K //= 10

        return A



