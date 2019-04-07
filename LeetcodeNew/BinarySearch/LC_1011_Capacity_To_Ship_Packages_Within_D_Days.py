
"""

Basically we split the array into D subarray

Similar as
875. Koko Eating Bananas
774. Minimize Max Distance to Gas Station
410. Split Array Largest Sum.


A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation:
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Note:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
"""

"""
Given the number of bags,
return the minimum capacity of each bag,
so that we can put items one by one into all bags.

Similar as
875. Koko Eating Bananas
774. Minimize Max Distance to Gas Station

"""
class Solution1:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) // 2, 1, 0

            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w

            if need > D:
                left = mid + 1
            else:
                right = mid
        return left

"""
The intuition for this problem, stems from the fact that

a) Without considering the limiting limiting days D, 
   if we are to solve, the answer is simply max(a)
b) If max(a) is the answer, we can still spend O(n) time 
   and greedily find out how many partitions it will result in.

[1,2,3,4,5,6,7,8,9,10], D = 5

For this example, assuming the answer is max(a) = 10, disregarding D,
we can get the following number of days:
[1,2,3,4] [5] [6] [7] [8] [9] [10]

So by minimizing the cacpacity shipped on a day, we end up with 7 days, 
by greedily chosing the packages for a day limited by 10.

To get to exactly D days and minimize the max sum of any partition, 
we do binary search in the sum space which is bounded by [max(a), sum(a)]

Binary Search Update:
One thing to note in Binary Search for this problem, is even if we end up finding a weight, 
that gets us to D partitions, we still want to continue the space on the minimum side, 
because, there could be a better minimum sum that still passes <= D paritions.

In the code, this is achieved by:

if res <= d:
     hi = mid
With this check in place, when we narrow down on one element, lo == hi, 
we will end up with exactly the minimum sum that leads to <= D partitions.
"""

class Solution2:
    def shipWithinDays(self, a, d):
        lo, hi = max(a), sum(a)
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in a:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                else:
                    tot += wt
            if res <= d:
                hi = mid
            else:
                lo = mid + 1
        return lo

"""
解题方法
非常类似875. Koko Eating Bananas这题，使用的方法是二分查找。

怎么分析出来的呢？还是看Note，为什么出了50000这个数字？如果是只和数组长度有关的算法，
应该把这个数字设的更大才对。但是如果把50000和500放在一起看大概就明白了，
应该是通过重量去遍历数组长度，那么500 × 50000 = 2500 0000的时间复杂度还是有点高。
所以我们最终使用的是对重量进行二分，所以log(500) * 50000就能通过了。

对于要进行查找的重量，我们都去计算这个重量情况下，是不是能够在D天之内把所有的货物都拉出去。
然后进行简单的二分就可以了。和猴子吃香蕉的题目如出一辙。
"""

class Solution3:
    def shipWithinDays(self, weights, D):

        l = max(weights)
        r = sum(weights)
        # [l, r)
        while l < r:
            mid = l + (r - l) / 2
            need = 1
            cur = 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                l = mid + 1
            else:
                r = mid
        return l



weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
a = Solution1()
print(a.shipWithinDays(weights, D))



