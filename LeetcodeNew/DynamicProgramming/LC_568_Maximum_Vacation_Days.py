
"""
https://leetcode.com/problems/maximum-vacation-days/solution/
https://leetcode.com/problems/maximum-vacation-days/discuss/267874/Python3-top-down-%2B-bottom-up-DP-solutions-with-explanation.


LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

Rules and restrictions:
You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.

Example 1:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation:
Ans = 6 + 3 + 3 = 12.

One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day.
(Although you start at city 0, we could also fly to and start at other cities since it is Monday.)
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.
Example 2:
Input:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
Output: 3
Explanation:
Ans = 1 + 1 + 1 = 3.

Since there is no flights enable you to move to another city, you have to stay at city 0 for the whole 3 weeks.
For each week, you only have one day to play and six days to work.
So the maximum number of vacation days is 3.
Example 3:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
Output: 21
Explanation:
Ans = 7 + 7 + 7 = 21

One of the best strategies is:
1st week : stay at city 0, and play 7 days.
2nd week : fly from city 0 to city 1 on Monday, and play 7 days.
3rd week : fly from city 1 to city 2 on Monday, and play 7 days.
Note:
N and K are positive integers, which are in the range of [1, 100].
In the matrix flights, all the values are integers in the range of [0, 1].
In the matrix days, all the values are integers in the range [0, 7].
You could stay at a city beyond the number of vacation days, but you should work on the extra days, which won't be counted as vacation days.
If you fly from the city A to the city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
We don't consider the impact of flight hours towards the calculation of vacation days.


"""
"""
题目大意：
给定N个城市，K周时间。

矩阵flights描述N个城市之间是否存在航班通路。

若flights[i][j] = 1，表示i与j存在通路，否则表示不存在。特别的，flights[i][i]恒等于0。

矩阵days表示可以在某城市逗留的最长天数。

例如days[i][j] = k，表示第i个城市第j周最长可以逗留k天。

初始位于0号城市，每周可以选择一个能够到达的城市逗留（也可以留在当前城市）。

求最优策略下的最长逗留总天数。

注意：

N和K是正整数，范围[1, 100]
矩阵flights的元素范围[0, 1]
矩阵days的元素范围[0, 7]
解题思路：
动态规划（Dynamic Programming）

dp[w][c]表示第w周选择留在第c个城市可以获得的最大总收益

初始令dp[w][0] = 0, dp[w][1 .. c - 1] = -1

当dp[w][c] < 0时，表示第c个城市在第w周时还不可达。
状态转移方程：

for w in (0 .. K)
    for sc in (0 .. N)
        if dp[w][sc] < 0:
            continue
        for tc in (0 .. N)
            if sc == tc or flights[sc][tc] == 1:
                dp[w + 1][tc] = max(dp[w + 1][tc], dp[w][sc] + days[tc][w])

"""
import collections

class Solution1:
    def maxVacationDays(self, flights, days):

        N, K = len(days), len(days[0])
        dp = [0] + [-1] * (N - 1)
        for w in range(K):
            ndp = [x for x in dp]
            for sc in range(N):
                if dp[sc] < 0: continue
                for tc in range(N):
                    if sc == tc or flights[sc][tc]:
                        ndp[tc] = max(ndp[tc], dp[sc] + days[tc][w])
            dp = ndp
        return max(dp)

"""
思路：

用动态规划来求解。我们定义dp[k][n] (0 < k < K, 0 < n < N)表示在第k周在城市n休假时，可以获得的最大休假天数。
我们初始化所有dp数组的元素为-1，那么状态转移方程就是：

dp[k][n] = max(dp[k-1][c] + days[n][k])，如果dp[k - 1][c] != -1并且(c == n或者flight[c][n] == 1)。
否则dp[k][n] = -1。最后返回dp[k][0],...,dp[k][n-1]中的最大值。

算法的时间复杂度是O(KN^2)，空间复杂度是O(KN)。
"""
class Solution2:
    def maxVacationDays(self, flights, days):
        N = len(flights)
        K = len(days[0])
        memo = {}

        # start from city 0 and week 0
        return self.dfs(0, 0, flights, days, N, K, memo)

    def dfs(self, city, week, flights, days, N, K, memo):
        if (city, week) in memo:
            return memo[(city, week)]

        if week == K:
            return 0

        maxDay = 0
        for i in range(N):
            # we could either stay in current city or fly to other city at current week
            if i == city or flights[city][i] == 1:
                # update maxDay using the result for next week
                maxDay = max(maxDay, days[i][week] + self.dfs(i, week + 1, flights, days, N, K, memo))

        memo[(city, week)] = maxDay
        return maxDay


