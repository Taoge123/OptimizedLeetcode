"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""



class Solution:
    def findKthNumber(self, n, k):
        k -= 1
        res = 1
        while k > 0:
            step = 0
            first, last = res, res + 1
            while first <= n:
                step += min(n + 1, last) - first
                first *= 10
                last *= 10
            if step <= k:
                res += 1
                k -= step
            else:
                res *= 10
                k -= 1
        return res



n = 130
k = 9

a = Solution()
print(a.findKthNumber(n, k))

