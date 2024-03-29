

"""
Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

"""


class Solution:
    def generateAbbreviations(self, word: str):
        n = len(word)
        res = []

        def dfs(path, pos, count):
            if pos == n:
                # if we still have count (like wo2)
                path = path + (str(count) if count else "")
                res.append(path)
                return

            # to accumulate count / count + str
            # count reset to 0
            dfs(path + (str(count) if count else "") + word[pos], pos + 1, 0)
            dfs(path, pos + 1, count + 1)

        dfs("", 0, 0)
        return res


class Solution2:
    def generateAbbreviations(self, word):

        res = []
        self.dfs(word, 0, "", res)
        return res

    def dfs(self, word, pos, path, res):
        if pos == len(word):
            res.append(path)
        else:
            self.dfs(word, pos + 1, path + word[pos], res)
            if not path or path[-1].isalpha():
                for j in range(pos + 1, len(word) + 1):
                    self.dfs(word, j, path + str(j - pos), res)