"""
flights是n*n矩阵, 表示city之间是否能飞; 
days[i][j] 是n*k矩阵，表示在city i，week j 这个时间最多能玩几天。

初始是在city 0, 问最多能玩几天。注意的是第一周不一定非得在city 0, 可以当天飞到其他city开始。
解法1：DFS， 对每一个当前city，遍历所有它能到达的城市，返回当前week在cur_city能得到的最大值，
days[i][week] + dfs(flights, days, i, week+1, data)，通过打表data来保存中间值,不然会超时。

解法2：DP, 用dp[i][j]来表示 week i in city j, 最多可以得到多少个vacation。

dp[i][j] = max(dp[i - 1][k] + days[j][i]) (k = 0...N - 1, if we can go from city k to city j)
"""

"""
Approach #1 Using Depth First Search [Time Limit Exceeded]
Algorithm

In the brute force approach, we make use of a recursive function dfsdfs, 
which returns the number of vacations which can be taken startring from 
cur\_citycur_city as the current city and weeknoweekno as the starting week.

In every function call, we traverse over all the cities(represented by ii) 
and find out all the cities which are connected to the current city, cur\_citycur_city. 
Such a city is represented by a 1 at the corresponding flights[cur\_city][i]flights[cur_city][i] position. 
Now, for the current city, we can either travel to the city which is connected to it or we can stay in the same city. 
Let's say the city to which we change our location from the current city be represented by jj. 
Thus, after changing the city, we need to find the number of vacations which we can take from the new city as the current city 
and the incremented week as the new starting week. This count of vacations can be represented as: 
days[j][weekno] + dfs(flights, days, j, weekno + 1)days[j][weekno]+dfs(flights,days,j,weekno+1).

Thus, for the current city, we obtain a number of vacations by choosing different cities as the next cities. 
Out of all of these vacations coming from different cities, we can find out the maximum number of vacations 
that need to be returned for every dfsdfs function call.

public class Solution {
    public int maxVacationDays(int[][] flights, int[][] days) {
        return dfs(flights, days, 0, 0);
    }
    public int dfs(int[][] flights, int[][] days, int cur_city, int weekno) {
        if (weekno == days[0].length)
            return 0;
        int maxvac = 0;
        for (int i = 0; i < flights.length; i++) {
            if (flights[cur_city][i] == 1 || i == cur_city) {
                int vac = days[i][weekno] + dfs(flights, days, i, weekno + 1);
                maxvac = Math.max(maxvac, vac);
            }
        }
        return maxvac;
    }
}

Complexity Analysis

Time complexity : O(n^k)O(n k). Depth of Recursion tree will be kk and each node contains nn branches in the worst case. Here nn represents the number of cities and kk is the total number of weeks.

Space complexity : O(k)O(k). The depth of the recursion tree is kk.

"""

"""
Approach #2 Using DFS with memoization [Accepted]:
Algorithm

In the last approach, we make a number of redundant function calls, 
since the same function call of the form dfs(flights, days, cur_city, weekno) 
can be made multiple number of times with the same cur\_citycur_city and weeknoweekno. 
These redundant calls can be pruned off if we make use of memoization.

In order to remove these redundant function calls, we make use of a 2-D memoization array memomemo. 
In this array, memo[i][j]memo[i][j] is used to store the number of vacactions that can be taken using the i^{th}i 
th  city as the current city and the j^{th}j 
th  week as the starting week. This result is equivalent to that obtained using the function call: 
dfs(flights, days, i, j). Thus, if the memomemo entry corresponding to the current function call already contains a valid value, 
we can directly obtain the result from this array instead of going deeper into recursion.

public class Solution {
    public int maxVacationDays(int[][] flights, int[][] days) {
        int[][] memo = new int[flights.length][days[0].length];
        for (int[] l: memo)
            Arrays.fill(l, Integer.MIN_VALUE);
        return dfs(flights, days, 0, 0, memo);
    }
    public int dfs(int[][] flights, int[][] days, int cur_city, int weekno, int[][] memo) {
        if (weekno == days[0].length)
            return 0;
        if (memo[cur_city][weekno] != Integer.MIN_VALUE)
            return memo[cur_city][weekno];
        int maxvac = 0;
        for (int i = 0; i < flights.length; i++) {
            if (flights[cur_city][i] == 1 || i == cur_city) {
                int vac = days[i][weekno] + dfs(flights, days, i, weekno + 1, memo);
                maxvac = Math.max(maxvac, vac);
            }
        }
        memo[cur_city][weekno] = maxvac;
        return maxvac;
    }
}

"""


