"""
857. Minimum Cost to Hire K Workers

Intuition
Doesn't efficiency and speed are the same thing?
Like efficiency = speed = produce / time?
Speed sounds more like time actually.
You work slow, so you need more time.

@Msylcatam reminded me this problem 857. Minimum Cost to Hire K Workers
for your extra exercise as revision.

Hungry and out for meal.
For C++, may you refer to 857, exact the same template.

Special period, take care of yourself.
Wash your hand, touch the keyboard instead of your face.
Consider of putting a mask if necessary.
Very important, mute tv and twitter of terrible speech.


Solution 1: Binary Insert
We hire the team from the most efficent people to less.
The current iterated engineer has the smallest efficency in the team.
The performance of a team = efficency[i] * sumSpeed

Each time we have a new engineer,
though will reduce the efficency of the team,
it may increment the sum of speed.

If the size of team is bigger than k,
we have to layoff the smallest speed.
Then we update the result.

Note we should try better team work.
But there is the chance that less engineers
and achieve greater performance than k engineers.
If you have efficient = speed = 100,
other engineer have nothing,
you should be independent engineer and be your own boss.
(I didn't test if LeetCode include this case.)

We keep our engineers in order of their speed,
and we insert the new engineer inside the list as per its speed.


Complexity
Time O(N^2), since insert take O(N)
Space O(N)
"""

import heapq


class SolutionTony:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:

        mod = 10 ** 9 + 7
        res = 0
        totalSpeed = 0
        heap = []
        # we wanna pick the highest efficiency
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, s)
            totalSpeed += s

            if len(heap) > k:
                totalSpeed -= heapq.heappop(heap)

            res = max(res, totalSpeed * e)

        return res % mod




class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        heap = []
        res = summ = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, s)
            summ += s
            if len(heap) > k:
                summ -= heapq.heappop(heap)
            res = max(res, summ * e)
        return res % (10 ** 9 + 7)






