
"""
https://leetcode.com/problems/longest-palindromic-substring/solution/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class SolutionCaikehe:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]


class Solution1:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            odd = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i + 1)

            res = max(res, odd, even, key=len)
        return res

    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


"""
Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2, 
and that new maxPalindrome includes this new character. 

Proof: if on adding 1 character, maxPalindromeLen increased by 3 or more, say the new maxPalindromeLen is Q, 
and the old maxPalindromeLen is P, and Q>=P+3. Then it would mean, even without this new character, 
there would be a palindromic substring ending in the last character, whose length is at least Q-2. 
Since Q-2 would be >P, this contradicts the condition that P is the maxPalindromeLen without the additional character.

So, it becomes simple, you only need to scan from beginning to the end, adding one character at a time, 
keeping track of maxPalindromeLen, and for each added character, you check if the substrings ending with this new character, 
with length P+1 or P+2, are palindromes, and update accordingly.

Now, this is O(n^2) as taking substrings and checking palindromicity seem O(n) time. 
e can speed up it by realizing that strings are immutable, 
and there are memory slicing tricks will help to speed these operations up. 
comparing string equality with "==" is O(1), and using slicing to substring and reverse is 
̶a̶l̶s̶o̶ ̶O̶(̶1̶)̶ ̶(̶n̶o̶t̶ ̶t̶o̶t̶a̶l̶l̶y̶ ̶s̶u̶r̶e̶ ̶a̶b̶o̶u̶t̶ ̶t̶h̶e̶ ̶s̶l̶i̶c̶i̶n̶g̶ ̶t̶h̶o̶u̶g̶h̶.̶ ̶ ̶I̶ ̶t̶h̶i̶n̶k̶ ̶i̶t̶ ̶i̶s̶ ̶O̶(̶1̶)̶,̶ ̶b̶u̶t̶ ̶c̶o̶u̶l̶d̶ ̶n̶o̶t̶ ̶f̶i̶n̶d̶ ̶a̶n̶y̶ ̶s̶o̶l̶i̶d̶ ̶l̶i̶t̶e̶r̶a̶t̶u̶r̶e̶ ̶a̶b̶o̶u̶t̶ ̶i̶t̶.̶ O(n) 
(thanks to ChuntaoLu). But as slicing is optimized by the interpreter's C code, it should run pretty fast. 
I'm pretty new to Python. Would appreciate you would give more insights or further optimization.

Thus, here is the O(n) method:
"""

class Solutio2:
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]



"""
动态规划
动态规划的两个特点：第一大问题拆解为小问题，第二重复利用之前的计算结果，来解答这道题。

那如何划分小问题呢，我们可以先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，这些必定是回文。
然后计算所有长度为2的子字符串，再根据起始位置从左向右。到长度为3的时候，我们就可以利用上次的计算结果：
如果中心对称的短字符串不是回文，那长字符串也不是，如果短字符串是回文，那就要看长字符串两头是否一样。
这样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。

我们维护一个二维数组dp，其中dp[i][j]表示字符串区间[i, j]是否为回文串，当i = j时，只有一个字符，肯定是回文串，如果i = j + 1，
说明是相邻字符，此时需要判断s[i]是否等于s[j]，如果i和j不相邻，即i - j >= 2时，除了判断s[i]和s[j]相等之外，dp[j + 1][i - 1]若为真，
就是回文串，通过以上分析，可以写出递推式如下：

dp[i, j] = 1                                        if i == j

         = s[i] == s[j]                             if j = i + 1

         = s[i] == s[j] && dp[i + 1][j - 1]         if j > i + 1      

"""
class Solution3:
    def longestPalindrome(self, s):
        if len(set(s)) == 1: return s
        n = len(s)
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start : end + 1]


"""
5.2 解题思路：
思路一：首先创建判断是否是回文的函数ishuiwen。需要三个参数，string s,int x,int y。x和y是判断字符串s的起始位置。
如果x==y，则为奇数回文字符串判断，并且回文字符串起始长度设为1，x–,y++。如果x!=y，则为偶数回文字符串判断，并且回文字符串起始长度设为0。
后循环条件，x大于等于0 并且 y小于s.length() && s[x]==s[y]，则长度+=2,x–,y++。这样最后返回得到的回文字符串s.substr(x + 1, 
count)。然后在longestPalindrome函数中，寻找最大的回文子串。
从k=0开始，每次判断两个回文子串，一个奇数的，一个偶数的，并记录长度大的子串。

思路二：首先，设置回文子串起始位置first=0，长度count=1。for k循环遍历字符串s，首先设置临时长度c_temp=0。
用i=k,然后for j逆向找个s中第一个与是s[i]相等的字符，这是回文子串的结束位置。此时回文子串的临时长度c_temp=2，然后i++，j–。
如果i小于j，则继续判断s[i]==s[j]，相等则i++，j–，c_temp+=2，不相等则c_temp=0，同时break。如果i==j，则c_temp+=1.
然后判断c_temp与count的大小，决定是否更新count与first。这样直至循环结束。最后，返回s.substr(first,count)。
"""


