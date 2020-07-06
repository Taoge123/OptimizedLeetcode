"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/613853/Python-5-solutions-gradually-optimizing-from-Naive-DFS-to-O(n)-space-DP
https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/151850/C%2B%2B-DP-solution-Space-complexity-from-O(n2)-to-O(n).

Approach 2: Priority Queue, O(NlogN)
i is the index of next stops to refuel.
res is the times that we have refeuled.
pq is a priority queue that we store all available gas.

We initial res = 0 and in every loop:

We add all reachable stop to priority queue.
We pop out the largest gas from pq and refeul once.
If we can't refuel, means that we can not go forward and return -1

"""

"""
0...A...B.......C

我们可以这样考虑．现在有一定量的startFuel，假设可以驶过两个加油站，但是达不到第三个加油站．说明我们应该在前两个加油站中的某一个或全部两个停下来加油．
但是该加多少呢？

其实，我们不用想的太远，千里之行始于足下，目前只需要加油使得能够开到第三个加油站即可．于是，我们优先考虑前两个加油站里较多的那一个，
不够的话就算上另一个．反正到了第三个加油站后，我们就又多了一个option．等过了第三个加油站，我们再类似地考虑，是否需要加油才能开到第四个加油站．
如果需要，就在前三个加油站里面尚未加过油的那些里，选择油量最多的那个即可；不需要的话，就把第四个加油站放入option list,考虑是否需要加油才能开到第五个加油站...

这就是贪心法的最优策略．特别注意，我们得把target当做一个加油站来处理。不能只用贪心法处理到最后一个加油站，再用剩下的curFuel来考虑是否能到target，
那样是错误的：因为这样的话你只是用尽全力到达最后一个加油站，而并没有用尽全力去到达target。

Leetcode Link
"""
import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        heap = []
        res = 0
        i = 0
        while startFuel < target:
            # heap is a priority queue that we store all available gas
            # distance <= 我的fuel就能到
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(heap, -stations[i][1])
                i += 1
            if not heap:
                return -1
            startFuel += -heapq.heappop(heap)
            res += 1
        return res



"""
解题思路：
动态规划的方法，但这里需要做个转换，原题是求加油的最少的次数，其实可以转换为在有n个加油站的情况下，
加i次油（i<=n）的情况下，车子能走的最长路径，算法的时间复杂度是O(n^2)。
dp三要素：
1，状态定义：dp[i] 为加 i 次油能走的最远距离，题目结果就是满足 dp[i] >= target 的最小 i。
2，边界就是dp[0] = startFuel
3,状态转移方程：
依次计算每个 dp[i]，对于 dp[0]，就只用初始的油量 startFuel 看能走多远。
每多一个加油站 station[i] = (location, capacity)，
如果之前可以通过加 t 次油到达这个加油站，现在就可以通过加 t+1 次油得到 capcity 的油量。
举个例子，原本加一次油可以行驶的最远距离为 15，现在位置 10 有一个加油站，有 30 升油量储备，那么显然现在可以加两次油行驶 45 距离。
这里注意一个点，对于每一个加油站，也就是更新dp[t+1]时候，由于新加了一个加油站，后面的加油站会影响前面的，因此只能从后往前遍历
如果从前往后更新，就错了，你好好想一下这个问题。

更详细解释：
算法核心在于抽象问题，也就是建模，大白话说，就是简化问题到另外一种形式
动态规划的算法核心是根据上一个状态求出下一个状态，一次性求解出全部状态的答案，然后返回你需要的，有的返回dp0有的返回dp-1
对于这道题，首先我们使用dp状态定义，简化问题，设dpi状态表示，加i次油最远可达距离，返会结果当然是dpi大于target时候的最小i
至此，all u need to think is what's dp[i], not the original question
然后边界就太简单了，dp0就是不加油最远跑到哪，当然就是初始油量
最后一个就是解决状态转移，如何从dp0转移到dp1，当然是能到达的情况下（dp[t] >= location），加油后更新为当前最大值
但是注意一点，更新dpi的时候，是不是前面i-1的加油站都要考虑进去？
i通过i-1得到，i-1也会由i-2得到，也就是说后面会影响前面的，因此需要从后面向前更新每个位置的最大值


"""

class SolutionDP:
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        n = len(stations)
        # dp[i][j]表示经过第i个加油站加油j次能够到达的最远距离
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        if startFuel >= target:
            return 0
        for i in range(n + 1):
            dp[i][0] = startFuel
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                # 前i-1站加j次，本站不加油
                if dp[i - 1][j] >= stations[i - 1][0]:
                    dp[i][j] = dp[i - 1][j]
                # 前i-1站加j-1次，本站加油
                if dp[i - 1][j - 1] >= stations[i - 1][0]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + stations[i - 1][1])

        for i in range(n + 1):
            if dp[n][i] >= target:
                return i
        return -1




class Solution1:
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)  # 更新为更大值

        for i, d in enumerate(dp):
            if d >= target: return i # 就是返回能到达终点的最小i
        return -1

