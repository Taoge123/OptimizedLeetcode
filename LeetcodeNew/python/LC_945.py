"""
Solution 1: Just Sort, O(NlogN)
Sort the input array.
Compared with previous number,
the current number need to be at least prev + 1.

Time Complexity: O(NlogN) for sorting
Space: O(1) for in-space sort

Note that you can apply "O(N)" sort in sacrifice of space.
Here we don't talk further about sort complexity.

"""


class Solution1:
    def minIncrementForUnique(self, A) -> int:
        res = 0
        A.sort()

        for i in range(1, len(A)):
            pre = A[i - 1]
            cur = A[i]
            if pre >= cur:
                res += pre - cur + 1
                A[i] = pre + 1
        return res


class Solution:
    def minIncrementForUnique(self, A) -> int:
        res = 0
        need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res



