

"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""

"""
O(k * n ^2)解法 其中k为单词个数，n为单词的长度：

利用字典wmap保存单词 -> 下标的键值对

遍历单词列表words，记当前单词为word，下标为idx：

1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案

2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案

3). 将当前单词word拆分为左右两半left，right。

     3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
     
     3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加
"""

class Solution:
    def palindromePairs(self, words):
        table = {word: i for i, word in enumerate(words)}
        res = set()
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                a = word[:k]
                b = word[k:]

                if a == a[::-1] and table.get(b[::-1], -1) not in [-1, i]:
                    res.add((table[b[::-1]], i))

                if b == b[::-1] and table.get(a[::-1], -1) not in [-1, i]:
                    res.add((i, table[a[::-1]]))

        return list(res)


class Solution2:
    def palindromePairs(self, words):

        table, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                a, b = word[:j], word[j:]
                if a in table and i != table[a] and b == b[::-1]:
                    res.append([i, table[a]])
                if j > 0 and b in table and i != table[b] and a == a[::-1]:
                    res.append([table[b], i])
        return res



words = ["abcd","dcba","lls","s","sssll"]

a = Solution()
print(a.palindromePairs(words))





