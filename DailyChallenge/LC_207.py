
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = []
        while queue:
            node = queue.popleft()
            visited.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return len(visited) == numCourses

