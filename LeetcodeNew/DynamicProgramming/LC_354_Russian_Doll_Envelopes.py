
"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

"""
Sort the array. Ascend on width and descend on height if width are same.
Find the longest increasing subsequence based on height.
Since the width is increasing, we only need to consider height.
[3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] 
when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
"""
import bisect
class Solution1:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        max_idx = 0
        heights = [envelopes[0][1]] + [0] * (len(envelopes) - 1)
        for e in envelopes:
            idx = bisect.bisect_left(heights, e[1], hi=max_idx + 1)
            heights[idx] = e[1]
            max_idx = max(max_idx, idx)
        return max_idx + 1


class Solution(object):
    def maxEnvelopes(self, envelopes):

        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        h=[]
        for i,e in enumerate(envelopes,0):
            j=bisect.bisect_left(h,e[1])
            if j<len(h):
                h[j]=e[1]
            else:
                h.append(e[1])
        return len(h)

'''It's a problem based on LIS.
DP solution for LIS is N^2 which will TLE here.
Using Binary Search approach will get accepted.

https://leetcode.com/problems/longest-increasing-subsequence/
'''
class Solution3:
    def maxEnvelopes(self, envelopes):

        if not envelopes:
            return 0

        l = len(envelopes)
        if l == 1:
            return 1

        envelopes.sort(
            cmp=lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        # sort the envelopes by width because they need to be inorder before consider the heigths or versa

        width = []
        for i in envelopes:
            width.append(i[1])

        res = self.longestSubsequence(width)
        # the problem became LIS after sort(width)

        return res

    def longestSubsequence(self, nums):

        if not nums:
            return 0
        l = len(nums)
        res = []

        for num in nums:
            pos = self.binarySearch(num, res)
            if pos >= len(res):
                res.append(num)
            else:
                res[pos] = num

        return len(res)

    def binarySearch(self, target, nums):

        if not nums:
            return 0

        l = len(nums)
        start = 0
        end = l - 1

        while start <= end:
            half = start + (end - start) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target:
                start = half + 1
            else:
                end = half - 1

        return start



# Using the idea for LIS. Sort the envelops using (w, -h).
class Solution4:
    def maxEnvelopes(self, envelopes):

        envelopes.sort(key=lambda key:(key[0], -key[1]))
        tails = []
        for i in range(0, len(envelopes)):
            idx = bisect.bisect_right(tails, envelopes[i][1])
            if idx - 1 >= 0 and tails[idx - 1] == envelopes[i][1]:
                continue
            if idx == len(tails):
                tails.append(envelopes[i][1])
            else:
                tails[idx] = envelopes[i][1]
        return len(tails)


"""
The solution of the problem is similar to the solution of 300. Longest Increasing Subsequence
. The only difference is to sort the list before DP to find the longest increasing subsequence.
"""
class Solution5:
    def maxEnvelopes(self, envelopes):
        if not envelopes:   return 0

        envelopes.sort()
        N = len(envelopes)
        dp = [1 for _ in range(N)]
        ans = 1
        for i in range(N):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans

