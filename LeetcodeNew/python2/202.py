
class Solution:
    def isHappy(self, n):

        visited = set()

        while n not in visited:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        return n == 1



