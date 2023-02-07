"""
angles = [10,11,14,16,....,359]
[0,2*pi]
(dx, dy)


"""

import math


class Solution:
    def visiblePoints(self, points, angle: int, location) -> int:
        same = 0
        nums = []
        for x, y in points:
            dx = x - location[0]
            dy = y - location[1]
            if dx == 0 and dy == 0:
                same += 1
                continue
            nums.append(math.atan2(dx, dy))
        nums.sort()
        nums = nums + [num + 2.0 * math.pi for num in nums]
        # print(nums)
        angle = math.pi * angle / 180

        res = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > angle:
                left += 1
            res = max(res, right - left + 1)
        return res + same







