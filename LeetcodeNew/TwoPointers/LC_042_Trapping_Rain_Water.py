
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

"""
For index i, the water volume of i: vol_i = min(left_max_i, right_max_i) - bar_i.

The left_max array from left to right is always non-descending, the right_max is non-ascending.

Having such observation, we can say:

Given i < j, if left_max_i <= right_max_j: vol_i = left_max_i - bar_i, otherwise, vol_j = right_max_j - bar_j
because, if left_max_i <= right_max_j: left_max_i <= right_max_j <= right_max_j-1 <= ... <= right_max_i, 
then min(left_max_i, right_max_i) is always left_max_i
"""

class Solution1:
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume

"""
The water we trapped depends on the left side and right side which has the max height,

We keep the left side and right side until we find a higher side
"""
class Solution2:

    def trap(self, arr):
        height, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(arr)):
            right = max(right, i)
            water += min(height[n], right) - i
        return water

class Solution3:

    def trap(self, arr):
        left = right = water = 0
        i, j = 0, len(arr)-1
        while i <= j:
            left, right = max(left, arr[i]), max(right, arr[j])
            while i <= j and arr[i] <= left <= right:
                water += left - arr[i]
                i += 1
            while i <= j and arr[j] <= right <= left:
                water += right - arr[j]
                j -= 1
        return water

class Solution4:
    def trap(self, height):

        i,j = 0,len(height)-1
        left_max = right_max = 0
        ans = 0
        while i<j:
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
            if left_max <= right_max:
                ans += (left_max-height[i])
                i += 1
            else:
                ans += (right_max-height[j])
                j -= 1
        return ans

