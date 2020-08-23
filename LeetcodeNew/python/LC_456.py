
"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

从后往前遍历。我们假设当前的元素nums[i]是132 pattern中的"2"，那么什么元素最适合作为"3"呢？
其实就是"2"的prev greater element，也就是nums[i]左边第一个比它大的元素，假设是nums[j]。
为什么这样的j最合适呢？因为j越接近i的话，我们就能够在[0,j-1]的区间里找到一个越小的数作为132 pattern里的"1"，
即越容易收集齐这样的132 pattern。

具体的做法是，我们先预处理数组，算出每个元素k左边的最小值leftMin[k]。然后从后往前遍历，对于第i个元素，
找到它的prev greater element，它的index记做j，那么查看leftMin[j]的元素是否比num[i]还小。
如果符合要求，就可以返回true.


"""

class SolutionWisdom:
    def find132pattern(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return False
        leftMin = [0] * n
        leftMin[0] = float('inf')
        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])

        stack = []
        for i in range(n - 1, -1, -1):
            second = float('-inf')
            # 要在右边找个仅次于nums[i]的
            while stack and stack[-1] < nums[i]:
                second = stack.pop()
            if leftMin[i] < second:
                return True
            stack.append(nums[i])
        return False



class Solution:
    def find132pattern(self, nums):

        mid = float('-inf')
        stack = []

        for item in nums[::-1]:
            if item < mid:
                return True

            while stack and stack[-1] < item:
                mid = stack.pop()

            stack.append(item)

        return False



nums = [3, 6, 4, 2]
# nums = [1, 2, 3, 4]4
a = SolutionWisdom()
print(a.find132pattern(nums))



