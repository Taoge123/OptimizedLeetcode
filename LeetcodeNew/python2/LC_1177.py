import collections

class Solution:
    def canMakePaliQueries(self, s: str, queries):
        res = []
        for l, r, k in queries:
            ss = s[l: r +1]
            rem = 0
            count = collections.Counter(ss)
            for ch, num in count.items():
                rem += num % 2
            need = rem // 2
            res.append(need <= k)
        return res



class Solution2:
    def canMakePaliQueries(self, s: str, queries):
        dp = [collections.Counter()]
        for i in range(1, len(s) + 1):
            dp.append(dp[i - 1] + collections.Counter(s[i - 1]))

        print(dp)
        res = []
        for l, r, k in queries:
            count = dp[r + 1] - dp[l]
            need = sum(v % 2 for v in count.values()) // 2
            res.append(need <= k)
        return res




class Solution3:
    def canMakePaliQueries(self, s: str, queries):
        n = 26
        dp = [[0] * n]

        for i in range(1, len(s) + 1):
            last = dp[i - 1][:]
            last[ord(s[i - 1]) - ord('a')] += 1
            dp.append(last)

        res = []
        for l, r, k in queries:
            left = dp[l]
            right = dp[r + 1]
            need = sum((right[i] - left[i]) & 1 for i in range(n)) // 2
            res.append(need <= k)
        return res




