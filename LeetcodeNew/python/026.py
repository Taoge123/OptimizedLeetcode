
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0

        j = 0
        for i in range(len(A)):
            if A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1

        return j + 1



