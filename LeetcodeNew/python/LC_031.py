"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


class Solution:
    def nextPermutation(self, nums):

        small, n = -1, len(nums)

        for i in range( n -1, 0, -1):
            if nums[ i -1] < nums[i]:
                small = i- 1
                break

        if small == -1:
            nums[:] = nums[::-1]
            return

        for i in range(n - 1, small - 1, -1):
            if nums[i] > nums[small]:
                nums[small], nums[i] = nums[i], nums[small]
                break

        nums[:] = nums[:small + 1] + nums[small + 1:][::-1]








