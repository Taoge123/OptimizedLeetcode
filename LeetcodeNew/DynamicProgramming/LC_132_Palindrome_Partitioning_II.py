
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

"""
Calculate and maintain 2 DP states:

pal[i][j] , which is whether s[i..j] forms a pal

d[i], which
is the minCut for s[i..n-1]

Once we comes to a pal[i][j]==true:

if j==n-1, the string s[i..n-1] is a Pal, minCut is 0, d[i]=0;
else: the current cut num (first cut s[i..j] and then cut the rest
s[j+1...n-1]) is 1+d[j+1], compare it to the exisiting minCut num
d[i], repalce if smaller.
d[0] is the answer.
"""
class Solution1:
    def minCut(self, s):
        pal = [[False for _ in range(len(s))] for _ in range(len(s))]
        cuts = [len(s)-i-1 for i in range(len(s))]
        for start in range(len(s)-1,-1,-1):
            for end in range(start, len(s)):
                if s[start] == s[end] and (end-start < 2 or pal[start+1][end-1]):
                    pal[start][end] = True
                    if end == len(s)-1:
                        cuts[start] = 0
                    else:
                        cuts[start] = min(cuts[start], 1+cuts[end+1])
        return cuts[0]


"""
Algorithm (460 ms) credits go to:
https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space

The main algorithm idea is if s[i,j] is a palindrome, then the minCut(s[:j]) is at most minCut(s[:i-1])+1. 
This literally needs to find out all possible palindromes in the list. 
The above post provides an efficient search algorithm. O(n) space and O(n^2) time complexity.

Further acceleration (460 ms -> 56 ms) credits go to:
https://leetcode.com/discuss/43950/python-100ms-extra-dealing-super-cases-reduces-576ms-100ms

The main idea for acceleration is to quickly check and exclude a few long palindrome tests..
"""

class Solution2:
    def minCut(self, s):
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1, len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            # even palindrome
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2 + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]


# The following code simply implements the algorithm without any optimization (1800 ms),
# and should be easier to understand. O(n) space and O(n^3) time complexity.
def minCut(self, s):
    cut = [x for x in range(-1,len(s))]
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            if s[i:j] == s[j:i:-1]:
                cut[j+1] = min(cut[j+1],cut[i]+1)
    return cut[-1]


"""
The main method that uses double dp is nothing novel.
However, if I add a few more lines at the beginning to avoid the long cases in which mincut = 0 
or mincut = 1, the time cost optimized so dramatically that I got really surprised...
"""
class SolutionTony:
    def minCut(self, s: str) -> int:

        if s == s[::-1]: return 0
        n = len(s)
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        isPal = [[False] * (i + 1) for i in range(n)]
        dp = [i for i in range(n)] + [-1]
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or isPal[i - 1][j + 1]):
                    isPal[i][j] = True
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        return dp[n - 1]


a = SolutionTony()
print(a.minCut("leet"))


