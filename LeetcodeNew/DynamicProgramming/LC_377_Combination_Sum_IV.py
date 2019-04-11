
"""
建议和这一道题
leetcode 216. Combination Sum III DFS + 按照index递归遍历 、
leetcode 39. Combination Sum DFS深度优先搜索 和这道题
leetcode 40. Combination Sum II DFS深度优先搜索 当到一起学习。

同时还建议和
leetcode 322. Coin Change 类似背包问题 + 很简单的动态规划DP解决 和
leetcode 518. Coin Change 2 类似背包问题 + 很简单的动态规划DP解决 一起学习

还有leetcode 474. Ones and Zeroes若干0和1组成字符串最大数量+动态规划DP+背包问题

https://blog.csdn.net/JackZhang_123/article/details/78174174
https://blog.csdn.net/fuxuemingzhu/article/details/79343825
http://songhuiming.github.io/pages/2018/06/18/leetcode-377-combination-sum-iv/

Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""
import collections

class Solution1:
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]


"""
The problem with negative numbers is that now the combinations could be potentially of infinite length. 
Think about nums = [-1, 1] and target = 1. 
We can have all sequences of arbitrary length that follow the patterns -1, 1, -1, 1, ..., -1, 1, 1 
and 1, -1, 1, -1, ..., 1, -1, 1 (there are also others, of course, 
just to give an example). So we should limit the length of the combination sequence, 
so as to give a bound to the problem.

This is a recursive Python code that solves the above follow-up problem, 
so far it's passed all my test cases but comments are welcome."""

class Solution2:
    def combinationSum4WithLength(self, nums, target, length, memo=collections.defaultdict(int)):
        if length <= 0: return 0
        if length == 1: return 1 * (target in nums)
        if (target, length) not in memo:
            for num in nums:
                memo[target, length] += self.combinationSum4(nums, target - num, length - 1)
        return memo[target, length]


class Solution3:
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i:
                    break
                combs[i] += combs[i - num]
        return combs[target]

"""
DP Solution (Accepted, 60 ms):
"""
class Solution4:
    def combinationSum4(self, nums, target):
        nums.sort()
        dp=[0]*(target+1)
        dp[0]=1 # if num == target
        for i in range(1,target+1):
            for num in nums:
                if num>i:
                    break
                dp[i] += dp[i-num]
        return dp[target]

"""
DFS Solution (Time Limit Exceeded):
DFS solution can only handle small cases(i.e.target<=25 && len(nums)<=5), 
due to large list memory usage of combs."""

class Solution5:
    def combinationSum4(self, nums, target):
        nums.sort()
        path=[]
        combs=[]
        self.dfs(nums, target, path, combs)
        return len(combs)
    def dfs(self, nums, target, path, combs):
        if target==0:
            combs.append(path)
        for i in range(0,len(nums)):
            if nums[i]>target:
                break
            self.dfs(nums, target-nums[i], path+[nums[i]], combs)


"""
题目大意：
给定一个无重复的正整数数组，计算得到一个目标正整数的所有可能组合方式的个数。

测试用例见题目描述。

注意不同的序列顺序应当视为不同的组合。

进一步思考：

如果数组中允许包含负数时应当怎样处理？

这会使问题作出怎样的变动？

如果允许负数需要对问题新增怎样的限制条件？

解题思路：
动态规划（Dynamic Programming）

状态转移方程：dp[x + y] += dp[x]

其中dp[x]表示生成数字x的所有可能的组合方式的个数。
"""
class Solution6:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for x in range(target + 1):
            for y in nums:
                if x + y <= target:
                    dp[x + y] += dp[x]
        return dp[target]



"""
题目大意
给了一个只包含正整数且不重复的数组，有多少种和为target的方案。

解题方法
这个题用回溯法竟然超时了！怪不得需要返回个数而不是所有的答案。

我们需要一个一维数组dp，其中dp[i]表示目标数为i的解的个数，然后我们从1遍历到target，
对于每一个数i，遍历nums数组，如果i>=x, dp[i] += dp[i - x]。这个也很好理解，比如说对于[1,2,3] 4，这个例子，
当我们在计算dp[3]的时候，3可以拆分为1+x，而x即为dp[2]，3也可以拆分为2+x，此时x为dp[1]，
3同样可以拆为3+x，此时x为dp[0]，我们把所有的情况加起来就是组成3的所有情况了。

算dp[n]的时候遍历num[1] to num[n] index = i

如果i < dp[n] 那么dp[n] = dp[n] + dp[n-i]

从逻辑上来考虑比较复杂，比如4=0+4 1+3 2+2 3+1 4+0

0+4 1 （1+1+1+1）
1+3 1的组合3的组合
2+2 2的组合2的组合
3+1 3的组合*1的组合
4+0 1 （4）

1+4+4+4+1 然后除以2 因为重复了一遍
但是结果似乎不对

看答案 算法是

dp[n] = dp[n] + dp[n-i]
比如4
从1遍历到4
1<4
dp[4] = dp[4] + dp[4-1]
"""

