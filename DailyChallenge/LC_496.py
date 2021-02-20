"""
4 1 2
1 3 4 2

"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        table = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                table[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(table.get(num, -1))
        return res

