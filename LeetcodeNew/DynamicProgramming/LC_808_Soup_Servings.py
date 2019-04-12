
"""
http://www.cnblogs.com/grandyang/p/9406434.html

There are two types of soup: type A and type B. Initially we have N ml of each type of soup.
There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B
Serve 75 ml of soup A and 25 ml of soup B
Serve 50 ml of soup A and 50 ml of soup B
Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.
Each turn, we will choose from the four operations with equal probability 0.25.
If the remaining volume of soup is not enough to complete the operation,
we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first,
plus half the probability that A and B become empty at the same time.

Example:
Input: N = 50
Output: 0.625
Explanation:
If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time,
is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

0 <= N <= 10^9.
Answers within 10^-6 of the true value will be accepted as correct.

"""
"""
First, 25ml is annoying
The decription is very difficult to understand, and all 25ml just make it worse.
When I finally figure it out, I consider only how many servings left in A and B.
1 serving = 25ml.
Well, it works similar to your milk powder or protin powder.
If the left part is less than 25ml, it is still considered as one serving.

Second, DP or recursion with memory
Now it's easy to solve this problem.
f(a,b) means the result probability for a ml of soup A and b ml of soup B.
f(a-4,b) means that we take the first operation: Serve 100 ml of soup A and 0 ml of soup B. f(a-3,b-1), f(a-2,b-2), f(a-1,b-3) are other 3 operations.
The condition a <= 0 and b <= 0 means that we run out of soup A and B at the same time, so we should return a probability of 0.5, which is half of 1.0.
The same idea for other two conditions.
I cached the process as we do for Fibonacci sequence. It calculate every case for only once and it can be reused for every test case. No worries for TLE.

Third, take the hint for big N
"Note that we do not have the operation where all 100 ml's of soup B are used first. "
It's obvious that A is easier to be empty than B. And when N gets bigger, we have less chance to run out of B first.
So as N increases, our result increases and it gets closer to 100 percent = 1.

Answers within 10^-5 of the true value will be accepted as correct.
Now it's obvious that when N is big enough, result is close enough to 1 and we just need to return 1.
When I incresed the value of N, I find that:
When N = 4800, the result = 0.999994994426
When N = 4801, the result = 0.999995382315
So if N>= 4800, just return 1 and it will be enough.

Complexity Analysis
I have to say this conversion process is necessary.

The solution using hashmap may luckly get accepted.
Thanks to leetcode infrastructure,
every test cases will run in seperate instances.
(this can be easily tested).

In this case it's the same for space and time using hashmap.

But are you writing codes running only once?
How about the case running multiple test cases within the same instance?

Without this conversion,
it needs O(200 * 5000) time & space if A == B,
it needs O(5000 * 5000) time & space if A != B, (which sounds like 250mb)

But in our solution above, we use only O(200 * 200) time & space.
"""

"""
解题思路
虽然题目乍一看比较复杂，好像让你去算概率，难道是概率题，不是编程题？
但稍加分析，可以总结如下信息：
初始状态下，A和B同时拥有N的汤。
终结状态下，

若A先被倒完，则A剩余的汤为0或负数。（因为在剩余汤不足时，可以倒比所需少的量）此时B剩余的汤应当大于0。
若A和B同时倒完，则A和B的汤均为0或负数。
若B先被倒完，则B剩余的汤为0或负数。此时A剩余的汤应当大于0。
有了初始状态和终结状态，可以想到用递归的方法来求解。在结算时，因为同时倒完的概率只需计算一半。因此，判断其为A先倒完时，返回1，而同时倒完时返回0.5。
又考虑到所有操作中汤的份量都是25的倍数，实际中间状态的可能最多为Ceil(N/25)^2。因此可以用动态规划来避免冗余计算。

以上基本实现了本题的主体解法。然而这是一个两次方复杂度的解法，随着N的上升，需要指数的时间去计算。
此时我们可以利用题目中提到的精度要求来做文章。让我们从概率的角度重新审题。
四个操作对汤消耗的期望值为A = 62.5, B = 37.5。A的消耗速度远高于B。
因此，当N变大时，A先倒完的概率趋向于1。我们尝试不断递增的N来运行程序后，可以发现当N>4800时，
所得概率已经落在1 - 10^-6内。也就是说所有大于4800的输入，都可以直接输出1作为结果。
"""
import math

"""
Nice solution though! In Python version, if you use f(a-100, b) + f(a-75, b-25) + f(a-50, b-50) + f(a-25, b-75) 
in the recursion section, then you don't need this line N = math.ceil(N / 25.0). 
Also, the global dictionary memo can be within the scope of soupServings to be a local dictionary. Runtime 42ms.
"""

class SolutionLee:
    memo = {}
    def soupServings(self, N):
        if N > 4800: return 1
        def f(a, b):
            if (a, b) in self.memo: return self.memo[a, b]
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            self.memo[(a, b)] = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
            return self.memo[(a, b)]
        N = math.ceil(N / 25.0)
        return f(N, N)


