"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line,
find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately,
and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.


Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2,
and if we use the radius 1 standard, then all the houses can be warmed.

"""
"""
The idea is to leverage decent Arrays.binarySearch() function provided by Java.

1. For each house, find its position between those heaters (thus we need the heaters array to be sorted).
2. Calculate the distances between this house and left heater and right heater, 
   get a MIN value of those two values. Corner cases are there is no left or right heater.
3. Get MAX value among distances in step 2. It's the answer.
Time complexity: max(O(nlogn), O(mlogn)) - m is the length of houses, n is the length of heaters.
"""
"""
Add two imaginary heaters at the infinite, then any house can be always between two heaters. 
Find the shortest distance of the two and compare it to the answer.
"""
import bisect

class Solution1:
    def findRadius(self, houses, heaters):

        houses.sort()
        heaters.sort()
        heaters=[float('-inf')]+heaters+[float('inf')] # add 2 fake heaters
        ans,i = 0,0
        for house in houses:
            while house > heaters[i+1]:  # search to put house between heaters
                i +=1
            dis = min (house - heaters[i], heaters[i+1]- house)
            ans = max(ans, dis)
        return ans


class Solution2:
    def findRadius(self, houses, heaters):
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect.bisect_left(heaters, h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r


class Solution3:
    def findRadius(self, houses, heaters):
        def bl(h):
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] < h:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        heaters.sort()
        r = 0
        for h in houses:
            ind = bl(h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r

"""
The idea is that for every house, you want to find the closest 2 heaters, 
and whichever in the 2 that is closer should warm this house. 
Iterate through the houses, use binary search to find the closest 2 heaters, update answer.
"""

class Solution4:
    def findRadius(self, houses, heaters):
        heaters.sort()

        ans = 0
        for h in houses:
            hi = bisect.bisect_left(heaters, h)
            left = heaters[hi - 1] if hi - 1 >= 0 else float('-inf')
            right = heaters[hi] if hi < len(heaters) else float('inf')
            ans = max(ans, min(h - left, right - h))

        return ans

"""
For each house find distance to closest heater. 
Take the max distance of these which is the radius needed.
"""

class Solution5:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        j,radius = 0,0
        for house in houses:
            while j+1 < len(heaters) and abs(heaters[j+1]-house) <= abs(heaters[j]-house):
                j += 1
            radius = max(radius,abs(heaters[j]-house))
        return radius


