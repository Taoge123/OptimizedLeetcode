
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if i == self.parent[i]:
            return self.parent[i]
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x < y:
            self.parent[y] = x
        else:
            self.parent[x] = y

class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        uf = UnionFind(26)
        for a, b in zip(A, B):
            if a != b:
                uf.union(ord(a) - ord('a'), ord(b) - ord('a'))

        return ''.join((chr(uf.find(ord(ch) - ord('a')) + ord('a')) for ch in list(S)))




