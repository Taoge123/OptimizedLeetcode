
"""
https://blog.csdn.net/fuxuemingzhu/article/details/83088406
http://bookshadow.com/weblog/2016/12/04/leetcode-unique-substrings-in-wraparound-string/

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz",
so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s.
In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""
import collections

class SOlutionLee:
    def findSubstringInWraproundString2(self, p):
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())

"""
After failed with pure math solution and time out with DFS solution, I finally realized that this is a DP problem...
The idea is, if we know the max number of unique substrings in p ends with 'a', 'b', ..., 'z', 
then the summary of them is the answer. Why is that?

The max number of unique substring ends with a letter equals to the length of max contiguous substring ends with that letter. 
Example "abcd", the max number of unique substring ends with 'd' is 4, apparently they are "abcd", "bcd", "cd" and "d".
If there are overlapping, we only need to consider the longest one because it covers all the possible substrings. 
Example: "abcdbcd", the max number of unique substring ends with 'd' is 4 and all substrings formed by the 2nd "bcd" part are covered in the 4 substrings already.
No matter how long is a contiguous substring in p, it is in s since s has infinite length.
Now we know the max number of unique substrings in p ends with 'a', 'b', ..., 'z' 
and those substrings are all in s. Summary is the answer, according to the question.
"""
class Solution1:
    def findSubstringInWraproundString(self, p):
        if len(p) < 1:
            return 0

        alphabet_cache = [0] * 26

        curr_len = 1
        alphabet_cache[ord(p[0]) - ord('a')] = 1
        for i in range(1, len(p)):
            if (((ord(p[i - 1]) - ord('a')) + 1) % 26) == (ord(p[i]) - ord('a')):
                curr_len = curr_len + 1
            else:
                curr_len = 1
            # the method of differentiating unique substrings is to keep track of the max number
            # of substrings that end in this specific letter i.
            alphabet_cache[ord(p[i]) - ord('a')] = max(alphabet_cache[ord(p[i]) - ord('a')], curr_len)
        return sum(alphabet_cache)


"""
Concise and straightforward! Attached is the python version of your solution.
Short explanation in case someone still confuse about zyoppy008's solution. 
Letters[i] represents the longest consecutive substring ended with chr(97+i), 
update res only when current L is bigger than letters[curr].
"""
class Solution2:
    def findSubstringInWraproundString(self, p):

        letters = [0] * 26
        res = L = curr = 0
        for i in range(len(p)):
            pre, curr = curr, ord(p[i]) - 97
            L = 1 if i > 0 and (pre + 1) % 26 != curr else L+1
            if L > letters[curr]:
                res += L - letters[curr]
                letters[curr] = L
        return res

"""
I use cmap[c] to store the maximum length of sub-string starts with c.

The time complexity of the code below is O(n) as well.
"""
class Solution3:
    def findSubstringInWraproundString(self, p):

        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        cmap = collections.defaultdict(int)
        start = end = 0
        for c in range(len(p)):
            if c and p[c-1:c+1] not in pattern:
                for x in range(start, end):
                    cmap[p[x]] = max(end - x, cmap[p[x]])
                start = c
            end = c + 1
        for x in range(start, end):
            cmap[p[x]] = max(end - x, cmap[p[x]])
        return sum(cmap.values())

class Solution4:
    def findSubstringInWraproundString(self, p):

        if len(p) <= 1:
            return len(p)
        count = collections.defaultdict(int)
        max_length = 1
        count[p[0]] = 1
        match = "zabcdefghijklmnopqrstuvwxyz"
        for i in range(1, len(p)):
            if p[i-1] + p[i] in match:
                max_length += 1
            else:
                max_length = 1
            count[p[i]] = max(count[p[i]], max_length)
        return sum(count.values())

"""
This solution might look a bit verbose but it is straight forward. 
dp[i] is the number of qualified substrings ending at the position i in p, 
seen is a dictionary keyed by the character c that maintains the greatest number of qualified substrings ending at the char c.
"""
class Solution5:
    def findSubstringInWraproundString(self, p):
        N = len(p)
        if N <= 1: return N

        dp = [0 for i in range(N)]
        start, seen = 0, {}
        dp[0], seen[p[0]] = 1, 1

        for i in range(1, N):
            if p[i - 1] == 'z' and p[i] == 'a' or ord(p[i - 1]) + 1 == ord(p[i]):
                x = i - start + 1
                if p[i] not in seen:
                    dp[i] = x
                    seen[p[i]] = dp[i]
                else:
                    if x > seen[p[i]]:
                        dp[i] = x - seen[p[i]]
                        seen[p[i]] = x
                    else:
                        dp[i] = 0
            else:
                if p[i] not in seen:
                    dp[i] = 1
                    seen[p[i]] = dp[i]
                else:
                    dp[i] = 0

                start = i

        return sum(dp)


"""
题目大意：
字符串s是小写字母"abcdefghijklmnopqrstuvwxyz"的无限循环，
s看起来像这样："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."

