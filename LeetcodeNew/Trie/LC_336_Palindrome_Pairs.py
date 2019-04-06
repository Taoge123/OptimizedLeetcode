
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
解题思路：
O(k * n ^2)解法 其中k为单词个数，n为单词的长度：

利用字典wmap保存单词 -> 下标的键值对

遍历单词列表words，记当前单词为word，下标为idx：

1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案

2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案

3). 将当前单词word拆分为左右两半left，right。

     3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
     
     3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
    """


class Solution1:
    def palindromePairs(self, words):

        wmap = {y: x for x, y in enumerate(words)}

        def isPalindrome(word):
            size = len(word)
            for x in range(size / 2):
                if word[x] != word[size - x - 1]:
                    return False
            return True

        ans = set()
        for idx, word in enumerate(words):
            if "" in wmap and word != "" and isPalindrome(word):
                bidx = wmap[""]
                ans.add((bidx, idx))
                ans.add((idx, bidx))

            rword = word[::-1]
            if rword in wmap:
                ridx = wmap[rword]
                if idx != ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in wmap:
                    ans.add((wmap[rright], idx))
                if isPalindrome(right) and rleft in wmap:
                    ans.add((idx, wmap[rleft]))
        return list(ans)

#Faster
class Solution2:
    '''算法思路：
    因为结果已知，由结果推导未知数，然后寻找未知数是否在表里边，是 hashtable 常见的一种应用，
    比如像 Two Sum，Three Sum 等等
    '''
    def palindromePairs(self, words):
        table, res = dict(map(reversed, enumerate(words))), set()
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                a, b = word[:k], word[k:]

                if a == a[::-1] and table.get(b[::-1], -1) not in [-1, i]:
                    res.add((table[b[::-1]], i))

                if b == b[::-1] and table.get(a[::-1], -1) not in [-1, i]:
                    res.add((i, table[a[::-1]]))

        return list(res)








