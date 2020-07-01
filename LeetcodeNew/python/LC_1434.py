
"""
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
                    if ((state >> person) & 1) == 1:
                        continue
                    newDP[state + (1 << person)] += dp[state]
                    newDP[state + (1 << person)] %= mod
            dp = newDP[:]
        return dp[(1 << n) - 1]









