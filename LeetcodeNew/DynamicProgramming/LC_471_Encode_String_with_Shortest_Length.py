
"""
https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95621/Python-solution-with-detailed-explanation
https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95601/Rigorous-proof%3A-Why-condition-%22(s%2Bs).find(s1)-less-s.size()%22-is-equivalent-to-substring-repetition

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters.
The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it.
If there are several solutions, return any of them is fine.


Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string,
so we do not encode it.


Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.

Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions,
both of them have the same length = 5, which is the same as "10[a]".


Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".


Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c",
so one answer can be "2[2[abbb]c]".
"""

"""
题解：
dp[i][j] = string from index i to index j in encoded form.
We can write the following formula as:-
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]) or if we can find some pattern in string from i to j which will result in more less length.
Time Complexity = O(n^3)
"""
"""
Either don't encode s at all, or encode it as one part k[...] or encode it as multiple parts
(in which case we can somewhere split it into two subproblems). Whatever is shortest. 
Uses @rsrs3's nice trick of searching s in s + s.
"""

class SolutionStefan:
    def encode(self, s, memo={}):
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1)
            one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
            memo[s] = min([s, one] + multi, key=len)
        return memo[s]


class SolutionBest:
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


"""
Even though many of us use the following smart condition in code to check for substring repetition, I didn't see a rigorous proof. So here is one.

Why condition (s+s).find(s,1) < s.size() is equivalent to substring repetition?

Proof: Let N = s.size() and L := (s+s).find(s,1), actually we can prove that the following 2 statements are equivalent:

1. 0 < L < N;
2. N%L == 0 and s[i] == s[i%L] is true for any i in [0, N). (which means s.substr(0,L) is the repetitive substring)
Consider function char f(int i) { return s[i%N]; }, obviously it has a period N.

"1 => 2": From condition 1, we have for any i in [0,N)

- s[i] == (s+s)[i+L] == s[(i+L)%N],
which means L is also a positive period of function f. Note that N == L*(N/L)+N%L, so we have
- f(i) == f(i+N) == f(i+L*(N/L)+N%L) == f(i+N%L),
which means N%L is also a period of f. Note that N%L < L but L := (s+s).find(s,1) is the minimum positive period of function f, 
so we must have N%L == 0. Note that i == L*(i/L)+i%L, so we have
- s[i] == f(i) == f(L*(i/L)+i%L) == f(i%L) == s[i%L],
so condition 2 is obtained.
"2=>1": If condition 2 holds, for any i in [0,N), note that N%L == 0, we have

- (s+s)[i+L] == s[(i+L)%N] == s[((i+L)%N)%L] == s[(i+L)%L] == s[i],
which means (s+s).substr(L,N) == s, so condition 1 is obtained.
"""

"""
Just borrow your idea.
Why condition (s+s).find(s,1) < s.size() is equivalent to substring repetition?

Assume index of string starts from 0. Let s be a non-empty string with size N >= 1,
with minimum period L(or smallest L that satifiess == s[0:L-1] * (N/L) ), where 0 < L <= N.
Consider an endless string f where f[i] = s[i%N], the minimum period of f is also L (We prove this formally in the appendix).
Let L1 = (s+s).find(s,1).
Claim: L1 == L.
Proof:

L1 >= L: From the computation of L1 we know that s[i] == (s+s)[(i+L1)%N] == s[(i+L1)%N]. Clearly L1 should be a period of f, that means L1 >= L
L1 <= L: Start from the definition of f and L, we know s must reappear in f at position L, 
that is f[0:N-1] == f[L:L+N-1], which means L1 <= L because L1 is the first position where we find s.
By showing L1 >= L and L1 <= L, the claim is proved.

Appendix:
Prove by contradiction.
Since L is already a period, the minimum period of f should be less than(1/2, 1/3, ...) or equal(1/1) to L, 
the period of s. If it is smaller that L, say there exist k >= 2 that (1/k) * L is the minimum period of f, then (1/k) * L is also a period of s. 
This leads to (1/k) * L >= L, contradiction occurs!
"""

