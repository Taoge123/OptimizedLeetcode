
"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""


class Solution:
    def maxEnvelopes(self, envelopes):
        nums = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        print(nums)
        nums = [y for x, y in nums]
        print(nums)
        return self.lis(nums)

    def lis(self, nums):
        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)



class SolutionTLE:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)
        dp = [1 for i in range(n)]
        envelopes.sort()

        for i in range(n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)






