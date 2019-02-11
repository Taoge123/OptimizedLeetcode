class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:  # backtracking
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 11)]):
            return []

        res = []
        self.sum_help(k, n, 1, [], res)
        return res

    def sum_help(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return

        if len(arr) > k or curr > 9:
            return

        for i in range(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res)
            arr.pop()


class Solution3:
    def combinationSum3(self, k, n):
        self.solution = []
        self.helper(1, k, n, [])
        return self.solution

    def helper(self, start, k, n, result):
        if k == 0 and n == 0:
            self.solution.append(result[:])
        for num in range(start, 10):
            result.append(num)
            if n - num >= 0:
                self.helper(num + 1, k - 1, n - num, result)
            result.pop()

"""
Some of the params don't need to be passed. 
path could give us more than one piece of information.
We keep track of the largest number in path and only consider numbers 
even larger to add to it.

"""


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, [], res)
        return res

    def dfs(self, k, n, path, res):
        if k < 0 or n < 0:
            return
        elif k == 0 and n == 0:
            res.append(path)
            return
        else:
            num = 1 if not path else path[-1] + 1
            for i in range(num, 10):
                self.dfs(k - 1, n - i, path + [i], res)


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        # global result
        gr = []

        # backtracking
        def bt(cr, x):
            """
            cr: current result
            x: next to try
            """
            if sum(cr) == n and len(cr) == k:
                gr.append(cr[:])
                return
            if sum(cr) >= n:
                return
            if len(cr) >= k:
                return
            for i in range(x, 10, 1):
                cr.append(i)
                bt(cr, i + 1)
                cr.pop()

        bt([], 1)

        return gr







