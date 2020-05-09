import collections

class Solution:
    def longestStrChain(self, words) -> int:
        table = {i: set() for i in range(1, 17)}

        for word in words:
            table[len(word)].add(word)

        dp = collections.defaultdict(lambda: 1)

        for k in range(2, 17):
            for word in table[k]:
                for i in range(k):
                    prev = word[:i] + word[i + 1:]
                    if prev in table[k - 1]:
                        dp[word] = max(dp[word], dp[prev] + 1)

        return max(dp.values() or [1])




class SolutionBetter:
    def longestStrChain(self, words) -> int:
        dp = {}
        for w in sorted(words, key=len):
            print(w)
            dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))
        print(dp)
        return max(dp.values())


words = ["a","b","ba","bca","bda","bdca"]
a = Solution()
print(a.longestStrChain(words))
