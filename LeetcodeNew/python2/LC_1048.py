
class Solution:
    def longestStrChain(self, words) -> int:
        dp = {}
        for w in sorted(words, key=len):
            print(w)
            dp[w] = max(dp.get(w[:i] + w[ i +1:], 0) + 1 for i in range(len(w)))
        print(dp)
        return max(dp.values())


words = ["a","b","ba","bca","bda","bdca"]
a = Solution()
print(a.longestStrChain(words))
