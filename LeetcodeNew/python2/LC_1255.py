import collections

class Solution:
    def maxScoreWords(self, words, letters, score):
        def getSrore(count):
            return sum([score[ord(c) - ord('a')] * count[c] for c in count])

        def dfs(i, count):
            if i >= len(words):
                return 0
            # do not select current word
            res = dfs(i + 1, count)

            # select current word
            count_word = collections.Counter(words[i])
            if all(count_word[c] <= count[c] for c in count_word):
                remain = collections.Counter()
                for c in count:
                    remain[c] = count[c] - count_word[c]
                res = max(res, dfs(i + 1, remain) + getSrore(count_word))
            return res

        return dfs(0, collections.Counter(letters))



