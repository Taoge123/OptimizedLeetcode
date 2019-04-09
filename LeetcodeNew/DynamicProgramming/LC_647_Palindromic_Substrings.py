"""
https://blog.csdn.net/fuxuemingzhu/article/details/79433960
https://leetcode.com/problems/palindromic-substrings/discuss/138237/Manacher-detailed-explanation-(O(N)-without-unnecessary-expansion-attempt)

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

The input string length won't exceed 1000.
"""
"""
在刚开始的时候博主提到了自己写的DP的方法比较复杂，为什么呢，因为博主的dp[i][j]定义的是范围[i, j]之间的子字符串的个数，
这样我们其实还需要一个二维数组来记录子字符串[i, j]是否是回文串，
那么我们直接就将dp[i][j]定义成子字符串[i, j]是否是回文串就行了，然后我们i从n-1往0遍历，
j从i往n-1遍历，然后我们看s[i]和s[j]是否相等，这时候我们需要留意一下，有了s[i]和s[j]相等这个条件后，
i和j的位置关系很重要，如果i和j相等了，那么dp[i][j]肯定是true；如果i和j是相邻的，
那么dp[i][j]也是true；如果i和j中间只有一个字符，那么dp[i][j]还是true；
如果中间有多余一个字符存在，那么我们需要看dp[i+1][j-1]是否为true，若为true，那么dp[i][j]就是true。
赋值dp[i][j]后，如果其为true，结果res自增1
"""
class SolutionSlow:
    def countSubstrings(self, s):

        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    res += 1
        return res

class Solution1:
    class Solution(object):
        cnt = 0

        def countSubstrings(self, s):
            self.cnt = 0
            n = len(s)
            for i in range(n):
                self.palindromic(s, i, i)  # judge odd length string
                self.palindromic(s, i, i + 1)  # judge even length string
            return self.cnt

        def palindromic(self, s, left, right):  # judge if a substring is palindromic
            n = len(s)
            while (left >= 0 and right < n and s[left] == s[right]):
                self.cnt += 1
                left -= 1
                right += 1


"""
方法三：动态规划
动态规划的思想是，我们先确定所有的回文，即 string[start:end]是回文. 当我们要确定string[i:j] 是不是回文的时候，要确定：

string[i] 等于 string[j]吗?
string[i+1:j-1]是回文吗?
单个字符是回文；两个连续字符如果相等是回文；如果有3个以上的字符，需要两头相等并且去掉首尾之后依然是回文。
"""
"""
这个回文字符串的题母，千篇一律啊。在5. Longest Palindromic Substring中，当遇到回文字符串时，
我们是使用maxL记录下来最长的那个。稍微修改，这个题我们只要做统计个数就可以。因此代码基本一样
"""


class Solution2:
    def countSubstrings(self, s):

        n = len(s)
        count = 0
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count


class Solution3:
    def countSubstrings(self, s):

        count = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1): # step size
            for i in range(N - l + 1):
                j = i + l - 1
                if l == 1 or (l == 2 and s[i] == s[j]) or (l >= 3 and s[i] == s[j] and dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1


class Solution4:
    def countSubstrings(self, s):

        # Pre-processed for Manacher's Algorithm
        s = '#' + '#'.join(s) + '#'

        # Initialization
        m = [0] * len(s)
        maxRight = 0  # The most-right position ever touched by sub-strings
        pos = 0  # The center for the sub-string touching the maxRight
        maxLen = 0

        for idx in range(len(s)):
            # check for idx
            if idx < maxRight:
                m[idx] = min(m[2 * pos - idx], maxRight - idx)  # symmetric to pos
            else:
                m[idx] = 1  # previous sub-strings haven't go this far

            # expand with taking idx as center
            # pay attention to the boundary
            while idx - m[idx] >= 0 and idx + m[idx] < len(s) and s[idx - m[idx]] == s[idx + m[idx]]:
                m[idx] += 1

            # update maxRight and pos if needed
            if m[idx] + idx - 1 > maxRight:
                maxRight = m[idx] + idx - 1
                pos = idx

            # update maxLen
            maxLen = max(maxLen, m[idx])

        # maxLen-1 represents the real length in original string without '#'
        m = [x - 1 for x in m]
        return sum([(1 + x) // 2 for x in m])


"""
Algorithm

For each possible palindrome center, let's expand our candidate palindrome 
on the interval [left, right] as long as we can. 
The condition for expanding is left >= 0 and right < N and S[left] == S[right]. 
That means we want to count a new palindrome S[left], S[left+1], ..., S[right].
"""

class Solution5:
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans




"""
Approach #2: Manacher's Algorithm [Accepted]
Intuition

Manacher's algorithm is a textbook algorithm that finds in linear time, 
the maximum size palindrome for any possible palindrome center. 
If we had such an algorithm, finding the answer is straightforward.

What follows is a discussion of why this algorithm works.

Algorithm

Our loop invariants will be that center, right is our knowledge of the palindrome 
with the largest right-most boundary with center < i, centered at center with right-boundary right. 
Also, i > center, and we've already computed all Z[j]'s for j < i.

When i < right, we reflect i about center to be at some coordinate j = 2 * center - i. 
Then, limited to the interval with radius right - i and center i, 
the situation for Z[i] is the same as for Z[j].

For example, if at some time center = 7, right = 13, i = 10, 
then for a string like A = '@#A#B#A#A#B#A#'`, the `center` is at the `'#'` between the two middle `'A'`'s, 
the right boundary is at the last `'#'`, `i` is at the last `'B'`, and `j` is at the first `'B'`. 
Notice that limited to the interval `[center - (right - center), right]` 
(the interval with center `center` and right-boundary `right`), 
the situation for `i` and `j` is a reflection of something we have already computed. 
Since we already know `Z[j] = 3`, we can quickly find `Z[i] = min(right - i, Z[j]) = 3`. 
Now, why is this algorithm linear? The while loop only checks the condition 
more than once when `Z[i] = right - i`. In that case, for each time `Z[i] += 1`, 
it increments `right`, and `right` can only be incremented up to `2*N+2` times. 
Finally, we sum up `(v+1) / 2` for each `v in Z`. Say the longest palindrome with some given center C has radius R. 
Then, the substring with center C and radius R-1, R-2, R-3, ..., 0 are also palindromes. 
Example: `abcdedcba` is a palindrome with center `e`, radius 4: but `e`, `ded`, `cdedc`, `
bcdedcb`, and `abcdedcba` are all palindromes. 
We are dividing by 2 because we were using half-lengths instead of lengths. 
For example we actually had the palindrome `a#b#c#d#e#d#c#b#a`, so our length is twice as big.
"""

class Solution6:
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v + 1) / 2 for v in manachers(S))


