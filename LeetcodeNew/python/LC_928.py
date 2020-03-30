import collections
import itertools

class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        table = collections.defaultdict(list)
        # 对每个初始感染节点依次bfs，因为节点总数不超过300，所以不会超时
        for init in initial:
            visited = set(initial)
            queue = collections.deque([init])
            while queue:
                infect = queue.popleft()
                for node in range(len(graph[infect])):
                    if graph[infect][node] == 0:
                        continue
                    if node in visited:
                        continue
                    visited.add(node)
                    table[node].append(init)
                    queue.append(node)
        # 统计出现最多次的感染节点
        res = [0] * n
        for key in table:
            if len(table[key]) == 1:
                res[table[key][0]] += 1
        if max(res) == 0:
            return min(initial)
        return res.index(max(res))





class SolutionBetter:
    def minMalwareSpread(self, graph, initial) -> int:
        if not graph:
            return -1
        N = len(graph)
        clean = set(range(N)) - set(initial)
        parents = list(range(N))
        size = [1] * N

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                if size[a] < size[b]:
                    parents[a] = b
                    size[b] += size[a]
                else:
                    parents[b] = a
                    size[a] += size[b]

        for u, v in itertools.combinations(clean, 2):
            if graph[u][v]: union(u, v)

        table = collections.defaultdict(set)
        infectedTimes = collections.Counter()
        for u in initial:
            for v in clean:
                if graph[u][v]:
                    table[u].add(find(v))

            for comm in table[u]:
                infectedTimes[comm] += 1

        count = [0] * N
        for u, comms in table.items():
            for comm in comms:
                if infectedTimes[comm] == 1:
                    count[u] += size[comm]

        maxi = max(count)
        return count.index(maxi) if maxi != 0 else min(initial)






