
"""
https://leetcode.com/problems/k-inverse-pairs-array/solution/

Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation:
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation:
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Note:

The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""
"""
For a better understanding, I would use O(n * k ) space instead of O(k) space. It's easy to write O(k) space version when you understand this DP process.
As @awice said in his Post

For example, if we have some permutation of 1...4

5 x x x x creates 4 new inverse pairs
x 5 x x x creates 3 new inverse pairs
...
x x x x 5 creates 0 new inverse pairs
O(n * k ^ 2) Solution
We can use this formula to solve this problem

dp[i][j] //represent the number of permutations of (1...n) with k inverse pairs.
dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j-2] + ..... +dp[i-1][j - i + 1]
So, We write a O(k*n^2) Solution through above formula like this

But the above solution is too slow, it spends 1000+ms

O(n * l) Solution
Look back to the above formula.

dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j-2] + ..... +dp[i-1][j - i + 1]
Let's consider this example
if i = 5

dp[i][0] = dp[i-1][0] (creates 0 inverse pair)
dp[i][1] = dp[i-1][0] (1) + dp[i-1][1] (0)  =  dp[i][0] + dp[i-1][1]
dp[i][2] = dp[i-1][0] (2) + dp[i-1][1] (1) + dp[i-1][2] (0) = dp[i][1] + dp[i-1][2]
.
.
.
dp[i][4] = dp[i-1][0] (4) + dp[i-1][1] (3) + dp[i-1][2] (2) + dp[i-1][3] (1) + dp[i-1][4] (0)  = dp[i][3] + dp[i-1][4]
Can you find the rules about above formula.
if j < i , we can compute dp[i][j] = dp[i][j-1] +dp[i-1][j]

So, how about j >= i
We know if we add number i into permutation(0 .. i -1 ), i can create 0 ~i -1 inverse pair
If j >= i , we still use dp[i][j] = dp[i][j-1] +dp[i-1][j].
We must minus dp[i][j-i]. (In fact it minusdp[i-1][j-i], because everyj >= iin dp vecor,it minus dp[i-1][j-i]individually)
For example, if i = 5

dp[i][5] = dp[i][4] + dp[i-1][5] - dp[i-1][0]
dp[i][6] = dp[i][5] + dp[i-1][6] - dp[i-1][1]


"""

"""
Let's try for a top-down dp. Suppose we know dp[n][k], the number of permutations of (1...n) with k inverse pairs.

Looking at a potential recursion for dp[n+1][k], depending on where we put the element (n+1) in our permutation, we may add 0, 1, 2, ..., n new inverse pairs. For example, if we have some permutation of 1...4, then:

5 x x x x creates 4 new inverse pairs
x 5 x x x creates 3 new inverse pairs
...
x x x x 5 creates 0 new inverse pairs
where in the above I'm representing any permutation of 1...4 with x's.
Thus, dp[n+1][k] = sum_{x=0..n} dp[n][k-x].

This dp has NK states with K/2 work, which isn't fast enough. We need to optimize further.

Let ds[n][k] = sum_{x=0..k-1} dp[n][x].
Then dp[n+1][k] = ds[n][k+1] - ds[n][k-n],
and the left hand side is ds[n+1][k+1] - ds[n+1][k].
Thus, we can perform all calculations in terms of ds.

Finally, to save space, we will only store the two most recent rows of ds, using ds and new.

In the code, we refer to -ds[n][k-n+1] instead of -ds[n][k-n] because the n being considered is actually n+1. For example, when n=2, we are appending information about ds[2][k] to new, so our formula of dp[n+1][k] = ds[n][k+1] - ds[n][k-n] is dp[2][k] = ds[1][k+1] - ds[1][k-1].
"""

class Solution1:
    def kInversePairs(self, N, K):
        MOD = 10 ** 9 + 7
        ds = [0] + [1] * (K + 1)
        for n in xrange(2, N + 1):
            new = [0]
            for k in xrange(K + 1):
                v = ds[k + 1]
                v -= ds[k - n + 1] if k >= n else 0
                new.append((new[-1] + v) % MOD)
            ds = new
        return (ds[K + 1] - ds[K]) % MOD

"""
f(n,k) = sum(f(n-1,i)), where max(k-n+1,0) <= i <= k
f(0,k) = 0
f(n,0) = 1


