

"""
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.


Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.


Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.


Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".


Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".


Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
"""


import functools

class Solution:
    def encode(self, s: str) -> str:
        def compress(i, j):
            pattern = s[i:j + 1]
            pos = (pattern + pattern).find(pattern, 1)
            if pos >= len(pattern):
                return pattern
            return str(len(pattern) // pos) + '[' + str(dfs(i, i + pos - 1)) + ']'

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == j:
                return s[i]

            res = compress(i, j)
            for k in range(i, j):
                res = min(res, dfs(i, k) + dfs(k + 1, j), key=len)
            return res

        return dfs(0, len(s) - 1)




class SolutionOMG:
    def encode(self, s: str) -> str:
        memo = dict()

        def collapse(i, j):
            pattern = s[i:j + 1]
            pos = (pattern + pattern).find(pattern, 1)
            if pos >= len(pattern):
                return pattern
            # print(s, i, j+1, pattern, pos, len(pattern) // pos, ' -- ', i, i+pos-1, ' -- ', dfs(i, i + pos - 1), f'{len(pattern) // pos}[{dfs(i, i + pos - 1)}]')
            return f'{len(pattern) // pos}[{dfs(i, i + pos - 1)}]'

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == j:
                return s[i]

            arr = []
            for k in range(i, j):
                arr.append(dfs(i, k) + dfs(k + 1, j))
            # print(arr)
            res = min(arr, key=lambda x: len(x))
            memo[i, j] = min(res, collapse(i, j), key=lambda x: len(x))
            return memo[i, j]

        return dfs(0, len(s) - 1)




class Solution:
    def collapse(self, dp, s, i, j):
        temp = s[i:j + 1]
        pos = (temp + temp).find(temp, 1)
        if pos >= len(temp):
            return temp
        return str(len(temp) // pos) + '[' + dp[i][i + pos - 1] + ']'

    def encode(self, s):
        n = len(s)
        dp = [[''] * n for _ in range(n)]

        for step in range(1, n + 1):
            for i in range(0, n + 1 - step):
                j = i + step - 1
                dp[i][j] = s[i:j + 1]
                for k in range(i, j):
                    left, right = dp[i][k], dp[k + 1][j]
                    if len(left) + len(right) < len(dp[i][j]):
                        dp[i][j] = left + right

                replace = self.collapse(dp, s, i, j)
                if len(replace) < len(dp[i][j]):
                    dp[i][j] = replace

        return dp[0][n - 1]




# s = "aaaaaaaaaa"
s = "aabcaabcd"
a = SolutionOMG()
print(a.encode(s))

