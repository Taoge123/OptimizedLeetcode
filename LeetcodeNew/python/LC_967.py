
"""
We initial the current result with all 1-digit numbers,
like cur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

Each turn, for each x in cur,
we get its last digit y = x % 10.
If y + K < 10, we add x * 10 + y + K to the new list.
If y - K >= 0, we add x * 10 + y - K to the new list.

We repeat this step N - 1 times and return the final result.
"""



class SolutionRika:
    def numsSameConsecDiff(self, n: int, k: int):
        path = ''
        res = []
        self.dfs(n, k, 0, path, res)
        return res

    def dfs(self, n, k, pos, path, res):

        if pos == n:
            res.append(int(path))
            return

        for i in range(10):
            if not path and i == 0:  # no leading zero
                continue
            if not path or abs(int(path[-1]) - i) == k:
                self.dfs(n, k, pos + 1, path + str(i), res)



class SolutionLee:
    def numsSameConsecDiff(self, N: int, K: int):
        cur = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
        if N == 1:
            return cur

        for i in range(2, N+ 1):
            cur2 = []
            for x in cur:
                y = x % 10
                if y + K < 10 and x > 0:
                    cur2.append(x * 10 + y + K)
                if y - K >= 0 and K != 0:
                    cur2.append(x * 10 + y - K)
            cur = cur2
        return cur



class Solution:
    def numsSameConsecDiff(self, N, K):
        cur1 = {x for x in range(1, 10)}
        for _ in range(N - 1):
            cur2 = set()
            for x in cur1:
                y = x % 10
                if y - K >= 0:
                    cur2.add(10 * x + y - K)
                if y + K <= 9:
                    cur2.add(10 * x + y + K)
            cur1 = cur2

        if N == 1:
            cur1.add(0)

        return list(cur1)