"""
Memoization: Time: O(N^3)

String based problem can be broken down into smaller sized problem involving sub-strings of the larger string.
For memoization, we generally parameterize a subtring as s(i,j). For DP, we can parameterize it in terms of substrings of length 1, 2, 3, ..., L.
Given a substring s(i,j), we have three choices for finding minimum encoding:
X = Do not encode s(i,j)
Y = Find all repeating patterns and encodings and then choose the minimum length encoding. Length of repeating pattern ranges from N//2 to 1.
Z = Split s(i,j) into two substrings left and right. s(i,k) and s(k+1,j). If left and right are same, 
then we have another candidate "2[left]". Now k ranges from i to j-1. Finally choose the minimun length encoding from all these possibilities.
s(i,j) = min(X, Y, Z, key=len)
Note: we use min method in Python to find the shortest string based on length.
Time Complexity: O(N^3) - There are N^2 sub-problems and every sub-problem can be solved in O(N).
Space Complexity: O(N^2)

"""

class Solution2:
    def find_repeating_pattern(self, s):
        N = len(s)
        min_so_far = s
        for i in range(N // 2, 0, -1):
            if N % i == 0:
                if self.test(i, s):
                    cnt, pattern = N // i, s[0:i]
                    min_so_far = min("%d[%s]" % (cnt, pattern), min_so_far, key=len) if cnt > 0 else min_so_far
        return min_so_far

    def test(self, i, s):
        pattern = s[0:i]
        for j in range(i, len(s) - i + 1, i):
            match = s[j:j + i]
            if pattern != match:
                return False
        return True

    def helper(self, s, i, j, cache):
        if j < i:
            return ""
        elif i == j:
            return s[i]
        elif i in cache and j in cache[i]:
            return cache[i][j]
        else:
            cache.setdefault(i, {})[j] = self.find_repeating_pattern(s[i:j + 1])
            for k in range(i, j):
                left, right = self.helper(s, i, k, cache), self.helper(s, k + 1, j, cache)
                if left == right:
                    cache[i][j] = min(cache[i][j], left + right, "2[%s]" % (left), key=len)
                else:
                    cache[i][j] = min(cache[i][j], left + right, key=len)
            return cache[i][j]

    def encode(self, s):

        cache = {}
        return self.helper(s, 0, len(s) - 1, cache)


"""
In each recursion, you find the last partition that will give you the minimized encoded length just like burst ballon.

For time complexity, the first step is to count how many subproblems generated by the recursion. 
The answer is O(n^2) because you just find all different s[start - end] which is O(n^2). 
For each subproblem, it takes you at most O(n) time to find repeated substring and do string concatenation. 
Thus, the worst time complexity is O(n^3)."""
class Solution3:
    def encode(self, s, dp = {}):

        if len(s) <= 4:
            return s
        elif s in dp:
            return dp[s]
        dp[s] = s
        idx = (2 * s).find(s, 1)
        if 0 <= idx < len(s):
            dp[s] = str(len(s) / idx) + "[" + self.encode(s[:idx], dp) + "]"
        for i in range(1, len(s)):
            left = self.encode(s[:i], dp)
            right = self.encode(s[i:], dp)
            if len(left) + len(right) < len(dp[s]):
                dp[s] = left + right
        return dp[s]


"""
题目大意：
给定一个非空字符串，将其编码使得编码长度最短。

编码规则为 k[encoded_string]， 其中中括号内的字符串encoded_string 重复k次

注意：

k是正整数，编码字符串不会为空或者包含额外的空白字符
你可以假设字符串只包含小写英文字母。字符串长度最多160
如果编码不能使字符串变短，就不要编码。如果答案不唯一，任意返回其一即可
解题思路：
记忆化搜索

利用字典dp记录字符串的最优编码串

枚举分隔点p， 将字符串拆解为left, right左右两部分

尝试将left调用solve函数进行编码压缩，并对right递归调用encode函数进行搜索

将left和right组合的最短字符串返回，并更新dp
"""
class Solution4:
    def __init__(self):
        self.dp = dict()

    def encode(self, s):

        size = len(s)
        if size <= 1: return s
        if s in self.dp: return self.dp[s]
        ans = s
        for p in range(1, size + 1):
            left, right = s[:p], s[p:]
            t = self.solve(left) + self.encode(right)
            if len(t) < len(ans): ans = t
        self.dp[s] = ans
        return ans

    def solve(self, s):
        ans = s
        size = len(s)
        for x in range(1, size // 2 + 1):
            if size % x or s[:x] * (size / x) != s: continue
            y = str(size / x) + '[' + self.encode(s[:x]) + ']'
            if len(y) < len(ans): ans = y
        return ans


"""
思路：

这道题还是应该用动态规划来做。我们建立一个二维的DP数组，其中dp[i][j]表示s在[i, j]范围内的字符串的缩写形式(如果缩写形式长度大于子字符串，
那么还是保留子字符串)，那么如果s字符串的长度是n，最终我们需要的结果就保存在dp[0][n-1]中，然后我们需要遍历s的所有子字符串，
对于任意一段子字符串[i, j]，我们我们以中间任意位置k来拆分成两段，比较dp[i][k]加上dp[k+1][j]的总长度和dp[i][j]的长度，
将长度较小的字符串赋给dp[i][j]，然后我们要做的就是在s中取出[i, j]范围内的子字符串t进行合并。
合并的方法是我们在取出的字符串t后面再加上一个t，然后在这里面寻找子字符串t的第二个起始位置，如果第二个起始位置小于t的长度的话，
说明t包含重复字符串，举个例子吧，比如 t = "abab", 那么t+t = "abababab"，我们在里面找第二个t出现的位置为2，小于t的长度4，
说明t中有重复出现，重复的个数为t.size()/pos = 2个，那么我们就要把重复的地方放入中括号中，注意中括号里不能直接放这个子字符串，
而是应该从dp中取出对应位置的字符串，因为重复的部分有可能已经写成缩写形式了，比如题目中的例子5。如果t = "abc"，
那么t+t = "abcabc"，我们在里面找第二个t出现的位置为3，等于t的长度3，说明t中没有重复出现，那么replace就还是t。
然后我们比较我们得到的replace和dp[i][j]中的字符串长度，把长度较小的赋给dp[i][j]即可，时间复杂度为O(n3)，空间复杂度为O(n2)。
"""
"""
dpi表示s[i, j]最短的压缩结果，subproblem里面枚举切分点k，分别得到dpi和dpk+1求和，找到长度最短的。

这道题关键是找sub = abcabc这种可压缩的情况，其中sub = s[i,j]。方法比较巧妙，用sub+sub = abcabcabcabc，
找第二个s在s+s里出现的位置，如果不是len(sub)，则说明sub有重复，那么就要压缩这个sub，
重复次数是len(sub) / indexOf(sub, 1)，重复的string用的是之前压缩过的dpi，index = indexOf(sub, 1)。
"""

"""
DP, 这个字符串编码的可能性有很多种，所以DP的方式就是对于每一种可能都求出一个结果最后得到最短的那个。

DP{i, j}代表编码后的s.substring(i, j+1). DP的过程中要注意每一个子串都具有编码和不编码的可能性，
对于substring的重复情况，重复的部分也可能被编码。

递推式：DP{i, j} = arg minLength(s.substring(i, j), DP{i, k}+DP{k+1, j}, after coding repeat.s.substring})
"""

s = "abbbabbbcabbbabbbc"

a = SolutionBest()
print(a.encode(s))


