
"""

https://leetcode-cn.com/problems/decode-ways-ii/solution/jie-ma-fang-fa-2-by-leetcode/


XXXXX 1 1
dp[i] = dp[i-1] * 1
dp[i] = dp[i-2] * 1

XXXX 1 *
dp[i] += dp[i-1] * 9
dp[i] += dp[i-2] * 9
dp[i] += dp[i-2] * 15





12 - AB, L


"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        else:
            if s[0] == '0':
                dp[1] = 0
            else:
                dp[1] = 1

        for i in range(1, n):
            if s[i] == '*':
                dp[i + 1] = 9 * dp[i]
                if s[i - 1] == '1':
                    dp[i + 1] += dp[i - 1] * 9
                elif s[i - 1] == '2':
                    dp[i + 1] += dp[i - 1] * 6
                elif s[i - 1] == '*':
                    dp[i + 1] += dp[i - 1] * 15
            else:
                if s[i] != '0':
                    dp[i + 1] = dp[i]
                else:
                    dp[i + 1] = 0

                if s[i - 1] == '1':
                    dp[i + 1] += dp[i - 1]
                elif s[i - 1] == '2' and s[i] <= '6':
                    dp[i + 1] += dp[i - 1]
                elif s[i - 1] == '*':
                    if s[i] <= '6':
                        dp[i + 1] += dp[i - 1] * 2
                    else:
                        dp[i + 1] += dp[i - 1] * 1

        return dp[-1] % mod


"""
解题思路：解码有多少种方法。一般求“多少”我们考虑使用dp。状态方程如下：

　　　　　当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]

　　　　　当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]

　　　　   当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。

　　　　   注意初始化时：dp[0]=1,dp[1]=1
"""
class Solution2:
    def numDecodings(self, s):
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]







