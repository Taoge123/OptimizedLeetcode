"""
Intuition
Need to sort by minimum - actual


Explanation
We have n investor,
each investor can invest actual energy,
and he think your company have minimum value.

If you already have at least minimum - actual energy,
the investory will invest you actual energy.

Assuming you get all investment,
how many energy you have at least in the end?

We sort by the energy required minimum - actual.
res is our current energy.
Each round we will get energy a and reach max(res + a, m).
Return directly res in the end.
"""


class Solution:
    def minimumEffort(self, tasks) -> int:
        tasks.sort(key=lambda a: a[1] - a[0])
        res = 0
        for actual, mini in tasks:
            res = max(res + actual, mini)
        return res



