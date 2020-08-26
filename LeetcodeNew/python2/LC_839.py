

class SolutionTLE:
    def similar(self, s, t):
        return sum(a != b for a, b in zip(s, t)) <= 2

    def find(self, s):
        if self.parent[s] == s:
            return self.parent[s]
        return self.find(self.parent[s])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += self.rank[x] == self.rank[y]

    def numSimilarGroups(self, A):
        self.parent = {}
        self.rank = {}

        for char in A:
            self.parent[char] = char
            self.rank[char] = 1

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if self.similar(A[i], A[j]):
                    self.union(A[i], A[j])

        return len(set(self.find(char) for char in A))






