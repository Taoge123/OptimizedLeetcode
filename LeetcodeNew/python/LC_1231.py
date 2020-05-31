"""
https://www.youtube.com/watch?v=AtewfTorv0g
410. Split Array Largest Sum
1231. Divide Chocolate
774. Minimize Max Distance to Gas Station
875. Koko Eating Bananas
1011. Capacity To Ship Packages In N Days

"""


class Solution:
    def maximizeSweetness(self, A, K: int) -> int:
        left, right = 1, sum(A) // (K + 1)
        while left < right:
            mid = (right - left) // 2 + left + 1
            cur = cuts = 0
            for num in A:
                cur += num
                if cur >= mid:
                    cuts += 1
                    cur = 0
            if cuts > K:
                left = mid
            else:
                right = mid - 1
        return right





