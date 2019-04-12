
"""

https://leetcode.com/problems/house-robber/discuss/164056/Python-or-tm
https://leetcode.com/problems/house-robber/discuss/164056/Python-or-tm

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you
rom robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

"""
Based on the recursive formula:

f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
"""
class Solution1:

    def rob(self, nums):
        last, now = 0, 0

        for i in nums:
            last = now
            now = max(last + i, now)

        return now


"""
> 类型：DP基础题
> Time Complexity O(N)
> Space Complexity O(1)
"""
class Solution2:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])

        return res[-1]


"""
以上的代码需要O(N)空间，利用滚动数组可以实现O(1)空间, 滚动数组针对这一类的问题，当dependency只取决于k个数的时候，
一种方法是可以定义k个函数来作为迭代的数据存储，另一种方法就是开辟一个长度为k的数组，然后在迭代的时候，
更新对应的res[i%k]即可。我比较喜欢这种方法的原因是，这种方法对应上面的方式，需要更改的不多，
如果在面试时候仅仅想出了上面的代码，可以再不花多少时间的情况下，优化出O(1)的空间复杂度。
"""

class Solution3:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i % 2] = max(res[(i - 1) % 2], res[(i - 2) % 2] + nums[i])

        return max(res[0], res[1])


class SolutionCaikehe:
    # O(n) space
    def rob1(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[-1]

    def rob2(self, nums):
        if not nums:
            return 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[0] = nums[0]
            elif i == 1:
                res[1] = max(nums[0], nums[1])
            else:
                res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[-1]

    # Constant space
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = b
            b = max(nums[i] + a, b)
            a = tmp
        return b



"""
198 House Robber
> 类型：DP基础题
> Time Complexity O(N)
> Space Complexity O(1)
"""


class Solution11:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])

        return res[-1]


"""
以上的代码需要O(N)空间，利用滚动数组可以实现O(1)空间, 滚动数组针对这一类的问题，
当dependency只取决于k个数的时候，一种方法是可以定义k个函数来作为迭代的数据存储，
另一种方法就是开辟一个长度为k的数组，然后在迭代的时候，更新对应的res[i%k]即可。
我比较喜欢这种方法的原因是，这种方法对应上面的方式，需要更改的不多，如果在面试时候仅仅想出了上面的代码，
可以再不花多少时间的情况下，优化出O(1)的空间复杂度。
"""
class Solution22:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i % 2] = max(res[(i - 1) % 2], res[(i - 2) % 2] + nums[i])

        return max(res[0], res[1])



"""
O（1）的存储空间 这个确实是屌 不过为什么res[0], res[1] = nums[0], max(nums[0], nums[1])这里的res[1]要取最大值？

之前我们能够返回dp数组最后一位的原因是，我们创造了和input数组大小一样的dp数组，所以是一一对应的关系，最后一位自然就是最大的。
因为你并不知道数组是基数还是偶数。此题定义的滚动数组arr[0]存的是基数数组最大值，arr[1]存的是偶数数组最大值

举个例子：

第一种代码，如果input数组是偶数结尾，你返回arr[-1]。然后在滚动数组你也返回arr[-1]，没毛病
第一种代码，如果input数组是基数结尾，你返回arr[-1]。然后在滚动数组你也返回arr[-1]，这个时候其实最大值是arr[0]，因为最后的数改动的是基数位
"""