"""
Let's maintain best[i], the most vacation days you can have ending in city i on week t. 
At the end, we simply want max(best), the best answer for any ending city.

For every flight i -> j (including staying in the same city, when i == j), 
we have a candidate answer best[j] = best[i] + days[j][t], and we want the best answer of those.

When the graph is sparse, we can precompute flights_available[i] = [j for j, 
adj in enumerate(flights[i]) if adj or i == j] instead to save some time, but this is not required.
"""

class Solution3:
    def maxVacationDays(self, flights, days):
        NINF = float('-inf')
        N, K = len(days), len(days[0])
        best = [NINF] * N
        best[0] = 0

        for t in xrange(K):
            cur = [NINF] * N
            for i in xrange(N):
                for j, adj in enumerate(flights[i]):
                    if adj or i == j:
                        cur[j] = max(cur[j], best[i] + days[j][t])
            best = cur
        return max(best)

class Solution33:
    def maxVacationDays(self, flights, days):
        n, k = len(days), len(days[0]) # n cities, k weeks
        max_vacation = [0] + [float('-inf') for _ in range(n-1)]

        for week in range(k):
            curr = [float('-inf') for _ in range(n)]

            for dep_city in range(n):
                for arr_city, flight_exists in enumerate(flights[dep_city]):
                    if flight_exists or dep_city == arr_city:
                        curr[arr_city] = max(curr[arr_city], max_vacation[dep_city] + days[arr_city][week])

            max_vacation = curr

        return max(max_vacation)


"""
Thought process
Recursive backtracking

    def backtrack(week, city):

        - backtrack(week, city) = max(stay: days[city][week] + backtrack(week+1, city), fly: 
          max(backtrack(week+1, other) + days[other][week]) for flights[city][other] == 1)
        - flights can be optimized using adjacency list
        - base case: week == N, return 0

because there is no state change, we can use memoization

be careful that even if working in a city all week, it can still provide more opportunites for more vacation in future (because maybe you can only fly to other city and cannot come back, but future weeks in this city may have many vacations)

just try everything possible!

Iterative solution is also simple
"""
# Top-down DP

import functools


class Solution4:
    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly]
		           for city in flights]
        @functools.lru_cache(None)
        def backtrack(week, city):
            if week == K:
                return 0
            stay = days[city][week] + backtrack(week+1, city)
            fly = max((days[other][week] + backtrack(week+1, other)
                      for other in flights[city]), default=0)
            return max(stay, fly)
        return backtrack(0, 0)


# Bottom-up DP
class Solution5:
    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly]
                   for city in flights]
        dp = [[0] * N for _ in range(K + 1)]
        for week in range(K - 1, -1, -1):
            for city in range(N):
                stay = days[city][week] + dp[week + 1][city]
                fly = max((days[other][week] + dp[week + 1][other]
                           for other in flights[city]), default=0)
                dp[week][city] = max(stay, fly)
        return dp[0][0]


# O(K) space optimization
class Solution6:
    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly]
                   for city in flights]
        dp = [0] * N
        cur = dp[:]
        for week in range(K-1, -1, -1):
            for city in range(N):
                stay = days[city][week] + dp[city]
                fly = max((days[other][week] + dp[other]
                          for other in flights[city]), default=0)
                cur[city] = max(stay, fly)
            dp, cur = cur, dp
        return dp[0]


"""
It's very clean. I have one question, could you elaborate how this works without tracking city that is visited in previous week? 
You just do flights[i][i] = 1 so I first thought this doesn't work 
if there is a city which can never be visited from other cities but has 7 vacation days for all weeks, 
but it seems your code passes all test cases, I still cannot figure out this part.

thanks. the problem allows you to stay in the same city once you reach it 
(instead of forcing you to travel to a different connected city) that's why i set flights[i][i] = 1.

if a city is only connected to itself it will never be used in the calculation of maximum vacation days starting from city 0 (unless of course IT IS city 0). 
this is why dp[0][0] is returned at the end, because the problem specifies starting at city 0. 
this is also the reason for if v, this represents a connection between 2 cities.

there is potentially some wasted computation in that dp[week][city] is calculated for all weeks/cities, 
even if the city is not connected to city 0.

one optimization would be to figure out the connected component city 0 belongs to, 
and ignore cities not belonging to that component

"""
class Solution7:
    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        for i in range(N): flights[i][i] = 1
        dp = [[0 for _ in range(N)] for _ in range(K + 1)]
        for k in range(K - 1, -1, -1):
            for n in range(N):
                dp[k][n] = max(dp[k + 1][i] + days[i][k] for i, v in enumerate(flights[n]) if v)
        return dp[0][0]


