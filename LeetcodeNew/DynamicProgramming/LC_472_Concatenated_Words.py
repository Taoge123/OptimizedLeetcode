
"""
Given a list of words (without duplicates),
please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string
that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""

"""
Do you still remember how did you solve this problem? https://leetcode.com/problems/word-break/

If you do know one optimized solution for above question is using DP, 
this problem is just one more step further. We iterate through each word and see if it can be formed by using other words.

Of course it is also obvious that a word can only be formed by words shorter than it. 
So we can first sort the input by length of each word, and only try to form one word by using words in front of it.
"""
import collections

class Solution1:
    def findAllConcatenatedWordsInADict(self, words):
        words = sorted(words,key=lambda t:len(t))
        word_dict = set()
        def isQualify(w):
            if w in word_dict:return True
            for i in range(1,len(w)):
                if w[:i] in word_dict and isQualify(w[i:]):return True
            return False
        res = []
        for w in words:
            if isQualify(w):res.append(w)
            word_dict.add(w)
        return res

class Solution2:
    def findAllConcatenatedWordsInADict(self, words):
        words = sorted(words,key=lambda t:len(t))
        len_word_dict = collections.defaultdict(set)
        def isQualify(w):
            if w in len_word_dict[len(w)]:return True
            for i in range(1,len(w)):
                if w[:i]in len_word_dict[i] and isQualify(w[i:]):return True
            return False
        res = []
        for w in words:
            if isQualify(w): res.append(w)
            len_word_dict[len(w)].add(w)
        return res


class Solution3:
    def findAllConcatenatedWordsInADict(self, words):

        d = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res


class Solution4:
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':
        d = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    memo[word] = True
                    break
                if prefix in d and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in d and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]
        return [word for word in words if dfs(word)]


class Solution5:
    def findAllConcatenatedWordsInADict(self, words):

        res = []
        words_dict = set(words)
        for word in words:
            words_dict.remove(word)
            if self.check(word, words_dict) is True:
                res.append(word)
            words_dict.add(word)
        return res

    def check(self, word, d):
        if word in d:
            return True

        for i in range(len(word), 0, -1):
            if word[:i] in d and self.check(word[i:], d):
                return True
        return False

