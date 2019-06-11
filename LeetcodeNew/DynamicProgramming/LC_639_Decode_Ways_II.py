
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*',
which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""

"""
思路一：

首先考虑：一位数字可以表示一个字母，比如1-A，两位字符也可以表示一个字母比如26-Z。那么根据是1个或者2个字符表示1个字母很快可以想到一个DFS的思路。

      对于每个大于2个字符的字符串S[n]，我们可以把它分解成两种情况：

     1. 前面n-2个字符的子串 和 最后两个字符的子串。

    2. 前面n-1个字符的子串 和 最后一个字符的子串。

    如果用nums()表示A-Z字符串可以匹配的个数，我们可以得到 

nums(S[1..n]) = nums(S[1...n-2] ) * nums(S[n-1，n])  +  nums(S[1...n-1] ) * nums(S[n]) .

    DFS 终止条件为：当要找的字符串长度小于3的时候，我们通过单独的分析一一列举出来。


思路二：

当一个题目可以被DFS搞定，接下来我们就得找找有没有对应的DP算法了。
通过上文我们知道。S[1..n] 总是可以由 S[1...n-1] + S[1....n-2]推导出来。无非是多了个系数：
中间再加上长度为1和2的字符串单独分析过程。Bingo，这不就是变形版的fibonacci数列问题吗！！

"""

"""
We can decode the string either from the begining or from the end. No matter which way, the last decode piece is either with length 1 or 2. If we start from the end and let dp[i] := number of ways to decode s[i:]. Then the general recursion relation is

dp[i] = factor(s[i]) * dp[i+1] + factor(s[i:i+2]) * dp[i+2], and we want to find dp[0]

where the factors can be checked from the hashtables below depending on the length of the last decoding piece:
factor_1 = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
factor_2 = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1, '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2, '*6': 2,'*7': 1, '8': 1, '9': 1, '1': 9, '2': 6, '**': 15}.

If we start from the beginning and let dp[i]:= number of ways to decode s[:i], the general recursion relation is

dp[i] = factor(s[i]) * dp[i-1] + factor(s[i-1:i+1]) * dp[i-2], and we want to find dp[-1]

code snippet 1 (decode from end to beginning):
"""
last_piece_length_1 = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
last_piece_length_2 = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1, '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2, '*6': 2,'*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = (1, 1)
        for i in range(len(s)-1, -1, -1):
            dp = ((last_piece_length_1.get(s[i], 0)*dp[0] + last_piece_length_2.get(s[i:i+2], 0)*dp[1])%(10**9 + 7), dp[0])
        return dp[0]

# code snippet 1_brute_force_DP:
class Solution1:
    def numDecodings(self, s):

        dp = [1]*(len(s)+2)
        for i in range(len(s)-1, -1, -1):
            dp[i] = (last_piece_length_1.get(s[i], 0)*dp[i+1] + last_piece_length_2.get(s[i:i+2], 0)*dp[i+2])%(10**9 + 7)
        return dp[0]



# code snippet 2 (decode from beginning to end):
class Solution11:
    def numDecodings(self, s):

        dp = (1, 1)
        for i in range(len(s)):
            dp = (dp[1], (last_piece_length_1.get(s[i], 0)*dp[1] + last_piece_length_2.get(s[i-1:i+1], 0)*dp[0])%(10**9 + 7))
        return dp[1]

# code snippet 2_brute_force_DP:
class Solution111:
    def numDecodings(self, s):

        dp = [1]*(len(s)+2)
        for i in range(2, len(s)+2):
            dp[i] = (last_piece_length_1.get(s[i-2], 0)*dp[i-1] + last_piece_length_2.get(s[i-2-1:i-2+1], 0)*dp[i-2])%(10**9 + 7)
        return dp[-1]


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






