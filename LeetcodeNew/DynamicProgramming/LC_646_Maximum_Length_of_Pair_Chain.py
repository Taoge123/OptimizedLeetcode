
"""
https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/105647/Python-solution-with-detailed-explanation

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed.
You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
"""
import bisect

class Solution1:
    def findLongestChain(self, pairs):
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur = p[1]
                res += 1
        return res

class Solution2:
    def findLongestChain(self, pairs):

        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


class Solution3:
    def findLongestChain(self, pairs):
        tails = []
        for start, end in sorted(pairs):
            idx = bisect.bisect_left(tails, start)
            if idx == len(tails):
                tails.append(end)
            else:
                tails[idx] = min(tails[idx], end)
        return len(tails)

"""
Maximum Length of Pair Chain https://leetcode.com/problems/maximum-length-of-pair-chain/#/description

LIS variant using O(N^2) time and O(N) space

Simply sort the array and apply LIS algorithm over it.
"""
class Solution4:
    def findLongestChain(self, pairs):

        pairs.sort(key = lambda x:(x[0], x[1]))
        LIS = [1]*len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                LIS[i] = max(LIS[i], LIS[j]+1) if pairs[j][1] < pairs[i][0] else LIS[i]
        return LIS[-1]



"""
O(Nlg(N)) with O(N) space solution

Variant of the binary search solution for LIS problem. 
details: https://discuss.leetcode.com/topic/75189/python-solution-with-detailed-explanation
"""
class Solution:
    def findLongestChain(self, pairs):

        pairs.sort(key = lambda x:x[0])
        tails = []
        for p in pairs:
            idx = bisect.bisect_left(tails, p[1])
            if idx == len(tails):
                if len(tails) == 0 or (idx>=1 and p[0] > tails[idx-1]):
                    tails.append(p[1])
            else:
                tails[idx] = p[1]
        return len(tails)





