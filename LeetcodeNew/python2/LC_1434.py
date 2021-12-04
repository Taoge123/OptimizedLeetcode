
"""
https://leetcode-cn.com/problems/number-of-ways-to-wear-different-hats-to-each-other/solution/python-3xie-gei-zi-ji-de-chao-xiang-xi-zhuang-ya-d/
https://leetcode-cn.com/problems/number-of-ways-to-wear-different-hats-to-each-other/solution/python-3xie-gei-zi-ji-de-chao-xiang-xi-zhuang-ya-d/
https://leetcode-cn.com/problems/number-of-ways-to-wear-different-hats-to-each-other/solution/python-01bei-bao-by-dangerusswilson/



state: 000101011000
i-bit represen =t if the i-th hat has been taken
dp[state] : the number of ways for this state


物品是人
for p in range(n):
    for state in range(111111111(bit)):
        for hat in HatsForThisPerson[p]:
            if hat has beent taken in state:
                continue
            else:
                newDP[state+hat] += dp[state]

res = sim(dp[state]) for those states contain n bit 1



如果换成不枚举人(40), 而是枚举帽子(10)

state: 000101011000
i-bit represen =t if the i-th hat has been taken
for hat in range(40):
    for state in range(1111111111(bit)):
        for person in PersonsForThisHat[h]:
            if person has taken in this state:
                continue
            else:
                newDP[state+person] += dp[state]

res = dp[111111111]
"""

"""
1434.Number-of-Ways-to-Wear-Different-Hats-to-Each-Other
这道题是一道典型的背包+状态压缩的DP问题。

最初的想法是将帽子作为状态。也就是用一串01向量来表示第i顶帽子是否被人taken了。大致的算法是:

for (int p=0; person < n; person++)
  for (int state = 000...000; state <= 111..111; state++)
  {
      for (int hat : HatsForThisPerson[p])
      {
          if (hat has been taken in state)
            continue;
          dp_new[state + hat] += dp[state]
      }
  }
最终的答案是在所有的state里面找出那些恰好有10个1的那些，取这些dp[state]的和。

但是这个方法有两大问题。首先state太大，有2^40种，第二层循环太复杂。其次，最终的答案要取C(40,10)种可能，也不实际。

比较巧妙的思路是看到人的数量最多只有10，用它来做状态非常合适。我们改定义为：用一串01向量来表示第i个人是否已经take苗子了。大致的算法是：

for (int h = 0; h < 40; h ++)
  for (int state = 000...000; state <= 111..111; state++)
  {
      for (int person : PersonsForThisHat[h])
      {
          if (person has taken hat in state)
            continue;
          dp_new[state + person] += dp[state]
      }
  }
最终的答案就是dp[111...111]
"""

import collections
import functools


class SolutionTony:
    def numberWays(self, hats) -> int:
        mod = 10 ** 9 + 7
        n = len(hats)
        h2p = collections.defaultdict(list)

        for p, hs in enumerate(hats):
            for h in hs:
                h2p[h].append(p)

        full_mask = (1 << n) - 1
        @functools.lru_cache(None)
        def dfs(i, mask):
            if mask == full_mask:
                return 1

            if i >= 41:
                return 0

            res = dfs(i + 1, mask)
            for p in h2p[i]:
                if mask & (1 << p):
                    continue

                res += dfs(i + 1, mask | (1 << p))
            return res
        return dfs(0, 0) % mod



class Solution:
    def numberWays(self, hats) -> int:
        n = len(hats)
        dp = [0 for i in range(1 << n)]
        mod = 10 ** 9 + 7
        personForThisHat = collections.defaultdict(list)
        for i, hat in enumerate(hats):
            for person in hat:
                personForThisHat[person].append(i)

        dp[0] = 1
        for hat in range(1, 41):
            newDP = dp[:]
            for state in range(1 << n):
                for person in personForThisHat[hat]:
                    # hat were taken
                    if ((state >> person) & 1) == 1:
                        continue
                    newDP[state + (1 << person)] += dp[state]
                    newDP[state + (1 << person)] %= mod
            dp = newDP[:]
        return dp[(1 << n) - 1]


class SolutionTD:
    def numberWays(self, hats) -> int:
        n = len(hats)
        N = (1 << n) - 1
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(cur, state):
            # cur 代表当前轮到第cur顶帽子可供选择
            # state 代表当前戴帽的人有哪些，为二进制压缩状态形式
            # 首先，如果当前所有人都带上了帽，则返回1
            if state == N:
                return 1

            # 若不满足所有人都戴上了帽，且当前也没有帽子了，则返回0
            if cur > 40:
                return 0

            # 首先考虑不戴该顶帽子，直接考虑后一顶，则其值应为dp(cur+1, pos)
            res = dfs(cur + 1, state)

            # 考虑有人佩戴该顶帽子
            for i in range(n):
                # 找到喜欢该帽子的人，且这个人并没有戴其他帽子（即二进制pos中该位置为0）
                if cur in hats[i] and state & (1 << i) == 0:
                    res += dfs(cur + 1, state + (1 << i))

            return res % mod

        return dfs(0, 0)




class SolutionDFS:
    def numberWays(self, hats) -> int:
        memo = {}
        return self.dfs(hats, 0, 0, memo)

    def dfs(self, hats, pos, state, memo):
        n = len(hats)
        N = (1 << n) - 1
        mod = 10 ** 9 + 7

        if (pos, state) in memo:
            return memo[(pos, state)]

        if state == N:
            return 1

        if pos > 40:
            return 0

        res = self.dfs(hats, pos + 1, state, memo)

        for i in range(n):
            if pos in hats[i] and state & (1 << i) == 0:
                res += self.dfs(hats, pos + 1, state + (1 << i), memo)

        memo[(pos, state)] = res
        return res % mod




class SolutionDFS2:
    def numberWays(self, hats) -> int:
        # 构建帽子到人的对应关系，以逐顶帽子分配
        hats = [set(hat) for hat in hats]
        table = collections.defaultdict(list)
        for person in range(1, 41):
            for i, hat in enumerate(hats):
                if person in hat:
                    table[person].append(i)
        memo = {}
        return self.dfs(hats, 0, 0, table, memo)

    def dfs(self, hats, state, pos, table, memo):
        N = (1 << len(hats)) - 1
        mod = 10 ** 9 + 7
        if state == N:
            return 1
        if pos > 40:
            return 0

        if (state, pos) in memo:
            return memo[(state, pos)]
        res = 0
        # 分配第i顶帽子，遍历所有喜欢第i顶帽子的人
        for i in table[pos]:
            # 当前的状态中，第i个人还没有戴帽子
            if (state & (1 << i)) == 0:
                # 尝试把帽子分给第j个人，并且更新状态，问题向前推进
                res += self.dfs(hats, state | (1 << i), pos + 1, table, memo)
        # 不分配第i顶帽子
        res += self.dfs(hats, state, pos + 1, table, memo)
        res %= mod
        memo[(state, pos)] = res
        return memo[(state, pos)]



