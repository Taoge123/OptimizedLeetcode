
"""
https://leetcode.com/problems/decode-ways/discuss/132163/Python-7-lines-DP-solution-w-explanation-44-ms-beats-96

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

"""
This is like a Fibonacci sequence solution.
First digit will start with variance(res[1]) 1 and we add imaginary variance 1(res[0]) for the proper construction of Fibonacci sequence.

Current digit analysis:
1. Integer(previos digit + current digit) == 0 or more than 26: (Return 0)
   We can't pass this number in the sequence as it always be False to continue. For example:
   "1212100121" => "121210" and "0121", "12121" and "00121"
   "1212401211" => "121240" and "1211" , "12124" and "01211" (No leading zero)

2. Integer(previos digit + current digit) > 26:
   We can't make this two digit number so the last variance stays the same and current digit left for calculation to next digit.

3. 10 <= Integer(previos digit + current digit) <= 26
   This is the tricky Fibonacci part.
   3.1) If current digit > 0, we can treat current digit as added number to sequence. 
   In this case, last variance (res[-1]) will not change as all the variations will have added number in the end.
   3.2 ) Or we can add Integer(previos digit + current digit) to sequence. In this case, 
   last variance(res[-2]) wiil not change as all the variations will have added number in the end.

Solution:
"""

class Solution1:

    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]


class Solution2:
    def numDecodings(self, s):
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0

        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]
            if s[i - 2:i][0] != '0' and int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]


class Solution3:
    def numDecodings(self, s):
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if len(s[i - 2:i]) == 2 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]


class SolutionPrev:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        prev, curr = 1, 1  # prev = s[i-2], curr = s[i-1], initialized to 1
        for i in range(1, len(s)):
            # letter 0 is not allowed, set curr to 0
            if s[i] == '0':
                curr = 0
            # two letters case
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                tmp = curr
                curr += prev  # curr is the sum of curr and prev
                prev = tmp  # old curr
            # one letter case, so no change
            else:
                prev = curr  # no change
        return curr