# DP, much faster than DFS
class Solution8:
    def maxVacationDays(self, flights, days):

        N, K = len(days), len(days[0])
        most = [float('-inf')] * N
        most[0] = 0
        for week in range(K):
            cur = [float('-inf')] * N
            for loc in range(N):
                for _next, f in enumerate(flights[loc]):
                    if f or _next == loc:
                        cur[_next] = max(cur[_next], most[loc] + days[_next][week])
            most = cur
        return max(most)


# DFS, much slower than DP
class Solution88:
    def maxVacationDays(self, flights, days):

        self.flights = flights
        self.days = days
        self.K = len(days[0])
        self.memo = {}
        ans = 0
        for loc, f in enumerate(flights[0]):
            if f == 1 or loc == 0:
                ans = max(ans, self.dfs(0, loc))
        return ans

    def dfs(self, week, loc):
        if (loc, week) in self.memo:
            return self.memo[(loc, week)]

        self.memo[(loc, week)] = 0
        if week != self.K:
            for _next, f in enumerate(self.flights[loc]):
                if f == 1 or _next == loc:
                    self.memo[(loc, week)] = max(self.memo[(loc, week)], self.dfs(week + 1, _next))
            self.memo[(loc, week)] += self.days[loc][week]
        return self.memo[(loc, week)]



"""
First convert flights to a graph represented by adjacency lists. 
An edge exists between two cities if there is a flight connecting them. 
And also include the source city in destination list since we can stay at the source city.

Then dp[week][city] recurrence: dp[w][c] = days[c][w] + max(dp[w+1][dest] for dest in g[c]).
It's easier to use bottom up here since the starting point (week 0) is fixed instead of ending point. 
Using bottom up, we can get the maximum value for week 0 in our dp table.

Eventually since we start at city 0, answer is the max days from city 0's destinations 
(in day 0, you can spend rest days of week 0 in city 0 or other cities connected to city 0)
"""
class Solution9:
    def maxVacationDays(flights, days):
        n, k = len(days), len(days[0])
        g = [[j for j, dst in enumerate(city) if dst] + [i] for i, city in enumerate(flights)]
        dp = [[0] * n for _ in range(k + 1)]
        for w in range(k)[::-1]:
            for c in range(n):
                dp[w][c] = days[c][w] + max(dp[w + 1][dst] for dst in g[c])
        return max(dp[0][dst] for dst in g[0])


class Solution10:
    def maxVacationDays(self, flights, days):
        n = len(flights)
        k = len(days[0])
        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if flights[i][j]:
                    graph[j].append(i)
            graph[i].append(i)
        dp = [[-float('inf')]*n for i in range(k+1)]
        dp[0][0] = 0
        for i in range(1,k+1):
            for j in range(n):
                for k in graph[j]:
                    dp[i][j] = max(dp[i][j],dp[i-1][k])
                dp[i][j] += days[j][i-1]
        return max(dp[-1])


class Solution11:
    def maxVacationDays(self, flights, days):
        if not flights: return None
        n = len(flights)
        k = len(days[0])
        if k == 0: return 0
        dp = [[0 for i in range(0, n)] for j in
              range(0, k)]  # representing the maximum days that you could play if given j weeks, ending in city i
        for i in range(0, n): flights[i][i] = 1
        dp[0][0] = days[0][0]
        for i in range(1, n):
            if flights[0][i] == 1:
                dp[0][i] = days[i][0]
            else:
                dp[0][i] = -1  # it is impossible to endup in this city on day 0

        for j in range(1, k):
            for i in range(0, n):
                dp[j][i] = -1
                for q in range(0, n):
                    if dp[j - 1][q] != -1 and flights[q][i] == 1:
                        dp[j][i] = max(days[i][j] + dp[j - 1][q], dp[j][i])

        return max(dp[-1])


# Python Clean Solution O(N*N*K)
class Solution12:
    def maxVacationDays(self, flights, days):

        dp = [[float("-inf")] * len(flights) for _ in range(len(days[0]) + 1)]
        dp[0][0] = 0
        for i in range(len(days[0])):
            for j in range(len(flights)):
                for k in range(len(flights)):
                    if flights[k][j] == 1 or j == k:
                        dp[i+1][j] = max(dp[i+1][j], dp[i][k] + days[j][i])
        return max(dp[-1])