My understanding of the solution:
Say f(n,k) is the number of arrays with n numbers and k reversed pairs.
Given [0,1,2...n-1], what would be the first number? The first number should range from 0 to n-1.
When it's 0, the problem f(n,k) is reduced to f(n-1, k), because the first number 0 causes no reversed pair.
When it's n-1, the problem f(n,k) is reduced to f(n-1, k-(n-1)), because [0,1,2,...,n-2] must be somewhere behind the leftmost n-1.
Consider all possible candidates as the first number, we have f(n,k) = sum( f(n-1,j) ) for max(k-(n-1),0)<=j<=k
The corner case is trivial: f(0,k) = 0 and f(n,0) = 1
The first j iteration (the line #n=4a) accumulates the dp[k] = sum( f(n-1,j) ) for 0<=j<=k
and the second j iteration (the line #n=4b) removes sum( f(n-1,j) ) for 0<=j<max(k-(n-1),0) from dp[k]

             
  # f(k) = # f[0] f[1] f[2] f[3] f[4] f[5] f[6] f[7]
  # n=0   #   0    0    0    0    0    0    0    0    
  # n=1   #   1    0    0    0    0    0    0    0
  # n=2   #   1    1    0    0    0    0    0    0
  # n=3   #   1    2    2    1    0    0    0    0  
  # n=4a  #   1*   3^   5'   6    6*   6^   6'   6      # we accumulate the last row from 0 to current k
  # n=4b  #   1    3    5    6    5    3    1    0      # then we subtract the sum from 0 to k-n
  
"""

class Solution2:
    def kInversePairs(self, n, k):
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1): dp[j] += dp[j - 1]
            for j in range(k, 0, -1): dp[j] -= j - i >= 0 and dp[j - i]
        return dp[k] % (10 ** 9 + 7)


"""
Idea:
You can write down some the cases from 1 to 4 and you will find the pattern.
Like when i = 4, you insert 4 to all the cases in a proper position when i = 3 to get the number of results when i=4.
Note that i limits the number of places you can do the insertion. If i = 5, there is only 5 places you can insert.
So you start from i = 0 as base case and you can get the final result at the end.

This is what we get from the above conclusion.

dp[i][j] = dp[i-1][j - i + 1] + dp[i-1][j - i + 2] + ... + dp[i-1][j]

But if you want to get your solution accepted in Python, then you need more optimization (BTW: I think is unfair since C++'s solution can pass it).
Actually, the above formula does have lots of redundant computation. As you can see, fordp[i][j]anddp[i][j-1], we may use dp[i-1][j-1], dp[i-1][j-2],...,dp[i-1][j-i+1]twice. Thus, I rewrite the formula as follows.

dp[i][j] = dp[i][j-1] + dp[i-1][j] - (if j - i >= 0: dp[i-1][j-i] else: 0)

It works like a sliding window, adding dp[i-1][j]to dp[i][j-1] and then reducing dp[i-1][j-i] if applicable to remain a sliding window whose size is i.

O(nk) space solution
"""
class Solution3:
    def kInversePairs(self, n, k):

        MOD = 10**9 + 7
        upper = n * (n - 1) / 2
        if k == 0 or k == upper:
            return 1
        if k > upper:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(k + 1):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
                if j - i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + MOD) % MOD
        return dp[n][k]

# O(k) space solution

class Solution33:
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        upper = n * (n - 1) / 2
        if k == 0 or k == upper:
            return 1
        if k > upper:
            return 0
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            temp =[1] + [0] * k
            for j in range(k + 1):
                temp[j] = (temp[j-1] + dp[j]) % MOD
                if j - i >= 0:
                    temp[j] = (temp[j] - dp[j - i]) % MOD
            dp = temp
        return dp[k]



class Solution4:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0]*(k+1)
        dp[0] = 1
        for I in range(2, n+1):
            curr = [0]*(k+1)
            #--------------------------------------------------
            # This is more intuitive, but more expensive
            # for j in range(1, min(I, k+1)):
            #     for m in range(j, k+1):
            #         curr[m] += dp[m-j]
            #--------------------------------------------------
            # Translated to the more efficient code below
            t = 0
            j = 1
            for m in range(1, k+1):
                t += dp[m-1]
                curr[m] = t
                if j+1 < min(I, k + 1):
                    j += 1
                else:
                    t -= dp[m-j] # only keep the top j items
            for i in range(1, k + 1):
                dp[i] += curr[i]

