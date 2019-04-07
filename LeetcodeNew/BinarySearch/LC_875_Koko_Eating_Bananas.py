
"""
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.
Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23


Note:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
"""

"""
Binary search between [1, 10^9] or [1, max(piles)] to find the result.
Time complexity: O(NlogM)

(p + m - 1) / m equal to ceil(p / m) (just personal behavior)

Here you find another similar problem.
774. Minimize Max Distance to Gas Station
"""
import math

class SolutionLee:
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) / 2
            if sum((p + m - 1) / m for p in piles) > H:
                l = m + 1
            else:
                r = m
        return l


class Solution1:
    def minEatingSpeed(self, piles, H):

        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            time = sum([math.ceil(i/m) for i in piles])
            if time > H:
                l = m + 1
            else:
                r = m
        return l


"""
Each hour, Koko chooses some pile of bananas, and eats K bananas from that pile.
There is a limited range of K's to enable her to eat all the bananas within H hours.
We ought to reduce the searching space and to return the minimum valid K.
Binary Search is born for that.
Initially, we know that K belongs to [1, the largest element in piles[]]. 
And we follow the pattern of lower-bound Binary Search except that 
if (K == target) is replaced with if (canEatAll(piles, K, H)).
"""


"""
分析：

1. 去找一个值满足某种条件，这种题见得太多了，显然是二分法，之后我整理一下所有的这种题目做一个合辑。
2. 那么这里怎么选定初始的lo和hi呢？我们要明确我们找的是吃的速度，那么最低，起码得在吃吧，
   所以起码lo = 1，那hi呢？我们注意到note中第二点pile.length <= H，因为我们吃的速度就算再快，
   一次也只能吃一盘而已，所以无论怎样最少都得pile.length个小时才能吃完，所以hi = max(piles)
思路：

对于某个确定的k值，我们如何计算吃完所有pile需要的时间呢，对于一盘，时间应该是piles[i]/k 向上取整，
然后求和判断是否大于H
若小于，则说明吃完还绰绰有余，还可以吃慢一点，从lo,mid中继续找
若大于，则说明吃得太慢了，则应该从mid,hi中继续找
"""

# O(NlogM) time，N = len(piles), M = max(piles)
class Solution2:
    def minEatingSpeed(self, piles, H):

        lo, hi = 1, max(piles)
        def canEat(k):
            time = 0
            for i in range(len(piles)):
                time += int(math.ceil(piles[i]//float(k)))
                if time > H: return False
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if canEat(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



class Solution3:
    def minEatingSpeed(self, piles, H):
        res, pilest = float('inf'), 0
        for i in piles:
            pilest+=i
        K = int(pilest/H)  # Optimization : K can not be lesser than this
        if K == 0: K = 1
        while res > H:
            res = 0
            for i in piles:
                res += math.ceil((i*1.0)/K)
            K+=1
        return K-1




