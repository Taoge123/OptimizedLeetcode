"""
https://leetcode.com/problems/new-21-game/discuss/220949/Python-3-Memorize-DFS-from-O(KW%2BW)-to-O(K-%2B-W)

https://www.youtube.com/watch?v=bd0t6cj7_4E
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/837.New-21-Game

837.New-21-Game
首先关于理解题意。这道题是基于赌场游戏black Jack的规则。玩家每一轮拿一张牌，可以拿任意轮(hit)。玩家也可以随时停止拿牌(stand)。但是如果拿到的所有牌的点数大于21，就爆炸了(bust)，也就是输。同时庄家也会陪玩家玩一样的规则，但是庄家是后手，当庄家拿满17的分数之后就会主动stand。

因为每一轮都是玩家先决策。因此玩家有先爆的风险。而且玩家可以赌博在大于17的时候继续hit.

再回到这一题。这题其实是帮助分析庄家赢的概率。也就是N=21,K=17的情况。

解法1：
一种比较常见的思想就是自上而下地递归处理。f(x)表示从手头积分是x时，最终实现目标（也就是等到停牌时积分小于等于N）的概率。那么从x可以通过一步跳转到x+1,x+2,x+3...,x+W。因此有递归方程

f(x) = [f(x+1)+f(x+2)+...+f(x+W)]/W
其中递归的终点是，当x>=K时停止递归.在这个边界条件，当x<=N时，f(x)=1；当x>N时，概率是f(x)=0.

本题中递归的解法会超时，显然会有很多重复的计算。

解法2：
另一种完全不同的思想，就是计算f(x)表示从0开始能走到x的概率。显然得到当前的积分x，完全取决于之前的积分。比如说当前积分x，可能是通过前一轮x-3的积分，再抽中一张3而来，而抽中3的概率永远是1/W。

我们有递归关系：

f(x) = f(x-1)/W + f(x-2)/W +...+ f(x-W)/W
这就是动态规划的思想。需要注意f(x)里面x必须是大于等于0的。也就是说，当W=10的时候，计算f(3) = f(0)/W+f(1)/W+f(2)/W，3只有三个前驱状态，而不是W个。

以上的算法会超时。为了节省时间，我们发现f(x)通常情况下就是它之前一个宽度为W的滑窗的和的1/W。特别注意，对于较大的x和较小的x，这个滑窗的宽度不见得都是W。可以想象，当x较小时，滑窗会不断增长；而x较大时，滑窗会不断缩短。滑窗每滑动一个，需要新增最近的元素，减去最远的元素，这要求

x-1<K
x-W-1>=0


"""


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (K + W)
        if len(dp) == 1:
            return 1
        for k in range(K, min(N + 1, K + W)):
            dp[k] = 1

        S = N - K + 1
        for k in range(K - 1, -1, -1):
            dp[k] = S / W
            S += dp[k] - dp[k + W]
        return dp[0]






