
"""
\Given a string and a string dictionary,
find the longest string in the dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
"""

"""
Let's check whether each word is a subsequence of S individually by "best" order 
(largest size, then lexicographically smallest.) 
Then if we find a match, we know the word being considered must be the best possible answer, 
since better answers were already considered beforehand.

Let's figure out how to check if a needle (word) is a subsequence of a haystack (S). 
This is a classic problem with the following solution: walk through S, 
keeping track of the position (i) of the needle 
that indicates that word[i:] still remains to be matched to S at this point in time. 
Whenever word[i] matches the current character in S, we only have to match word[i+1:], 
so we increment i. At the end of this process, 
i == len(word) if and only if we've matched every character 
in word to some character in S in order of our walk.
"""

"""
这道题给了我们一个字符串，和一个字典，让我们找到字典中最长的一个单词，
这个单词可以通过给定单词通过删除某些字符得到。由于只能删除某些字符，并不能重新排序，
所以我们不能通过统计字符出现个数的方法来判断是否能得到该单词，而是只能老老实实的按顺序遍历每一个字符。
我们可以给字典排序，通过重写comparator来实现按长度由大到小来排，如果长度相等的就按字母顺序来排。
然后我们开始遍历每一个单词，用一个变量i来记录单词中的某个字母的位置，我们遍历给定字符串，
如果遍历到单词中的某个字母来，i自增1，如果没有，就继续往下遍历。这样如果最后i和单词长度相等，
说明单词中的所有字母都按顺序出现在了字符串s中，由于字典中的单词已经按要求排过序了，
所以第一个通过验证的单词一定是正确答案，我们直接返回当前单词即可
"""

class Solution1:
    def findLongestWord(self, S, D):
        D.sort(key=lambda x: (-len(x), x))
        for word in D:
            i = 0
            for c in S:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""


class SolutionLee:

    def findLongestWord(self, s, d):
        for word in sorted(d, key=lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in word): return word
        return ''


class Solution3:
    def findLongestWord(self, s, d):
        res = ''
        for cand in d:
            if self.check(s, cand) and (len(cand) > len(res) or (len(cand) == len(res) and cand < res)):
                res = cand
        return res

    def check(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            i += 1
        return j == len(t)



