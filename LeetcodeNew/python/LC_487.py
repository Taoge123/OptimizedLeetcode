
"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream?
In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

"""


import collections
import functools


class SolutionMemo:
    def findMaxConsecutiveOnes(self, nums):

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, k, count):
            if i >= n:
                return count

            if nums[i] == 0 and k <= 0:
                return count

            if nums[i] == 0:
                use = dfs(i + 1, k - 1, count + 1)
                no_use = dfs(i + 1, k, 0)
            else:
                use = dfs(i + 1, k, count + 1)
                no_use = dfs(i + 1, k, count + 1)
            return max(use, no_use)

        return dfs(0, 1, 0)



class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        res = 0
        left = 0
        k = 1
        queue = collections.deque([])
        for i, num in enumerate(nums):
            if num == 0:
                queue.append(i)
            if len(queue) > k:
                left = queue.popleft() + 1
            res = max(res, i - left + 1)
        return res


"""
【1 0 0 1 1 1】
    
queue = [2]
res = 2


"""

"""
if nums[i] == 0:
    no[i] = 0
    use[i] = no[i-1] + 1

if nums[i] == 1:
    no[i] = no[i-1] + 1
    use[i] = use[i-1] + 1

487.Max Consecutive Ones II
类似于动态规划的思想，设计两个状态变量：
count1记录当前从未使用反转权力、可以得到的连续1的个数；count2记录当前已经使用反转权力、可以得到的连续1的个数。

如果nums[i]==1，那么count1和count2各自加1，没有问题。

如果nums[i]==0，那么count1要置零；count2怎么办呢？事实上count2=count1+1既可。

一路上追踪最大曾出现过的count2就是最后的答案。

"""


class SolutionDP:
    def findMaxConsecutiveOnes(self, nums) -> int:
        # no is no flip and use has one flip
        no = 0
        use = 0
        res = 0
        for num in nums:
            if num == 0:
                use = no + 1
                no = 0
            else:
                use += 1
                no += 1
            res = max(res, no, use)
        return res




class Solution2:
    def findMaxConsecutiveOnes(self, nums) -> int:

        res = 0
        left = 0
        queue = -1

        for i, num in enumerate(nums):
            if num == 0:
                left = queue + 1
                queue = i
            res = max(res, i - left + 1)
        return res













