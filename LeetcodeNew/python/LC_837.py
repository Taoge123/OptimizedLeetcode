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


class SolutionTony1:
    def new21Game(self, N, K, W):
        return self.dfs(N, K, W, 0, {})

    def dfs(self, N, K, W, i, memo):

        if i == K - 1:
            return min(N - K + 1, W) / W
        if i > N:
            return 0
        elif i >= K:
            return 1.0

        if i in memo:
            return memo[i]

        prob = self.dfs(N, K, W, i + 1, memo) - (self.dfs(N, K, W, i + 1 + W, memo) - self.dfs(N, K, W, i + 1, memo)) / W

        memo[i] = prob

        return prob


class SolutionTLE:
    def new21Game(self, N, K, W):
        return self.dfs(N, K, W, 0, {})

    def dfs(self, N, K, W, i, memo):

        if i >= K:
            if i <= N:
                return 1.0
            else:
                return 0
            # return 1.0 if i <= N else 0

        if i in memo:
            return memo[i]

        prob = 0

        for i in range(1, W + 1):
            prob += self.dfs(N, K, W, i + i, memo)

        prob /= W

        memo[i] = prob

        return prob




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



"""
首先被代码的简洁迷惑以为是道简单题，但最后花了好多时间才搞明白。结合几个人的评论和lee的回复，说一下自己的思路，希望能帮到之后又confused的同学。有不对的地方请指正。（懒得翻译成英语了）
首先从比较可以理解的probability方面入手。thanks to @grimreap, 这样可以建立一些信心了解问题的本质。
Case: N=3, K=1, W=10
i=1 (drawn card-1) : You win as you get 1(1<=N), P(i=1)=1/10=0.1
i=2 (drawn card-2) : You win as you get 2(2<=N), P(i=2)=1/10=0.1
i=3 (drawn card-3) : You win as you get 3(3<=N), P(i=3)=1/10=0.1
All events are independent: Total prob = 0.1+0.1+0.1 = 0.3
Case: N=3, K=2, W=10
i=1 (draw 1) P(draw=1)=0.1 [call this A], Same event, we do not stop now we can draw either 1 or 2 , as i<K, for drawing 1 or 2 , P(1 or 2)=0.1+0.1=0.2 [call this B], P(complete draw) = P(A)xP(B)=0.1x0.2 = 0.02
i=2 (drawn card-2) : You win as you get 2(2<=N) and you stop as 2>=K, P(i=2)=1/10=0.1
i=3 (drawn card-3) : You win as you get 3(3<=N) and you stop as 2>=K, P(i=3)=1/10=0.1
这个计算方法跟Lee的是反过来的，但是最后的结果（本质）是一样的。
而Lee的思路是，p[i]（dp[i]） 是得到这个点的概率，比如w(范围)是[1,10]. K =3
i=1(抽中1分的概率)就是 1/10.
i=2: 0.1(抽中2分的概率)+0.1x0.1(两次抽中1)的概率
i=3: 0.1 (抽中3分的概率) + 0.1x0.1(第一次抽中1，第二次抽中2) + 0.1x0.1(第一次抽中2，第二次抽中1)+0.1x0.1x0.1（三次抽中0.1）
可以从公式里面归纳出
i=1:
0.1x1
i=2:
0.1x(1+0.1)
i=3:
0.1(1+0.1+0.1+0.01) = 0.1(1+0.1+0.11) 括号里是之前的p的sum，以此来推出Wsum的公式
那为什么>k之后，几不变了呢，例如k=3
i=4: 0.1(抽中4)+0.1x0.1(抽中1 and 3) +0.1x0.1(抽中2 and 2)+0.1x0.1x0.1(抽中2个1，一个2)
i=5: 0.1(抽中4)+0.1x0.1(抽中1 and 4) +0.1x0.1(抽中2 and3)+0.1x0.1x0.1(抽中2个1，一个3)
…
可以看到，最后大于k的公式后面都是一样的。因为3（k）是一道坎，只有抽中小于3的数，后面才可能继续抽。

最后。。如果i-w >0, 比如say W = 10, when we reach i = 11, dp[i] = Wsum / W = (dp[1] + .. + dp[10]) /10
i = 11是不可能一次抽中的（大于w），所以要把一次抽中的概率减去，就是第一次。
i = 12不可能跟2一样（抽中1一次11，再抽中1，也不可能一下抽中12）要把这次概率减去。

最后这块我只能从概念上这样理解，但不能从公式上进行证明，如果可以请帮助。
"""


class SolutionLe:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W: return 1
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K: Wsum += dp[i]
            if i - W >= 0: Wsum -= dp[i - W]
        return sum(dp[K:])



class SolutionTD:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W - 1:
            return 1

        memo = [0] * K
        memo[K - 1] = (N - K + 1) / W

        for i in reversed(range(K - 1)):
            memo[i] = memo[i + 1] + (memo[i + 1] - self.helper(i + W + 1, N, K, memo)) / W
        return memo[0]

    def helper(self, i, N, K, memo):
        if i > N:
            return 0
        if i >= K:
            return 1
        return memo[i]




