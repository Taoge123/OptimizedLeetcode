
"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.


Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""


"""
最朴素的思想。

题目给的不是有序的，一定要先排序，排序了之后，对houses进行遍历，找出大于house的最小的heater，
然后求出house据左右的heater的最小距离。然后求出整个的最大距离，即为所求。
这个题的思路是从把heater对house进行覆盖的思路转化成house距离左右heater的最小距离。结果是所有最小距离的最大距离。
"""

import bisect

class Solution:
    def findRadius(self, houses, heaters) -> int:

        houses = sorted(houses)
        heaters = sorted(heaters)

        i, res = 0, 0

        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i+1]-house) <= abs(heaters[i]-house):
                i += 1

            res = max(res, abs(heaters[i] - house))
        return res





class Solution2:
    def findRadius(self, houses, heaters) -> int:
        heaters = sorted(heaters)
        res = 0

        for house in houses:
            index = bisect.bisect_left(heaters, house)
            if index == len(heaters):
                res = max(res, house - heaters[-1])
            elif index == 0:
                res = max(res, heaters[0] - house)
            else:
                res = max(res, min(heaters[index] - house, house - heaters[index - 1]))

        return res







