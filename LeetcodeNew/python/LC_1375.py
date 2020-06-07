"""
Explanation
right is the number of the right most lighted bulb.

Iterate the input light A,
update right = max(right, A[i]).

Now we have lighted up i + 1 bulbs,
if right == i + 1,
it means that all the previous bulbs (to the left) are turned on too.
Then we increment res


Complexity
Time O(N)
Space O(1)
"""


class Solution:
    def numTimesAllBlue(self, light):
        right = res = 0
        for i, num in enumerate(light, 1):
            right = max(right, num)
            res += right == i
        return res



class SolutionTony:
    def numTimesAllBlue(self, light) -> int:
        if not light:
            return 1

        res = 0
        preSum = [1]
        n = len(light)
        for i in range(2, n + 1):
            preSum.append(i + preSum[-1])

        newLight = [light[0]]
        for i in range(1, n):
            newLight.append(light[i] + newLight[-1])

        for i, j in zip(preSum, newLight):
            if i == j:
                res += 1
        return res


