class Solution:
    def mostVisited(self, n: int, rounds):
        res = []
        for i in range(rounds[0], rounds[-1] + 1, 1):
            res.append(i)

        if len(res) > 0:
            return res

        for i in range(1, rounds[-1] + 1):
            res.append(i)

        for i in range(rounds[0], n + 1):
            res.append(i)

        return res




