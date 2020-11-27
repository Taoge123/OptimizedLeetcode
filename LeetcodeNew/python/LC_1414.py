"""
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585632/JavaC%2B%2BPython-Easy-Prove

"""


from sortedcontainers import SortedList

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k

        tree = SortedList()
        a, b = 0, 1
        while b < k:
            a, b = b, a + b
            tree.add(b)

        res = 0
        while k > 0:
            idx = tree.bisect_right(k)
            fib = tree[idx-1]
            print(tree, k, fib)
            k -= fib
            res += 1

        return res





class SolutionLee:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b

        return self.findMinFibonacciNumbers(k - a) + 1


k = 10
a = Solution()
print(a.findMinFibonacciNumbers(k))

