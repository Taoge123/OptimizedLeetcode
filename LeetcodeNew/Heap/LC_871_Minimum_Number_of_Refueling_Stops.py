
"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?
If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
If the car reaches the destination with 0 fuel left, it is still considered to have arrived.



Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation:
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
"""

"""
Approach 1: 1D DP, O(N^2)
dp[t] means the furthest distance that we can get with t times of refueling.

So for every station s[i],
if the current distance dp[t] >= s[i][0], we can refuel:
dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])

In the end, we'll return the first t with dp[i] >= target,
otherwise we'll return -1.

"""
import heapq

class SolutionLee:
    def minRefuelStops(self, target, startFuel, s):
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i + 1)[::-1]:
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1


"""
Approach 2: Priority Queue, O(NlogN)
i is the index of next stops to refuel.
res is the times that we have refeuled.
pq is a priority queue that we store all available gas.

We initial res = 0 and in every loop:

We add all reachable stop to priority queue.
We pop out the largest gas from pq and refeul once.
If we can't refuel, means that we can not go forward and return -1
"""

class SoutionLee2:
    def minRefuelStops(self, target, cur, s):
        pq = []
        res = i = 0
        while cur < target:
            while i < len(s) and s[i][0] <= cur:
                heapq.heappush(pq, -s[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res


class Solution3:
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1


class Solution4:
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans

