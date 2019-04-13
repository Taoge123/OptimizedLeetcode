
"""
Given a set of distinct positive integers,
find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

"""
题目大意：
给定一个不重复正整数集合，寻找最大子集，使得子集中的任意一对元素 (Si, Sj) 均满足Si % Sj = 0或者Sj % Si = 0。

如果存在多种答案，返回其中之一即可。

测试用例如题目描述。

解题思路：
动态规划（Dynamic Programming）

状态转移方程：

dp[x] = max(dp[x], dp[y] + 1)  其中： 0 <= y < x 且 nums[x] % nums[y] == 0
返回结果利用辅助数组pre记录
"""
"""
这道题给了我们一个数组，让我们求这样一个子集合，集合中的任意两个数相互取余均为0，而且提示中说明了要使用DP来解。
那么我们考虑，较小数对较大数取余一定不为0，那么问题就变成了看较大数能不能整除这个较小数。
那么如果数组是无序的，处理起来就比较麻烦，所以我们首先可以先给数组排序，这样我们每次就只要看后面的数字能否整除前面的数字。
定义一个动态数组dp，其中dp[i]表示到数字nums[i]位置最大可整除的子集合的长度，还需要一个一维数组parent，
来保存上一个能整除的数字的位置，两个整型变量mx和mx_idx分别表示最大子集合的长度和起始数字的位置，
我们可以从后往前遍历数组，对于某个数字再遍历到末尾，在这个过程中，如果nums[j]能整除nums[i], 
且dp[i] < dp[j] + 1的话，更新dp[i]和parent[i]，如果dp[i]大于mx了，还要更新mx和mx_idx，
最后循环结束后，我们来填res数字，根据parent数组来找到每一个数字
"""

class Solution1:
    def largestDivisibleSubset(self, nums):

        nums = sorted(nums)
        size = len(nums)
        dp = [1] * size
        pre = [None] * size
        for x in range(size):
            for y in range(x):
                if nums[x] % nums[y] == 0 and dp[y] + 1 > dp[x]:
                    dp[x] = dp[y] + 1
                    pre[x] = y
        idx = dp.index(max(dp))
        ans = []
        while idx is not None:
            ans += nums[idx],
            idx = pre[idx]
        return ans



"""
解题方法
是否想起了Longest Increase Sequence？这两个题非常相似啊，所以做题一定要把融会贯通才行。

首先需要对题目给出的数组进行排序，这样的作用是我们从左到右遍历一次，每次只看后面的数字能不能被前面的整除就行。

问题分成了两个部分：

寻找最长的满足题目的数组
输出整个结果
使用一个一维DP，其含义是题目要求的数组，DP[i]的含义是，从0~i位置满足题目的最长数组。
先用i遍历每个数字，然后用j从后向前寻找能被nums[i]整除的数字，这样如果判断能整除的时候，
再判断dp[i] < dp[j] + 1，即对于以i索引结尾的最长的数组是否变长了。
在变长的情况下，需要更新dp[i]，同时使用parent[i]更新i的前面能整除的数字。另外还要统计对于整个数组最长的子数组长度。

知道了对于每个位置最长的子数组之后，我们也就知道了对于0~n区间内最长的满足题目条件的数组，最后需要再次遍历，
使用parent就能把正儿个数组统计输出出来。因为这个最大的索引mx_index是对n而言的，所以输出是逆序的。

总感觉语言是乏力的，明白LIS对这个题有好处。

注意

注意这个case：
[1,2,4,8,9,72]
到72的时候，往前找到9，可以整除，更新dp[5]为max(1, 2 + 1) = 3,
注意此时应该继续往前找，不能停，直到找到8,发现dp[3] + 1 = 5 > 3，于是更新dp[i]
注意就是不能停，找到一个能整除并不够，前面有可能有更大的啊~~
时间复杂度是O(N^2)，空间复杂度是O(N).

"""
class Solution2:
    def largestDivisibleSubset(self, nums):

        if not nums: return []
        N = len(nums)
        nums.sort()
        dp = [0] * N #LDS
        parent = [0] * N
        mx = 0
        mx_index = -1
        for i in range(N):
            for j in range(i - 1, -1 , -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        return res[::-1]


class Solution3:
    def largestDivisibleSubset(self, nums):

        if not nums: return []
        nums.sort()
        n = len(nums)
        dp, index = [1] * n, [-1] * n
        max_dp, max_index = 1, 0
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j

            if max_dp < dp[i]:
                max_dp, max_index = dp[i], i

        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = index[max_index]
        return ans



"""
My S[x] is the largest subset with x as the largest element, i.e., 
the subset of all divisors of x in the input. With S[-1] = emptyset as useful base case. 
Since divisibility is transitive, a multiple x of some divisor d is also a multiple of all elements in S[d], 
so it's not necessary to explicitly test divisibility of x by all elements in S[d]. 
Testing x % d suffices.

While storing entire subsets isn't super efficient, it's also not that bad. 
To extend a subset, the new element must be divisible by all elements in it, 
meaning it must be at least twice as large as the largest element in it. 
So with the 31-bit integers we have here, the largest possible set has size 31 
(containing all powers of 2).
"""



