
"""
https://www.youtube.com/watch?v=I0Ttr25Nio4
背包问题
Solution 2
Very standard Knapsack problem.
Some black magic here:

1. I initial the impossible number with -1,
   so that the all imporssible negative value will be impossible.

2. We can always add the digit to tail.
   Because we already add the bigger digits first.


Constraint given in the problem: 1 <= cost[i] <= 5000. So cost of any i does not exceed 5000.
Remember: The cost of painting a digit (i+1) is given by cost[i].

He made the size of the dp list + 5000 more than target. Just to avoid : if c > t then skip c.
The dp[target+1]... dp[target + 5000] are garbage values and not needed for final answer. ----- (point 1)

(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost)) ----- when c > t, e.g., c = 1000, t(target) = 800. dp[-200] will be filled.
dp[-200] is the 200th element from the end which is useless coz of (point 1)

dp[i]: stores the answer ITSELF, i.e., the output.
dp[0] = 0 as cost[i]>=1. No digit (i+1) is part of the string number.

Suppose: dp[20] = 25 and there is a single (9, 15) - digit, cost pair.... i.e., (8+1, cost[8])

To calculate dp[40] = dp[40-15]10 + (9) for i, c in (9, 15)
dp[40] = 2510 + 9
dp[40] = 259 (This is same as '25' + '9')


  def largestNumber(self, cost, target):
    dp = [0] + [-1] * (target + 5000) # smart initialization
    --if c > t then skip c condition is not needed because of dp[t+5000]


    for t in xrange(1, target + 1):
        dp[t] = max(dp[t - c] * 10 + (i + 1) for i, c in enumerate(cost))
                                      # digit i+1    # go through all (i+1, cost[i])

    # just convert the number to string
    return str(max(dp[t], 0))

    # Why max() in return statement. See edge case: target = 20,   costs: [6, 3, 9]

    # The total cost used must be equal to target. But this is not possible by summing up elements in costs.
    # as we initialized dp[all numbers except 0] = -1. When it is -1, we know no subset with repetition in cost could give target.
    # So return 0, when dp is negative (as they want 0 if not possible)
"""


class Solution:
    def largestNumber(self, cost, target):
        dp = [0] + [-1] * (target + 5000)
        for i in range(1, target + 1):
            # dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
            for idx, num in enumerate(cost):
                dp[i] = max(dp[i], dp[i - num] * 10 + idx + 1)
        return str(max(dp[i], 0))


class Solution2:
    def largestNumber(self, cost, target):
        dp = [0] + [-1] * (target + 5000)
        for i in range(1, target + 1):
            # dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
            for idx, num in enumerate(cost):
                if i - num >= 0:
                    dp[i] = max(dp[i], dp[i - num] * 10 + idx + 1)
        return str(max(dp[i], 0))



