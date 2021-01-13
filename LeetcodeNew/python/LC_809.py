class Solution_:

    def check(self, s, w):
        # lllll
        n, m = len(s), len(w)
        j = 0
        for i in range(n):
            if j < m and s[i] == w[j]:
                j += 1
            elif s[i - 1:i + 2] != s[i] * 3 != s[i - 2:i + 1]:
                return False

        return j == m

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        res = 0
        for w in words:
            res += self.check(S, w)
        return res



class Solution:
    def expressiveWords(self, S: str, words) -> int:
        if not S or len(words) == 0:
            return 0
        res = 0
        for word in words:
            if self.helper(S, word):
                res += 1
        return res

    def helper(self, s, word):
        if not word:
            return False

        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                len1 = self.getLength(s, i)
                len2 = self.getLength(word, j)
                if len1 < 3 and len1 != len2 or len1 >= 3 and len1 < len2:
                    return False
                i += len1
                j += len2
            else:
                return False

        return i == len(s) and j == len(word)

    def getLength(self, word, i):
        j = i
        while j < len(word) and word[j] == word[i]:
            j += 1
        return j - i


"""
compression
 h e l l o o o
               i 
               j
 h - 1
 e - 1
 j - 2

"""

#         for word in words:
#             i = j = g = 0
#             while i < len(word):
#                 while j + 1 < len(word) and word[j + 1] == word[j]:
#                     j += 1
#                 if guide[g][0] != word[i] or (guide[g][1] == 2 and j - i + 1 == 1) or guide[g][1] < j - i + 1:
#                     break
#                 i, j, g = j + 1, j + 1, g + 1
#             if g == len(guide): res += 1
#         return res



class Solution2:
    def expressiveWords(self, S, words):

        if not S:
            return 0
        guide, i, j, res = [], 0, 0, 0
        while i < len(S):
            while j + 1 <len(S) and S[j + 1] == S[j]: j += 1
            guide.append((S[i], j - i + 1))
            i = j = j + 1
        for word in words:
            i = j = g = 0
            while i < len(word):
                while j + 1 < len(word) and word[j + 1] == word[j]: j += 1
                if guide[g][0] != word[i] or (guide[g][1] == 2 and j - i + 1 == 1) or guide[g][1] < j - i + 1: break
                i, j, g = j + 1, j + 1, g + 1
            if g == len(guide): res += 1
        return res




S = "heeellooo"
words = ["hello", "hi", "helo"]
a = Solution()
print(a.expressiveWords(S, words))

