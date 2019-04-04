
"""
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

"""
from collections import Counter


class Solution1:
    def sortColors(self, nums):
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


"""
This is a dutch partitioning problem. We are classifying the array into four groups: 
red, white, unclassified, and blue. Initially we group all elements into unclassified. 
We iterate from the beginning as long as the white pointer is less than the blue pointer.

If the white pointer is red (nums[white] == 0), we swap with the red pointer 
and move both white and red pointer forward. If the pointer is white (nums[white] == 1), 
the element is already in correct place, so we don't have to swap, just move the white pointer forward. 
If the white pointer is blue, we swap with the latest unclassified element.
"""

class Solution2:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


class SolutionCaikehe:
    # count sort
    def sortColors1(self, nums):
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0 + c1] = [1] * c1
        nums[c0 + c1:] = [2] * c2

    # one pass
    def sortColors(self, nums):
        # zero and r record the position of "0" and "2" respectively
        l, r, zero = 0, len(nums) - 1, 0
        while l <= r:
            if nums[l] == 0:
                nums[l], nums[zero] = nums[zero], nums[l]
                l += 1;
                zero += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

class Solution4:
    def sortColors(self, nums):
        c = Counter(nums)
        for i in range(c[0]): nums[i] = 0
        for i in range(c[0], c[0] + c[1]): nums[i] = 1
        for i in range(c[0] + c[1] ,  c[0] + c[1] + c[2]): nums[i] = 2


"""
1 Pass
l 的左侧都是0，不含l 。 r 的右侧都是2, 不含 r
mid 代表着所有的1 (One)，在扫描的时候:
碰到0，交换到左边的l区间, 碰到2，交换到右边的r区间。扫描完后，中间部分就都是1 (One)

注意边界条件是mid <= r
"""


class Solution5:
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        mid = 0

        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                mid += 1;
                l += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1



