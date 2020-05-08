
class Solution:
    def prefixesDivBy5(self, A):
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2 % 5

        return [num % 5 == 0 for num in A]


