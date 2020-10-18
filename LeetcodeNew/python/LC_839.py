import collections

class SolutionUF:
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


class SolutionDFS:
    def numSimilarGroups(self, A):
        graph = collections.defaultdict(list)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if self.similar(A[i], A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * len(A)
        res = 0
        for i in range(len(A)):
            if not visited[i]:
                self.dfs(A, i, visited, graph)
                res += 1

        return res

    def similar(self, word1, word2):
        mismatches = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1
                if mismatches > 2:
                    return False
        return True

    def dfs(self, A, i, visited, graph):
        visited[i] = True
        for nei in graph[i]:
            if not visited[nei]:
                self.dfs(A, nei, visited, graph)




class SolutionBFS:
    def numSimilarGroups(self, A) -> int:
        res = 0
        visited = [False] * len(A)

        for i in range(len(A)):
            if visited[i]:
                continue
            res += 1
            queue = collections.deque()
            queue.append(A[i])
            while queue:
                node = queue.popleft()
                for j in range(len(A)):
                    if visited[j]:
                        continue

                    diff = 0
                    k = 0
                    while k < len(node) and diff <= 2:
                        if node[k] != A[j][k]:
                            diff += 1
                        k += 1

                    if diff == 2 or diff == 0:
                        visited[j] = True
                        queue.append(A[j])
        return res






