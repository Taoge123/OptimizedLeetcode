
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        graph = collections.defaultdict(list)
        # visited = collections.defaultdict(int)
        res = []
        indegree = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(res) == numCourses:
            return res
        return []

