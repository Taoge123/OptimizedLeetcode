
"""
https://leetcode.com/problems/delete-and-earn/discuss/1173247/Python-DP-Similar-to-House-Robber
https://leetcode.com/problems/delete-and-earn/discuss/1491241/Simplest-dp(recusion-%2B-memoization)-solution
https://leetcode.com/problems/delete-and-earn/discuss/1056337/clean-memo
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/740.Delete-and-Earn

p : the max profit if we rob this
q : the max profit if we don't rob this

动态规划问题，对于nums中出现的最大的数n来说，有两种可能：

能挣到点数，那么最大的分数就是n×n出现的次数+最大值为n-2时的分数
不能挣到点数，那么最大值就是最大值为n-1的分数
因为nums的元素取值范围为[1,10000]所以可以用哈希表来保存每个数字出现了多少次。


解法1：
本题有一个特点，如果我们选择了数值k，那么所有值为k的元素都会被计入gain而不能再被访问。
这就提示了我们其实不应该按照元素的index顺序遍历（否则可能会遇到很多次已经被处理过的数值），
更方便的做法是应该按照元素的value顺序（比如说从小到大）来遍历。

假设我们处理完当前数值k，记目前位置的最大收益是dp[k]。注意这个dp[k]不能保证k被earn与否。
可能k这个数被delete and earn了，那么意味着实际的收益应该是dp[k-2]+k;也有可能这个k并没有被delete and earn,
那么它的收益完全就取决于dp[k-1]。最终我们会在这两个决策中挑更大的作为dp[k]。

于是动态转移方程就是

dp[k] = max(dp[k-2]+gain[k], dp[k-1])
其中gain[k]表示对k这个数值进行delete and earn的收益，其中包括了数组中出现重复的k的情况。如果数组中没有k，
那么显然gain[k]=0.

应为我们是按照数值的从小到大顺序遍历的，所以最终答案应该是dp[数组最大的value]。


"""

import collections
import functools


class SolutionMemo:
    def deleteAndEarn(self, nums):
        arr = [0] * (max(nums) + 1)
        for num in nums:
            arr[num] += num

        @functools.lru_cache(None)
        def dfs(i):
            if i >= len(arr):
                return 0
            return max(dfs(i + 2) + arr[i], dfs(i + 1))

        return dfs(0)


class Solution:
    def deleteAndEarn(self, nums) -> int:

        arr = [0] * (max(nums) + 1)
        for num in nums:
            arr[num] += num

        memo = {}
        return self.dfs(arr, 0, memo)

    def dfs(self, arr, i, memo):
        if i in memo:
            return memo[i]

        if i >= len(arr):
            return 0

        memo[i] = max(self.dfs(arr, i + 2, memo) + arr[i], self.dfs(arr, i + 1, memo))
        return memo[i]



class Solution:
    def deleteAndEarn(self, nums):
        count = collections.Counter()
        dp = [0] * 10001
        for num in nums:
            count[num] += num
        for i in range(1, len(dp)):
            if i == 1:
                dp[i] = count[i]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + count[i])
        return max(dp)



class Solution2:
    def deleteAndEarn(self, nums):
        points = [0] * 1001
        for num in nums:
            points[num] += num
        prev, curr = 0, 0
        for point in points:
            prev, curr = curr, max(point + prev, curr)
        return curr


class Solution22:
    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num
        preTake, preSkip = 0, 0
        for i in range(10001):
            take = preSkip + points[i]
            skip = max(preSkip, preTake)
            preTake = take
            preSkip = skip
        return max(preSkip, preTake)


class Solution222:
    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num

        dp = [0] * 10001
        dp[1] = 1
        for i in range(1, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        return dp[-1]


