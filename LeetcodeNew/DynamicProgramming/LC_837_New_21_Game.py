
"""
https://blog.csdn.net/fuxuemingzhu/article/details/83615241

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.
During each draw, she gains an integer number of points randomly from the range [1, W],
where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.
What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
"""

"""
Intuition:
The same problems as "Climbing Stairs".

Explanation:
In a word,
dp[i]: probability of get points i
dp[i] = sum(last W dp values) / W

To get Wsum = sum(last W dp values), we can maintain a sliding window with size at most K.

Time Complexity:
O(N)
"""

class SolutionLee:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W:
            return 1
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K:
                Wsum += dp[i]
            if i - W >= 0:
                Wsum -= dp[i - W]
        return sum(dp[K:])


# It might be better to have a look at below code before reading the post. The result is a summation of the probablity from
class Solution1:
    def new21Game(self, N, K, W):

        dp = [0 for _ in range(N + 1)]
        dp[0] = 1
        for i in range(1, N+1):
            if i <= K:
                # sliding window. size = W
                dp[i] = sum(dp[max([i - W, 0]):i]) * 1.0 / W
            else:
                # start from dp[m] where m < K, and take one more step to i. i>K.
                dp[i] = sum(dp[max([i - W, 0]):K]) * 1.0 / W
        res = sum(dp[K:])
        return res

"""

 * dp[i] represents the total probability to get points i
 * dp[i] = dp[1] * 1/W + dp[2] * 1/W + dp[3] * 1/W + ... dp[i-2] * 1/W + dp[i-1] * 1/W
 * So dp[i] = (dp[1] + dp[2] + ... + dp[i - 1]) / W = Wsum / W
 * Conditional probability: 
 keep a window with size K (assume K = 10), the probability of getting point i is the sum
 * of probability from point i - 10 to i, point i - 9 to i, ... , i -1 to i. 
 Since every card has equal probability,
 * the probability to get any one of cards is 1/10. 
 So the total probability of dp[i] is sum of all conditional
 * probability.
 * Once i is over than or equal to K, we can accumulate probability to final result
 *
 * （翻译）条件概率：dp[i]表示可以到达i分数的概率总和。假设我们的K为10的话，抽到每张牌的概率都是1/10。那么我们只需要从dp[i-10]
 * 开始加就可以了，所以就是维持一个size为K的window。比如12这个数，我们可以由抽到2的概率（dp[2]）乘以1/10或者抽到3的概率（dp[3]）
 * 乘以1/10得来...一直到dp[11] * 1/10，那么把他们相加就是可以到达point i的总概率了（就是dp[i]的值）。相当于是最基本的条件概率。
 * 那么总概率就是 dp[12] = dp[2] * 1/10 + dp[3] * 1/10 + dp[4] * 1/10 + ... + dp[11] * 1/10.
 * 再详细剖析：因为从2到11这10个数都有可能通过只抽一张牌就到达12分。以此类推，只要是point没到K，之前的数都有可能到达当前的数，size超过K的时候，
 * 我们就维持一个size为K的window，再通过条件概率的公式累加和就可以了。
 *
 * 现在我们已经有公式 dp[i] = dp[1] * 1/W + dp[2] * 1/W + dp[3] * 1/W + ... dp[i-2] * 1/W + dp[i-1] * 1/W，
 * 通过这个公式，我们可以换算成 (dp[1] + dp[2] + ... + dp[i - 1]) / W，
 这里的dp[1] + dp[2] + ... + dp[i - 1] 就是Wsum，所以dp[i] = Wsum / W。
 * 换句话来说Wsum就是通过一次抽排就能到当前分数的概率之和。当然，我们这个example公式的Wsum是当i没有超过W时候的值，
 * 如果i超过了W，那就不是从dp[1]开始加了，而是从dp[i - W]开始加，相当于向右挪动window， 最多只能是从point i - W
 * 开始才能通过只抽一张牌就到达point i
    
public double new21Game(int N, int K, int W) {
    if (K == 0 || N >= K + W) {
        return 1;
    }

    double result = 0;
    double Wsum = 1;
    double dp[] = new double[N + 1];
    dp[0] = 1;

    for (int i = 1; i <= N; i++) {
        dp[i] = Wsum / W;
        // when points is less than K, all previous card could go to current i by only drawing one card
        if (i < K) {
            Wsum += dp[i];
        }
        // when points is equal to or more than K, all probability will be accumulated to results
        else {
            result += dp[i];
        }

        // when i is over than W, then we need to move the window
        if (i - W >= 0) {
            Wsum -= dp[i - W];
        }
    }
    return result;
        
"""
"""
thanks to @lee215 for this problem, got some real 'fun' time to think this through.
首先被代码的简洁迷惑以为是道简单题，但最后花了好多时间才搞明白。结合几个人的评论和lee的回复，说一下自己的思路，希望能帮到之后又confused的同学。有不对的地方请指正。（懒得翻译成英语了）
首先从比较可以理解的probability方面入手。thanks to @grimreap, 这样可以建立一些信心了解问题的本质。
Case: N=3, K=1, W=10
i=1 (drawn card-1) : You win as you get 1(1<=N), P(i=1)=1/10=0.1
i=2 (drawn card-2) : You win as you get 2(2<=N), P(i=2)=1/10=0.1
i=3 (drawn card-3) : You win as you get 3(3<=N), P(i=3)=1/10=0.1
All events are independent: Total prob = 0.1+0.1+0.1 = 0.3
Case: N=3, K=2, W=10
i=1 (draw 1) P(draw=1)=0.1 [call this A], Same event, we do not stop now we can draw either 1 or 2, 
as i<K, for drawing 1 or 2 , P(1 or 2)=0.1+0.1=0.2 [call this B], P(complete draw) = P(A)xP(B)=0.1x0.2 = 0.02
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

"""
The transition equation from the first solution is:
dp[i] = 1/w * (dp[i - 1] + dp[i - 2] + ... + dp[i - W])

