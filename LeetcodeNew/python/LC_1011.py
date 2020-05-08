"""

Explanation
Given the number of bags,
return the minimum capacity of each bag,
so that we can put items one by one into all bags.

We binary search the final result.
The left bound is max(A),
The right bound is sum(A).


More Good Binary Search Problems
Here are some similar binary search problems.
Also find more explanations.
Good luck and have fun.

Find the Smallest Divisor Given a Threshold
Divide Chocolate
Capacity To Ship Packages In N Days
Koko Eating Bananas
Minimize Max Distance to Gas Station
Split Array Largest Sum
"""


class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        left = max(weights)
        right = left * len(weights) // D
        while left < right:
            mid = (left + right) // 2
            count = 1
            summ = 0
            for w in weights:
                if summ + w > mid:
                    count += 1
                    summ = 0
                summ += w

            if count > D:
                left = mid + 1
            else:
                right = mid

        return left

