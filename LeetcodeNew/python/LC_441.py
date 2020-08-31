
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

441.Arranging-Coins
假设答案是k，那么n一定是介于等差数列求和公式sum(k)与sum(k+1)之间，即

(1+k)*k/2 <=n < (1+k+1)*(k+1)/2     （*）
化简

k(k+1) <= 2n <= (k+1)(k+2)
缩放

k^2 < 2n < (k+2)^2
所以有k的范围是

sqrt(2n)-2 < k < sqrt(2n)
可以见只有两个整数解: k = sqrt(2n)-1 或者 sqrt(2n)。我们只要检查一下这两个是否满足原始的(*)式即可。
"""

"""
(1+k) * (k) // 2 <= n < (1+k+1) * (k+1) // 2
    k(k+1) <= 2n < (k+1)*(k+2)
        k^2 <= 2n < (k+2) ^ 2
            sqrt(2n) - 2 < k < sqrt(2n)



"""

import math

class SolutionWisdom:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0

        for k in range(int(math.sqrt(2 * n)) - 3, int(math.sqrt(2 * n)) + 1):
            if k * (k + 1) <= 2 * n and 2 * n < (k + 1) * (k + 2):
                return k
        return -1



class Solution1:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n > 0:
            i += 1
            n -= i

        return i if n == 0 else i - 1



class Solution2:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (right - left) // 2 + left
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1

        return right