Substitute all the i with i -1
dp[i-1] = 1/w * (dp[(i - 1) - 1] + dp[(i - 1) - 2] + ... + dp[(i - 1) - W]) = 1/w * (dp[i - 2] + dp[i - 3] + ... + dp[i - 1 - W])

Let's format the equations like this:
(1)  dp[i]      = 1/w * (dp[i - 1] + dp[i - 2] + dp[i - 3] + ... + dp[i - W])
(2)  dp[i-1]    = 1/w * (            dp[i - 2] + dp[i - 3] + ... + dp[i - W] + dp[i - 1 - W])

From (1), subtract (2). Everything from dp[i - 2] to dp[i - W] are cancelled out, leaving only:
dp[i] - dp[i-1] = 1/w * (dp[i - 1] - dp[i - 1 - W]);

Move dp[i-1] to the right. Now we have an equation where each i is only depending on i - 1
dp[i] = dp[i-1] + 1/w * (dp[i - 1] - dp[i - 1 - W]);
"""
"""
A intuitive idea is simply use dp[i] as the probability to reach i, dp[i]=probability[i].

Then dp[i]=sum(dp[i-j]) for j in [1, W], but this causes O(KW) complexity.

In uwi's code,

dp[i] is the prefix for numbers larger than or equal to i, so probability[i]=sum(dp[:i+1])

Let's use p[i] for probability[i].

In this case,

the initial situation is p[0]=1, p[i]=0 for i>0, so dp[0]=1, dp[1]=-1
the recursive formula at i is to update p[i+1:i+W+1] only, so set dp[i+1]+=p[i]/W, dp[i+W+1]-=p[i]/W, and p[i] is maintained in the code as val.

So just add val for i in range(K, N+1).

"""

"""
Intuiatively, we can generate the following equation:

F(x) = (F(x+1) + F(x+2) + ... + F(x+W)) / W
Where F(x) is the prob that we will eventually have <= N points when we have x points.
We will stop picking when we have >= K points, so the exit of the recursion is cur >= K.
There are K+W states in total and for each state < K, we spend O(W) (the for loop) to generate the prob, therefore O(KW+W) in total.
"""


class Solution1:
    def new21Game(self, N, K, W):
        return self.dfs(N, K, W, 0, {})

    def dfs(self, N, K, W, cur, memo):

        if cur >= K:
            return 1.0 if cur <= N else 0

        if cur in memo:
            return memo[cur]

        prob = 0

        for i in range(1, W + 1):
            prob += self.dfs(N, K, W, cur + i, memo)

        prob /= W

        memo[cur] = prob

        return prob

"""
However, do we really need a for loop to get the prob?
Since

