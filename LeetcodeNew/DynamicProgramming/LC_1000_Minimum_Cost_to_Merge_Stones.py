
"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile,
and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""
"""
Solution 1: 3D DP
Intuition
Seem that most of games, especially stone games, are solved by dp?

Explanation

dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.

Initial status dp[i][i][1] = 0 and dp[i][i][m] = infinity

dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j]
dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])

The origine python2 solution is a bit too long on the memorization part.
So I rewrote it in python3 with cache helper,
so it will be clear for logic.

Complexity
Time O(N^3/K), Space O(KN^2)
"""

class SolutionLee1:
    def mergeStones(self, stones, K):
        n = len(stones)
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
        res = dp(0, n - 1, 1)
        return res if res < inf else -1


"""

Solution 2: 2D DP
Explanation
Suggested by @yaoct, we can simplify the third parameter m in DP.

stones[i] ~ stones[j] will merge as much as possible.

Finally (j - i) % (K - 1) + 1 piles will be left.

It's less than K piles and no more merger happens.

dp[i][j] means the minimum cost needed to merge stones[i] ~ stones[j].

Complexity
Time O(N^3/K) Space O(N^2)
It can be improved, but I think it's fine now.

"""

class SolutionLee2:
    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)



"""

FAQ
Q: Why mid jump at step K - 1
A: We can merge K piles into one pile,
we can't merge K + 1 piles into one pile.
We can merge K + K - 1 piles into on pile,
We can merge K + (K - 1) * steps piles into one pile.


Update 2019-03-04
Sorry guys, It seems that somehow it started kind of debate in one of my replies.
I didn't mean to do that and I feel I have to say something.

Yes, I agree that people have right to express in their comfortable language, including Chinese.
It's not the same as the situation of a meeting room.
User don't take others' time and force them to listen to you.
Reader can choose what they want to read.
Like ebooker and trip adviser, they have comments in all languages.

I strongly disagree any unreasonable downvotes.
Posts and reply should not be downvoted for no reason like language.
Personally I receive downvotes for each of my posts.
Of course, people have right to do that but please at least say something or leave a message.
Like "I downvote for the reason that....", so that I can also improve somehow, right?

I encourage everyone to express in English and discuss with all others.
The main reason is that English is still one important skill for engineers.
We need to learn from documents in English.
Moreover, as a Chinese engineer, I hope I can bring the good stuff back to the world.

In the end, the most important, I encourage everyone to learn some Chinese :)
"""

"""
(i) Personally, this solution seems more a dfs with memorization than dp solution to me. Each (i, j, m) problem is dfs into (i, mid, 1) + (mid+1, j , m-1) . With no memorization, this will incur much repeated work. Thus we store each (i, j, k) which has been computed, into memo[][][]. Since the range of (i,j) shrinks when dfs goes on, the ending condition is the case when i == j.
(ii) The reason we need +stonesNumber[i][j] (the sum of stones from pile i to pile j) is that we need to merge piles together to 1 pile. This is done in the case when m = 1. Note that when m = 1, the last step must be merge K piles together. Thus we have res = dp(i,j,K) + prefix[j+1]-prefix[i]
(iii) The reason we can skip K-1 items when looping from i to j: Because we need to make sure when we split it into (i, mid,1) +(mid+1, j , m-1), the left half (i, mid, 1) can be resolved by merging K piles consecutively.
(iv) I think we can judge whether we should return -1 at the very beginning by checking if (n-1) % (K-1) == 0. If so, there must be a solution. Otherwise, no solution.


So the essence of +=K-1 is to make there's at least K piles at hand 
so that we can merge these K piles into 1 pile. I see. 
Previously I was wondering if we write as dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m-1]),
can we write like dp[i][j][m] = min(dp[i][mid][2] + dp[mid + 1][j][m-2]), 
dp[i][j][m] = min(dp[i][mid][3] + dp[mid + 1][j][m-3]) etc
"""
"""
My solution is based on Hvivi in python, I just implements it in C++.
https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247750/Python-DP-easy-to-understand

I use a 3 dimension matrix to record the statuses.
dp[i][j][k], it means the minimum cost to merge stones from position i(include) to position j(include) into k piles.
The initial state is dp[i][j][k] = 0 if j - i + 1 == k, otherwise, dp[i][j][k] = MAX_COST( aka. INFINIT).
Since we can only merge K continuous piles. The transition function is like this:
When k != 1:
dp[i][j][k] = min(dp[i][mid][1] + dp[mid+1][j][k-1]) , since we cannot do anything to merge the piles.
When k == 1:
dp[i][j][k] = min(dp[i][mid][1] + dp[mid+1][j][K-1] + stoneNumbers[i][j]), 
since we can merge K continuous piles into 1 pile, 
and the cost will be the total number of the stone between postion i and postion j.
"""

"""
Create prefix table. I used python "reduce" method. Same if using "for" loop. With prefix table, cost from i to j could be calculated in O(1) time.
Simply use dfs to loop through all possibilites merging between index i and j into m piles of stones.
"@functools.lrc_cache(None)" caches the execution result for (i,j,m) input, so that the complexity level could be largely reduced
"""
import functools
import math

class Solution1:
    def mergeStones(self, stones, K):
        p = functools.reduce(lambda s, x: s + [s[-1] + x], stones, [0])

        @functools.lru_cache(None)
        def dfs(i, j, m):
            if (j - i + 1 - m) % (K - 1): return math.inf
            if i == j: return 0 if m == 1 else math.inf
            if m == 1: return dfs(i, j, K) + p[j + 1] - p[i]
            return min(dfs(i, k, 1) + dfs(k + 1, j, m - 1) for k in range(i, j))

        res = dfs(0, len(stones) - 1, 1)
        return res if res != math.inf else -1


class Solution2:
    def mergeStones(self, stones, K):
        from functools import lru_cache
        @lru_cache(None)
        def dfs(l, r, pile):
            if pile == K and (r - l ) % (pile-1):
                return float('inf')
            if l == r:
                return 0
            if pile == 1:
                return dfs(l,r,K) + sum(stones[l:r+1])
            return min(dfs(l,i,1) + dfs(i+1, r, pile-1) for i in range(l, r))
        ans = dfs(0, len(stones)-1, 1)
        return -1 if ans == float('inf') else ans




