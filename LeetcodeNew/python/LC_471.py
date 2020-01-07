

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






