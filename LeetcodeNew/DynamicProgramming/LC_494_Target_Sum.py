
"""
https://blog.csdn.net/fuxuemingzhu/article/details/80484450
http://fuxuemingzhu.cn/
https://github.com/WuLC/LeetCode/blob/master/Algorithm/Python/494.%20Target%20Sum.py

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

"""
Python solution, but it's really easy to understand.
To make it clear for everyone, find following the syntax for get() method of dictionary(hase map)

dict.get(key, default)
The method get() returns a value for the given key. If key is not available then returns default value.
"""
import collections

class SolutionLee:
    def findTargetSumWays(self, nums, S):
        count = {0: 1}
        for x in nums:
            count2 = {}
            for tmpSum in count:
                count2[tmpSum + x] = count2.get(tmpSum + x, 0) + count[tmpSum]
                count2[tmpSum - x] = count2.get(tmpSum - x, 0) + count[tmpSum]
            count = count2
        return count.get(S, 0)

class Solution11:
    def findTargetSumWays(self, nums, S):
        count = collections.defaultdict(int)
        count[0] = 1
        for x in nums:
            step = collections.defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step

        return count[S]



class Solution2:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)


"""
At first I just remember the current index and current target, and for each index, 
either subtract the nums[i] from S or add it to S. But this got TLE, 
then I came up with this solution. Just store the intermediate result with (index, s) and this got accepted.

"""


class Solution3:
    def findTargetSumWays(self, nums, S):

        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(i + 1, s - nums[i]) + findTarget(i + 1, s + nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]

        cache = {}
        return findTarget(0, S)


"""
题目大意：
给定一组非负整数a1, a2, ..., an，以及一个目标数S。给定两种符号+和-，对于每一个整数，选择一个运算符。

计算有多少种运算符的组合方式，可以使整数的和为目标数S。

注意：

给定数组长度为正数并且不会超过20。
元素之和不会超过1000。
输出答案确保在32位整数范围内。
解题思路：
动态规划（Dynamic Programming）

状态转移方程：dp[i + 1][k + nums[i] * sgn] += dp[i][k]

上式中，sgn取值±1，k为dp[i]中保存的所有状态；初始令dp[0][0] = 1

利用滚动数组，可以将空间复杂度优化到O(n)，n为可能的运算结果的个数
"""

class Solution4:
    def findTargetSumWays(self, nums, S):

        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            counter = collections.Counter()
            for sgn in (1, -1):
                for k in dp.keys():
                    counter[k + n * sgn] += dp[k]
            dp = counter
        return dp[S]


"""
刚开始用的dfs做的，遍历所有的结果，统计满足结果的个数就可以了。没错，超时了。超时的代码如下：
"""
class Solution111:
    def findTargetSumWays(self, nums, S):

        def helper(index, acc):
            if index == len(nums):
                if acc == S:
                    return 1
                else:
                    return 0
            return helper(index + 1, acc + nums[index]) + helper(index + 1, acc - nums[index])
        return helper(0, 0)


"""
其实一般能用dfs解决的题目，如果题目只要求满足条件的数字而不是所有的结果，那么dfs会超时。
解决方法其实基本只有一条路：动态规划。

我们定义了一个二维数组，这个二维数组dp[i][j]的意义是我们从最开始的位置到第i个位置上能够成和为j的组合有多少种，
因为求和之后数的范围不确定，所以数组中保存的是字典，字典保存的是到i位置能求得的和为某个数的个数。

所以从左到右进行遍历，在每个位置都把前一个位置的字典拿出来，看前一个位置的所有能求得的和。
和当前的数值分别进行加减操作，就能得出新一个位置能求得的和了。
"""

"""
状态转移方程是：

dp[0][0] = 1;
dp[i + 1][x + nums[i]] += dp[i][x];
dp[i + 1][x - nums[i]] += dp[i][x];
注意：其中x是在前一个位置能够成的和。

要注意一点是，dp初始不能采用下面方式：

dp = [collections.defaultdict(int)] * (_len + 1) 

这种初始化方式会使每个位置的元素其实是同一个字典。

"""
class Solution222:
    def findTargetSumWays(self, nums, S):

        _len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(_len + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[_len][S]


"""
分析：

这道题可以单纯的用暴力法解决，也就是对每个元素分别进行一次正负的累加，复杂度为2^n，因为n不超过20，故也就100w左右，但是在leetcode上同样的解法c++和java可以通过，python是无法通过的
这里介绍discuss里一位大神提出来的超帅的数学解法，这道题中我们加正负号无非是将nums分为两个子集p,n，p中元素全部加正号，n中元素全部加负号，使得sum(p) - sum(n) = S，而本身又有sum(p) + sum(n) = sum(nums)，故两式相加化简得sum(p) = (sum(nums)+S) / 2
那么这个式子直接给出了一个信息，也就是如果能找到p，则必有sum(nums)+S % 2 == 0这个条件，这个条件可以帮我们快速判断是否有解。
那么此时题目就变成给定一个数组nums，求有多少组不同的p，使得sum(p) = target，直接dp可解
思路：

建立dp，dp[i] = j代表数组nums中有j组子集的和为i，初始dp[0] = 1
如nums = [1,1,1,1,1]，按照如下步骤分析
对nums[0]分析，则得dp[1] = 1(因为dp[0] = 1)
对nums[1]分析，则得dp[1] = 2,dp[2] = 1(因为dp[0] = 1,dp[1] = 1)
对nums[2]分析，则得dp[1] = 3,dp[2] = 2,d[3] = 1,依次类推
"""
class Solution6:
    def findTargetSumWays(self, nums, S):

        if sum(nums) < S: return 0
        if (sum(nums) + S) & 1: return 0

        target = (sum(nums) + S) / 2
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(len(nums)):
            for val in range(target, nums[i]-1, -1):
                if dp[val-nums[i]]:
                    dp[val] += dp[val-nums[i]]
        return dp[-1]


