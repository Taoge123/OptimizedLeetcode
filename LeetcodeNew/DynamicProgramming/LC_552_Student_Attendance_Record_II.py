
"""
Given a positive integer n, return the number of all possible attendance records with length n,
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note: The value of n won't exceed 100,000.
"""
"""
dp[i]the number of all possible attendance (without 'A') records with length i :

end with "P": dp[i-1]
end with "PL": dp[i-2]
end with "PLL": dp[i-3]
end with "LLL": is not allowed
so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

the number of all possible attendance (with 'A') records with length n:
∑dp[i] *dp[n-1-i] i = 0,1,...,n-1

Time Complexity O(n)
Space Complexity O(n)

(In code nums[i+1] means dp[i])

dp[i] = dp[i].[end with 'P'] + dp[i].[end with 'PL'] + dp[i].[end with 'PLL'] + dp[i].[end with 'LLL']

dp[i-1] is the number of all possible attendance (without 'A') records with length i-1.
For each one it can push_back a 'P'(still valid) to get a record whose length is i.

For each record ending with 'P' whose length is i, we can pop_back 'P' to get a record (still valid) whose length is 'i-1'.

So, dp[i-1] = dp[i].[ends with 'P']

It doesn't mean dp[i-1] = dp[i-1].[ends with 'P']

"""
class Solution1:
    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result


"""
At time t where every report is length t, Let a, b, c be sequence types 
without an 'A' ending in N, NL, LL; and d,e,f be sequence types with an 'A' ending in N, NL, LL. 
(Here, N will denote a non-'L' character.) These types are disjoint, 
and exhaustive (their union is the set of all valid reports.) At the beginning when t = 1, a = b = d = 1 and we should compute N-1 more steps.

From a sequence of type a, b, c, we can write an 'A' to give us a sequence of type d, or a 'P' to give us a sequence of type a. 
From a sequence of type d, e, f, we can write a 'P' to give us a sequence of type d. 
From a sequence of type a, b, d, e, we can write an 'L' to give a sequence of (respectively) b, c, e, f. 
These are all the letters we could write in any situation. Working backwards, we can get the sums for a,b,c,d,e,f written below.
"""

class Solution2:
    def checkRecord(self, N):
        MOD = 10 ** 9 + 7
        a = b = d = 1
        c = e = f = 0
        for _ in xrange(N - 1):
            a, b, c, d, e, f = (a + b + c) % MOD, a, b, (a + b + c + d + e + f) % MOD, d, e

        return (a + b + c + d + e + f) % MOD


"""
Recurrence formula:
Let Q(n) be the solution of the the question, namely the number of all rewardable records.
Let R(n) be the number of all rewardable records without A.

Thinking the problem as replacing Ps and As on an array of Ls instead. Since the constraint is no more than 3 continuous Ls is allowed. For a n-size array, let's just look into the first 3 places, since there must be at least on replacement been taken place there:

First, let's consider the case we replacing with P. There're 3 cases:

P??: meaning we replace the first L with P. Doing so will shrink the problem size by one, so the number of this case is Q(n-1);
LP?: meaning we replace the second L with P. The first place got to be L since the case where P in the first place is being considered above. So the number of this case is Q(n-2);
LLP: meaning we replace the third L with P. Leaving us the number of Q(n-3);
Now let's consider the case we replacing with A:

A??: This we narrow down the problem size by one, and for the rest places there must be no As. So the number is R(n-1);
LA?: this will be R(n-2);
LLA: this will be R(n-3);
It's easy to see that the recurrence formula of R is just similar to the first 3 cases combined, namely:
R(n) = R(n-1) + R(n-2) + R(n-3)

So the recurrence formula of Q is:

Q(n) = Q(n-1) + Q(n-2) + Q(n-3) + R(n-1) + R(n-2) + R(n-3)
     = Q(n-1) + Q(n-2) + Q(n-3) + R(n)
"""



from collections import deque

class Solution3:
    def checkRecord(self, n):
        MOD = 1000000007
        withA = deque([1, 3, 8])
        withoutA = deque([1, 2, 4])
        if n < 3:
            return withA[n]
        for i in range(3, n+1):
            withoutA.append(sum(withoutA) % MOD)
            withA.append((sum(withA) + withoutA[-1]) % MOD)
            withoutA.popleft()
            withA.popleft()
        return withA[-1]