class Solution1:
    def soupServings(self, N):

        if N >= 5551:
            return 1
        memo = {}

        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            if (a, b) in memo:
                return memo[a, b]
            ans = 0.0
            for da, db in ((-100, 0), (-75, -25), (-50, -50), (-25, -75)):
                ans += dfs(a + da, b + db)
            ans *= 0.25
            memo[a, b] = ans
            return ans

        return dfs(N, N)


class Solution2:
    def soupServings(self, N):
        visited = {}
        def dfs(a, b):
            if (a, b) in visited: return visited[(a, b)]
            elif a <= 0 or b <= 0: return (a < b and 1) or (a == b and 0.5) or (b < a and 0)
            visited[(a, b)] = 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b -50) + dfs(a - 25, b - 75))
            return visited[(a, b)]
        return N > 4800 and 1 or round(dfs(N, N), 5)


class Solution3:
    def soupServings(self, N):

        Q, R = divmod(N, 25)
        N = Q + (R > 0)
        if N >= 500: return 1
        serves=[(4,0),(3,1),(2,2),(1,3)]
        dp=[[0]*(N+1) for _ in range(N+1)]
        dp[N][N]=1
        for i in range(N,0,-1):
            for j in range(N,0,-1):
                for  ser in serves:
                    tem1=0 if i-ser[0]<=0 else i-ser[0]
                    tem2=0 if j-ser[1]<=0 else j-ser[1]
                    dp[tem1][tem2]+=dp[i][j]*0.25
        return sum([dp[0][i] for i in range(1,N+1)])+dp[0][0]*0.5


"""
题目大意：
有A，B两种汤。初始每种汤各有N毫升，现有4种操作：

1. A倒出100ml，B倒出0ml
2. A倒出75ml， B倒出25ml
3. A倒出50ml， B倒出50ml
4. A倒出25ml， B倒出75ml
每种操作的概率均等为0.25。如果汤的剩余容量不足完成某次操作，则有多少倒多少。当每一种汤都倒完时停止操作。

求A先倒完的概率，加上A和B同时倒完的概率。

解题思路：
记忆化搜索 + 特判

if A <= 0 and B <= 0: dp[A][B] = 0.5 

elif A <= 0: dp[A][B] = 1 

elif B <= 0: dp[A][B] = 0

else: dp[A][B] = 0.25 * (dp[A - 100][B] + dp[A - 75][B - 25] + dp[A - 50][B - 50] + dp[A - 25][B - 75])
当N >= 14000时，近似等于1，直接返回1即可
"""
class Solution4:
    def soupServings(self, N):

        self.memo = {}
        if N >= 14000: return 1.0
        return self.solve(N, N)
    def solve(self, A, B):
        if A <= 0 and B <= 0: return 0.5
        if A <= 0: return 1
        if B <= 0: return 0
        if (A, B) in self.memo:
            return self.memo[(A, B)]
        ans = 0.25 * (self.solve(A - 100, B) + self.solve(A - 75, B - 25) +
                      self.solve(A - 50, B - 50) + self.solve(A - 25, B - 75))
        self.memo[(A, B)] = ans
        return ans



"""
解题方法
这个题是个简单的记忆化搜索问题。

使用solve(A, B)函数表示当A, B分别是两者的数量的时候，A先倒完的概率，加上A和B同时倒完的概率*0.5。同时使用memo来保存这个结果。

if A <= 0 and B > 0: return 1 // A先倒完，结果是1
if A <= 0 and B <= 0: return 0.5 // A和B同时倒完，结果是题目设定的0.5
if A > 0 and B <= 0: return 0 // B先倒完，结果是0
1
2
3
由于四个操作发生的概率是相等的，所以，当A,B同时剩余的时候，其结果是4个操作获得概率的平均数。

另外就是题目给了提示，B没有每次倒100的情况，所以，A先倒完的概率更大。
当N很大的时候，我们会做很多次操作，最后肯定是A先结束。题目要求小数点后6位，所以当N > 5600 直接 return 1.0。

另外在测试中发现，如果把(A,B)是否在记忆化数组中放到所有判断的前面，速度会加快。

时间复杂度是O(N2)，空间复杂度是O(N2).
"""


class Solution5:
    def soupServings(self, N):

        self.memo = dict()
        if N > 5600: return 1.0
        return self.solve(N, N)

    def solve(self, A, B):
        if (A, B) in self.memo:
            return self.memo[(A, B)]
        if A <= 0 and B > 0: return 1
        if A <= 0 and B <= 0: return 0.5
        if A > 0 and B <= 0: return 0
        prob = 0.25 * (self.solve(A - 100, B) + self.solve(A - 75, B - 25)
                       + self.solve(A - 50, B - 50) + self.solve(A - 25, B - 75))
        self.memo[(A, B)] = prob
        return prob








