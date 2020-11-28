"""
https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode/
"""
import bisect
bisect.bisect
class SolutionTLE:
    def longestDupSubstring(self, S):
        left, right = 0, len(S)
        res = ''

        while left < right:
            mid = (left + right) // 2
            temp = self.check(mid, S)
            if not temp:
                right = mid
            else:
                left = mid + 1
                res = temp
        return res

    def check(self, num, S):
        visited = set()
        for i in range(len(S) - num + 1):
            if S[i:i + num] in visited:
                return S[i: i + num]
            visited.add(S[i: i + num])
        return None


"""
Intuition
Suffix array is typical solution for this problem.
The fastest way is to copy a template form the Internet.
The code will be quite long.
Here I want to share a binary search solution.


Explanation
Binary search the length of longest duplicate substring and call the help function test(L).
test(L) slide a window of length L,
rolling hash the string in this window,
record the seen string in a hashset,
and try to find duplicated string.

I give it a big mod for rolling hash and it should be enough for this problem.
Actually there could be hash collision.
One solution is to have two different mod for hash.
Or we can use a hashmap to record the index of string.


Complexity
Binary Search in range 1 and N, so it's O(logN)
Rolling hash O(N)
Overall O(NlogN)
SpaceO(N)
"""


class Solution:
    def longestDupSubstring(self, S):
        nums = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            pos = self.check(mid, nums, S, mod, res)
            if pos:
                lo = mid
                res = pos
            else:
                hi = mid - 1
        return S[res:res + lo]

    def check(self, mid, nums, S, mod, res):
        p = pow(26, mid) % mod
        cur = 0
        for i in range(len(nums[:mid])):
            cur = (cur * 26 + nums[i]) % mod

        visited = {cur}
        for i in range(mid, len(S)):
            cur = (cur * 26 + nums[i] - nums[i - mid] * p) % mod
            if cur in visited:
                return i - mid + 1
            visited.add(cur)






