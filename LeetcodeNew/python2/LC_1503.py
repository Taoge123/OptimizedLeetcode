"""
Intuition
When two ants meet at some point,
they change their directions and continue moving again.
But you can assume they don't change direction and keep moving.

(You don't really know the difference of ants between one and the other, do you?)


Explanation
For ants in direction of left, the leaving time is left[i]
For ants in direction of right, the leaving time is n - right[i]


Complexity
Time O(N)
Space O(1)
"""


class Solution:
    def getLastMoment(self, n: int, left, right) -> int:

        res = 0
        for num in left:
            res = max(res, num)

        for num in right:
            res = max(res, n - num)

        return res



