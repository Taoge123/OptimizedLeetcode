
"""
https://blog.csdn.net/fuxuemingzhu/article/details/82902655
https://leetcode.com/problems/wiggle-subsequence/solution/

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
class Solution1:
    def wiggleMaxLength(self, nums):

        if not nums:return 0
        sol = 1
        flag = None
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==0:continue
            if nums[i+1]-nums[i]>0:
                if flag == None or flag == False:
                    sol += 1
                flag = True
            if nums[i+1]-nums[i]<0:
                if flag == None or flag == True:
                    sol += 1
                flag = False
        return sol


class Solution2:
    def wiggleMaxLength(self, nums):

        n = len(nums)
        if n < 2: return n
        if nums[1] > nums[0]:
            inc, dec = 1, 0
        elif nums[1] < nums[0]:
            inc, dec = 0, 1
        else:
            inc, dec = 0, 0

        for i in range(2, n):
            if nums[i] > nums[i - 1]:
                inc = dec + 1
            if nums[i] < nums[i - 1]:
                dec = inc + 1
        return max(inc, dec) + 1


class Solution3:
    def wiggleMaxLength(self, nums):

        if len(nums) < 2:
            return len(nums)
        # mimic a stack
        prev2, prev1 = None, nums[0]
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] == prev1:
                continue
            if prev2 == None or prev2 < prev1 > nums[i] or prev2 > prev1 < nums[i]:
                prev2, prev1 = prev1, nums[i]
                ans += 1
            else:
                prev1 = nums[i]
        return ans

"""
题目大意
如果一个数组里面，相邻的两个数字的差是正负交替的，那么认为这个是波动序列。求输入的数组里面最长的波动序列长度。

解题方法
明显的DP问题，本来的想法是用个二维DP，可是提交了几遍只通过了部分测试用例。才去看的别人的两个DP数组的解法。

定义了一个记录递增的DP数组inc，一个记录递减的DP数组dec，这两个DP数组分别保存的是开头元素是递增、递减的最长波动序列长度。
对于每个位置，从头遍历，如果当前的元素比前面的元素大，应该更新递增数组，否则，如果比前面的数字小，那么应该更新递减数组。

时间复杂度是O(N^2)，空间复杂度是O(N).
"""

class Solution11:
    def wiggleMaxLength(self, nums):

        n = len(nums)
        if n <= 1:
            return n
        inc, dec = [1] * n, [1] * n
        for x in range(n):
            for y in range(x):
                if nums[x] > nums[y]:
                    inc[x] = max(inc[x], dec[y] + 1)
                elif nums[x] < nums[y]:
                    dec[x] = max(dec[x], inc[y] + 1)
        return max(inc[-1], dec[-1])

"""
其实不需要从头遍历，只需要知道前面元素对应的最长递增和递减数组即可。

时间复杂度是O(N)，空间复杂度是O(N).
"""
class Solution22:
    def wiggleMaxLength(self, nums):

        n = len(nums)
        if n <= 1:
            return n
        inc, dec = [1] * n, [1] * n
        for x in range(1, n):
            if nums[x] > nums[x - 1]:
                inc[x] = dec[x - 1] + 1
                dec[x] = dec[x - 1]
            elif nums[x] < nums[x - 1]:
                inc[x] = inc[x - 1]
                dec[x] = inc[x - 1] + 1
            else:
                inc[x] = inc[x - 1]
                dec[x] = dec[x - 1]
        return max(inc[-1], dec[-1])


"""
简单分析代码就可以看出，每个元素都只和它之前的元素相关，因此，只需要使用两个变量即可。

时间复杂度是O(N)，空间复杂度是O(1).
"""
class Solution33:
    def wiggleMaxLength(self, nums):

        n = len(nums)
        if n <= 1:
            return n
        inc, dec = 1, 1
        for x in range(1, n):
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec)


"""
题目大意：
如果一个序列的相邻数字之差在正数和负数之间交替变换，则称此序列为一个“摆动序列”。
第一个差值（如果存在的话）正负均可。少于两个元素的序列也被认为是摆动序列。

例如，[1,7,4,9,2,5] 是一个摆动序列，因为差值(6,-3,5,-7,3)正负交替。
反例， [1,4,7,2,5] 以及 [1,7,4,5,5] 不是摆动序列，第一个是因为前两个差值连续为正，第二个是因为最后一个差值是0。

给定一个整数序列，返回其最长摆动子序列的长度。一个子序列可以通过从原始序列中删除一定数目的（也可以为0）元素得到。

测试用例见题目描述。

思考题：

你可以在O(n)的时间内求解吗？

解题思路：
解法I O(n) 遍历

一次遍历，将序列的连续递增部分和递减部分进行合并。
"""

class Solution111:
    def wiggleMaxLength(self, nums):

        size = len(nums)
        if size < 2: return size
        delta = nums[1] - nums[0]
        ans = 1 + (delta != 0)
        for x in range(2, size):
            newDelta = nums[x] - nums[x-1]
            if newDelta != 0 and newDelta * delta <= 0:
                ans += 1
                delta = newDelta
        return ans

"""
解法II O(n ^ 2) 动态规划

利用两个辅助数组inc, dec分别保存当前状态为递增/递减的子序列的最大长度
"""

class Solution222:
    def wiggleMaxLength(self, nums):

        size = len(nums)
        inc, dec = [1] * size, [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    inc[x] = max(inc[x], dec[y] + 1)
                elif nums[x] < nums[y]:
                    dec[x] = max(dec[x], inc[y] + 1)
        return max(inc[-1], dec[-1]) if size else 0


"""
解法III O(n) 动态规划

上述代码的时间复杂度可以优化成O(n)

参考https://leetcode.com/articles/wiggle-subsequence/
"""
class Solution333:
    def wiggleMaxLength(self, nums):

        size = len(nums)
        inc, dec = [1] * size, [1] * size
        for x in range(1, size):
            if nums[x] > nums[x - 1]:
                inc[x] = dec[x - 1] + 1
                dec[x] = dec[x - 1]
            elif nums[x] < nums[x - 1]:
                inc[x] = inc[x - 1]
                dec[x] = inc[x - 1] + 1
            else:
                inc[x] = inc[x - 1]
                dec[x] = dec[x - 1]
        return max(inc[-1], dec[-1]) if size else 0

# 观察可知，上述代码的空间复杂度还可以进一步优化成O(1)
class Solution444:
    def wiggleMaxLength(self, nums):

        size = len(nums)
        inc = dec = 1
        for x in range(1, size):
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec) if size else 0