F(x) = (F(x+1) + F(x+2) + ... + F(x+W)) / W
F(x+1) = (F(x+2) + F(x+3) + ... + F(x+1+W)) / W
After a substraction, we have

F(x) = F(x+1) - 1/W * (F(x+1+W) - F(x+1))
In this case, we get our prob at points = x by a simple substraction which is O(1).
Here we still have K + W states so the time complexity should be O(K+W).

But Wait...
Why does the exit or the base case of the recursion change..?
That's because the expression

F(x) = F(x+1) - 1/W * (F(x+1+W) - F(x+1))
relies on the fact that for every F(x), we have:

F(x) = (F(x+1) + F(x+2) + ... + F(x+W)) / W
But that is not true.

In fact, when x = K, F(x) = either 1 or 0, but not (F(x+1) + ... + F(x+W)) / W
Since the rule does not apply for F(K), we can not use the formula to calculate F(K-1) !
And that is why we modify the base case here.
At x = K-1, only one more pick left, therefore we have two cases:

1. N-(K-1) >= W, which means we pick all 1 to W safely.
2. N-(K-1) < W, means that some of the numbers will make our points > N. Then we can only pick N-(K-1) from 1 to W.
The prob is therefore min(N-K+1, W) / W
"""


class Solution2:
    def new21Game(self, N, K, W):

        return self.dfs(N, K, W, 0, {})

    def dfs(self, N, K, W, cur, memo):

        if cur == K - 1:
            return min(N - K + 1, W) / W
        if cur > N:
            return 0
        elif cur >= K:
            return 1.0

        if cur in memo:
            return memo[cur]

        prob = self.dfs(N, K, W, cur + 1, memo) - (
                    self.dfs(N, K, W, cur + 1 + W, memo) - self.dfs(N, K, W, cur + 1, memo)) / W

        memo[cur] = prob

        return prob


"""
解题方法
动态规划
类似爬楼梯的问题，每次可以跨[1,W]个楼梯，当一共爬了K个和以上的台阶时停止，问这个时候总台阶数<=N的概率。

使用动态规划，dp[i]表示得到点数i的概率，只有当现在的总点数少于K的时候，才会继续取数。那么状态转移方程可以写成：

1. 当i <= K时，dp[i] = （前W个dp的和）/ W；(爬楼梯得到总楼梯数为i的概率）
2. 当K < i < K + W时，那么在这次的前一次的点数范围是[i - W, K - 1]。我们的dp数组表示的是得到点i的概率，
   
   所以dp[i]=(dp[K-1]+dp[K-2]+…+dp[i-W])/W.
   
   （可以从前一次的基础的上选[1,W]个数字中的一个）
3. 当i>=K+W时，这种情况下无论如何不都应该存在的，所以dp[i]=0.
时间复杂度是O(N)，空间复杂度是O(N).
"""

class Solution3:
    def new21Game(self, N, K, W):
        if K == 0:
            return 1
        dp = [1.0] + [0] * N
        tSum = 1.0
        for i in range(1, N + 1):
            dp[i] = tSum / W
            if i < K:
                tSum += dp[i]
            if 0 <= i - W < K:
                tSum -= dp[i - W]
        return sum(dp[K:])


"""
思路： 
题目的意思是，在已有点数不超过K的情况下，可以从[1, W]中任选一个数，保证和不超过N。求最后当点数超过K时，这个点数小于N的概率。
这个问题其实类似于爬楼梯，每次可跨上[1, W]阶楼梯。 
采用动态规划，dp[i]表示点数为i的概率，只有当已有点数小于K时，才能再取数，所以有： 
当i<=K时，dp[i] = (前W个dp之和) / W 
当K< i< K+W时，前一次最多只能是K-1点，最少为i-W点，所以dp[i] = (dp[K-1]+dp[K-2]+…+dp[i-W])/W 
当i >= K+W时，无论如何都无法取到，dp[i] = 0
"""
class Solution4:
    def new21Game(self, N, K, W):

        if K == 0: return 1
        dp = [1.0] + [0.0] * N
        # Wsum表示(前W个dp之和)/W
        Wsum = 1.0000
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            # 因为当i>=K时，不能再取数，因此后面的概率不能累加
            if i < K: Wsum += dp[i]
            # 因为只需要计算前w个dp之和，所以当i>=W时，减去最前面的dp。
            if 0 <= i - W < K: Wsum -= dp[i - W]
        return sum(dp[K:])




