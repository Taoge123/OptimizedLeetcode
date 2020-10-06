"""
m : 2 ^ m


"""


class Solution:
    def maximumRequests(self, n: int, requests) -> int:
        m = len(requests)
        res = 0
        for state in range((1 << m)):
            if self.check(state, n, requests):
                res = max(res, self.count(state))
        return res

    def check(self, s, n, requests):
        building = [0] * 20
        for i in range(n):
            building[i] = 0

        m = len(requests)
        for i in range(m):
            if ((s >> i) & 1) == 1:
                building[requests[i][0]] -= 1
                building[requests[i][1]] += 1

        for i in range(n):
            if building[i] != 0:
                return False
        return True

    def count(self, s):
        res = 0
        for i in range(32):
            if ((s >> i) & 1) == 1:
                res += 1
        return res


