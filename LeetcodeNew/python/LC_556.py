

"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


Example 2:

Input: 21
Output: -1
"""

"""
Next permunation
这道题让我们求下一个排列顺序，由题目中给的例子可以看出来，如果给定数组是降序，则说明是全排列的最后一种情况，
则下一个排列就是最初始情况，可以参见之前的博客 Permutations。我们再来看下面一个例子，有如下的一个数组
1　　2　　7　　4　　3　　1
下一个排列为：
1　　3　　1　　2　　4　　7
那么是如何得到的呢，我们通过观察原数组可以发现，
1. 如果从末尾往前看，数字逐渐变大，到了2时才减小的，
2. 然后我们再从后往前找第一个比2大的数字，是3，
3. 那么我们交换2和3，
4. 再把此时3后面的所有数字转置一下

1　　2　　7　　4　　3　　1
1　　2　　7　　4　　3　　1
1　　3　　7　　4　　2　　1
1　　3　　1　　2　　4　　7

"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:

        nums = list(str(n))
        length = len(nums)

        i, j = length - 2, length - 1
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i < 0:
            return -1

        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        res = int("".join(nums[:i + 1] + nums[i + 1:][::-1]))

        if res >= 2 ** 31 or res == n:
            return -1

        return res



