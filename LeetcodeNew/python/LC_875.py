"""
分析：

去找一个值满足某种条件，这种题见得太多了，显然是二分法，之后我整理一下所有的这种题目做一个合辑。
那么这里怎么选定初始的lo和hi呢？我们要明确我们找的是吃的速度，那么最低，起码得在吃吧，所以起码lo = 1，
那hi呢？我们注意到note中第二点pile.length <= H，因为我们吃的速度就算再快，一次也只能吃一盘而已，
所以无论怎样最少都得pile.length个小时才能吃完，所以hi = max(piles)
思路：

对于某个确定的k值，我们如何计算吃完所有pile需要的时间呢，对于一盘，时间应该是piles[i]/k 向上取整，然后求和判断是否大于H
若小于，则说明吃完还绰绰有余，还可以吃慢一点，从lo,mid中继续找
若大于，则说明吃得太慢了，则应该从mid,hi中继续找
"""

import math


class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if sum((p + mid - 1) // mid for p in piles) > H:
                left = mid + 1
            else:
                right = mid

        return left





class Solution2:
    def minEatingSpeed(self, piles, H: int) -> int:

        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            time = sum([math.ceil(i / mid) for i in piles])
            if time > H:
                left = mid + 1
            else:
                right = mid
        return left