现在我们有另外一个字符串p。你需要寻找p有多少个非空子串在s中出现。输入p，你需要输出s中有多少个不同的p的非空子串。

解题思路：
按照子串的首字母分类计数

用字典cmap记录以某字母开始的子串的最大长度

遍历字符串p，维护区间[start, end]，p[start ... end]是无限循环字符串s的一部分

更新p[start], p[start + 1], ... p[end]在cmap中的长度值

最终结果为cmap中value的和
"""
class Solution6:
    def findSubstringInWraproundString(self, p):

        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        cmap = collections.defaultdict(int)
        start = end = 0
        for c in range(len(p)):
            if c and p[c-1:c+1] not in pattern:
                for x in range(start, end):
                    cmap[p[x]] = max(end - x, cmap[p[x]])
                start = c
            end = c + 1
        for x in range(start, end):
            cmap[p[x]] = max(end - x, cmap[p[x]])
        return sum(cmap.values())


"""
将上述代码中cmap的含义变更为记录以某字母结尾的子串的最大长度，可以使代码简化。
"""
class Solution7:
    def findSubstringInWraproundString(self, p):

        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        cmap = collections.defaultdict(int)
        clen = 0
        for c in range(len(p)):
            if c and p[c-1:c+1] not in pattern:
                clen = 1
            else:
                clen += 1
            cmap[p[c]] = max(clen, cmap[p[c]])
        return sum(cmap.values())

"""
题目大意
在一个无限循环的字母表s中，找出给定的字符串的所有子串在s中出现了多少次。

解题方法
这个做法和前几天的某个做法一致，从头开始遍历，在遍历的过程中，只用考虑当新添加这个字符的时候，
能否和前面构成连续的，如果能构成连续的，那么结果中增加上以这个字符结尾的子串个数，即当前的长度。否则就是一个新串，长度是1.

其实这个思路就是dp，dp数组保存的是以当前字符结尾，能够成的所有子字符串个数。

比如abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd,
d，那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中，
那么我们知道以某个字符结束的最大字符串包含其他以该字符结束的字符串的所有子字符串。

这个思路又有点类似于虫取法，一直更新和保存子区间的长度。

时间复杂度是O(N)，空间复杂度是O(26)。

"""
class Solution8:
    def findSubstringInWraproundString(self, p):

        count = collections.defaultdict(int)
        N = len(p)
        _len = 0
        for i in range(N):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or (p[i] == 'a' and p[i - 1] == 'z')):
                _len += 1
            else:
                _len = 1
            count[p[i]] = max(count[p[i]], _len)
        return sum(count.values())

class Solution9:
    def findSubstringInWraproundString(self, p):

        letters = [0] * 26
        result, length = 0, 0
        for i in range(len(p)):
            curr = ord(p[i]) - ord('a')
            if i > 0 and ord(p[i-1]) != (curr-1)%26 + ord('a'):
                length = 0
            length += 1
            if length > letters[curr]:
                result += length - letters[curr]
                letters[curr] = length
        return result





