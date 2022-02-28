"""
https://github.com/wisdompeak/LeetCode/tree/master/DFS/1718.Construct-the-Lexicographically-Largest-Valid-Sequence

"""


class Solution:
    def constructDistancedSequence(self, n):

        res = [0 for i in range(2 * n - 1)]
        visited = [0 for i in range(n + 1)]

        def dfs(i):
            if i == 2 * n - 1:
                return True
            if res[i] > 0:
                return dfs(i + 1)

            for j in range(n, 0, -1):
                if visited[j] == 1:
                    continue
                if j > 1 and (i + j >= 2 * n - 1 or res[i + j] > 0):
                    continue
                visited[j] = 1
                res[i] = j

                if j > 1:
                    res[i + j] = j

                if dfs(i + 1):
                    return True

                visited[j] = 0
                res[i] = 0

                if j > 1:
                    res[i + j] = 0
            return False

        dfs(0)
        return res





class SolutionRika:
    def constructDistancedSequence(self, n: int):
        # combination --> each time fill num 1 or num 2... n
        # two case:
        # 1) num == 1: only need to fill once --> path[pos]
        # 2) num > 1: need tp fill in two position --> path[pos] and path[pos + num]

        path = [0] * (2 * n - 1)

        res = []
        self.dfs(n, 0, set(), path, res)
        return path

    def dfs(self, n, pos, visited, path, res):

        if len(visited) == n:
            return True

        for num in range(n, 0, -1):  # 从大到小试 ---> 排序
            while pos < len(path) and path[pos] != 0:
                pos += 1

            if num == 1 and num not in visited:
                visited.add(num)
                path[pos] = num
                if self.dfs(n, pos + 1, visited, path, res):
                    return True
                path[pos] = 0
                visited.remove(num)
            if num not in visited and pos + num < len(path) and path[pos] == 0 and path[pos + num] == 0:
                path[pos] = num
                path[pos + num] = num
                visited.add(num)
                if self.dfs(n, pos + 1, visited, path, res):
                    return True
                visited.remove(num)
                path[pos] = 0
                path[pos + num] = 0






