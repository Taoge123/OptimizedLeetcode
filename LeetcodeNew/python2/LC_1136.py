import collections


class Solution:
    def minimumSemesters(self, N: int, relations) -> int:

        graph = collections.defaultdict(list)
        indegree = {n : 0 for n in range(1, N+ 1)}

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        # queue = collections.deque([(n, 1) for n in indegree if indegree[n] == 0])
        queue = collections.deque()

        for node in range(1, N):
            if not indegree[node]:
                queue.append(node)

        if not queue:
            return -1
        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        queue.append(nei)
            res += 1

        if sum(indegree.values()) != 0:  # if a graph is a DAG, after topo sort, all nodes' indegree will become zero
            return -1
        else:
            return res



