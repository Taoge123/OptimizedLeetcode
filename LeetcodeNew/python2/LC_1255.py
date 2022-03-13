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



class SolutionTony:
    def maxScoreWords(self, words, letters, score):

        count = collections.defaultdict(int)
        for ch in letters:
            count[ch] += 1

        n = len(words)

        def dfs(i, count):
            if i >= n:
                return 0

            flag = True
            word_count = collections.Counter(words[i])

            for ch in word_count:
                if word_count[ch] > count[ch]:
                    return dfs(i + 1, count)

            # use chars and subtract from count
            for ch in words[i]:
                if count[ch] < 1:
                    return dfs(i + 1, count)
                count[ch] -= 1

            pick = dfs(i + 1, count) + get_score(words[i])
            # add it back for backtracking
            for ch in words[i]:
                count[ch] += 1

            no_pick = dfs(i + 1, count)
            return max(pick, no_pick)

        def get_score(word):
            val = 0
            for ch in word:
                val += score[ord(ch) - ord('a')]
            return val

        return dfs(0, count)


words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
a = SolutionTony()
print(a.maxScoreWords(words, letters, score))


