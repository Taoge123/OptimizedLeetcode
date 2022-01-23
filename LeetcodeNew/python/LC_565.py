
"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.



Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}


Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""


class SolutionTonyDP:
    def arrayNesting(self, nums):

        n = len(nums)
        self.memo = {}

        def dfs(i, visited, count):
            if i in self.memo:
                return self.memo[i]
            if i in visited:
                return count

            visited.add(i)
            res = dfs(nums[i], visited, count + 1)
            self.memo[i] = res
            return res

        res = 0
        for i in range(n):
            res = max(res, dfs(i, set(), 0))
        return res



class SolutionMemoWithoutCount:
    def arrayNesting(self, nums):

        n = len(nums)
        self.memo = {}

        def dfs(i, visited):
            if i in self.memo:
                return self.memo[i]
            if i in visited:
                return len(visited)

            visited.add(i)
            res = dfs(nums[i], visited)
            self.memo[i] = res
            return res

        res = 0
        for i in range(n):
            res = max(res, dfs(i, set()))
        return res



class Solution:
    def arrayNesting(self, nums) -> int:
        res = 0
        for i in range(len(nums)):
            nxt = i
            step = 0

            while nums[nxt] != -1:
                step += 1
                temp = nxt
                nxt = nums[nxt]
                nums[temp] = -1

            res = max(res, step)

        return res




