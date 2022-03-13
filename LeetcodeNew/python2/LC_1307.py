"""
https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463920/Python-Backtracking
https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463921/python-backtracking-with-pruning-tricks
https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/464400/Python-backtracking


CBA
ED
F

-----
JIHG

# row, col, acuumulated sum
dfs(i, j, summ)



"""

import collections


class Solution:
    def isSolvable(self, words, result) -> bool:
        # table = [0] * 128
        # visited = [0] * 10
        table = collections.defaultdict(lambda: -1)
        visited = collections.defaultdict(int)
        result = result[::-1]

        for i, word in enumerate(words):
            if len(word) > len(result):
                return False
            words[i] = word[::-1]

        def dfs(i, j, summ):
            if j == len(result):

                # 如果还有进位, 不行
                if summ != 0:
                    return False
                # result更长, 最后面还有一位, 但后面那位不是 0
                if len(result) > 1 and table[result[-1]] == 0:
                    return False
                return True

            if i == len(words):
                if table[result[j]] != -1:
                    if table[result[j]] != summ % 10:
                        return False
                    else:
                        # this column is good, go back to first row and start second column
                        return dfs(0, j + 1, summ // 10)

                else:
                    if visited[summ % 10] == 1:
                        return False
                    table[result[j]] = summ % 10
                    visited[summ % 10] = 1
                    if dfs(0, j + 1, summ // 10):
                        return True
                    table[result[j]] = -1
                    visited[summ % 10] = 0
                    return False

            if j >= len(words[i]):
                return dfs(i + 1, j, summ)

            ch = words[i][j]
            if table[ch] != -1:
                if len(words[i]) > 1 and j == len(words[i]) - 1 and table[ch] == 0:
                    return False
                return dfs(i + 1, j, summ + table[ch])

            else:
                for d in range(10):
                    if visited[d] == 1:
                        continue
                    table[ch] = d
                    visited[d] = 1
                    if dfs(i + 1, j, summ + d):
                        return True
                    table[ch] = -1
                    visited[d] = 0

                return False

        return dfs(0, 0, 0)



words = ["SEND","MORE"]
result = "MONEY"

a = Solution()
print(a.isSolvable(words, result))



