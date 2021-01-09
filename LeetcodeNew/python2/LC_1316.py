
"""
dp[i][j]

XX[XXi]XXX[XXj]

1316.Distinct-Echo-Substrings
本题其实很简单。定义dp[i][j]表示以i结尾的substring和以j结尾的substring最长有多少字符是相同的。这是一个非常基础的动态规划。

如果发现dp[i][j]>=j-i，那么就说明text[i+1:j]就是符合要求的echo substring的一半。统计个数的时候我们再用一个set来去重就行。

"""



class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        dp[0][0] = 0
        visited = set()
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if text[i - 1] == text[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] >= j - i:
                    temp = text[i:j]
                    # print(temp, visited)
                    if temp not in visited:
                        res += 1
                        visited.add(temp)
        return res




class Solution2:
    def distinctEchoSubstrings(self, text: str) -> int:
        table = {}
        res = set()
        for i, v in enumerate(text):
            if v not in table:
                table[v] = [i]
            else:
                for j in table[v]:
                    if text[j:i] == text[i:i+i-j]:
                        res.add(text[j:i])
                table[v].append(i)

        print(res)
        return len(res)


