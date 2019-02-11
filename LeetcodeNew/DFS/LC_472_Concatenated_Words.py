"""
Do you still remember how did you solve this problem?
https://leetcode.com/problems/word-break/

If you do know one optimized solution for above question is using DP,
this problem is just one more step further.
 We iterate through each word and see if it can be formed by using other words.

Of course it is also obvious that a word can only be formed by words shorter than it.
So we can first sort the input by length of each word,
and only try to form one word by using words in front of it.

"""

class Solution:
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
        """
        :type words: List[str]
        :rtype: List[str]
        """
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





