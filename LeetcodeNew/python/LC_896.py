
class Solution:
    def isMonotonic(self, A) -> bool:
        return not {(i >j) - (i <j) for i, j in zip(A, A[1:])} >= {1, -1}


class Solution2:
    def isMonotonic(self, A) -> bool:

        inc = dec = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                inc = False
            if A[i] < A[i + 1]:
                dec = False

        return inc or dec



A = [1,3,2]
a = Solution2()
print(a.isMonotonic(A))


