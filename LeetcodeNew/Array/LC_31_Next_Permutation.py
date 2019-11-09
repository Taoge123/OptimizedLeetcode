# class Solution:
#     def nextPermutation(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         length = len(nums)
#         firstSmall = -1
#
#         for i in range(length - 1, 0, -1):
#             if nums[i - 1] < nums[i]:
#                 firstSmall = i - 1
#                 break
#         print(firstSmall)
#         if firstSmall == -1:
#             nums[:] = nums[::-1]
#             return
#
#         for i in range(length - 1, firstSmall - 1, -1):
#             if nums[firstSmall] < nums[i]:
#                 nums[i], nums[firstSmall] = nums[firstSmall], nums[i]
#                 break
#         nums[:] = nums[:firstSmall + 1] + nums[firstSmall + 1:][::-1]
#
#         return nums
#

class Solution:
    def nextPermutation(self, nums):

        small, large = -1, -1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                small = i - 1
                break

        if small == -1:
            nums[:] = nums[::-1]
            return

        for i in range(n - 1, small, -1):
            if nums[i] > nums[small]:
                nums[i], nums[small] = nums[small], nums[i]
                break
        nums[:] = nums[:small+1] + nums[small+1:][::-1]
        return nums

nums = [1,3,2]
a = Solution()
print(a.nextPermutation(nums))















