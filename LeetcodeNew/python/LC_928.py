"""
https://buptwc.com/2018/10/21/Leetcode-928-Minimize-Malware-Spread-II/
https://leetcode.com/problems/minimize-malware-spread-ii/discuss/515981/Python-Time-O(n3)-DFS-Solution
https://leetcode.com/problems/minimize-malware-spread-ii/discuss/184112/Short-Python-DFS-solution-w-short-explanation-~290-ms


"""

import collections
import itertools

class SolutionBFS:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        sources = collections.defaultdict(list)
        # 对每个初始感染节点依次bfs，因为节点总数不超过300，所以不会超时
        for init in initial:
            visited = set(initial)
            queue = collections.deque([init])
            while queue:
                node = queue.popleft()
                for nei in range(len(graph[node])):
                    if graph[node][nei] == 0:
                        continue
                    if nei in visited:
                        continue
                    visited.add(nei)
                    sources[nei].append(init)
                    queue.append(nei)
        # 统计出现最多次的感染节点
        count = [0] * n
        for key in sources.keys():
            #如果一个节点只有另一个能感染
            if len(sources[key]) == 1:
                count[sources[key][0]] += 1
        if max(count) == 0:
            return min(initial)
        return count.index(max(count))





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




class SolutionDFS:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        clean = set(range(n)) - set(initial)

        def dfs(node):
            visited.add(node)
            for nei, adj in enumerate(graph[node]):
                if nei not in clean:
                    continue
                if nei in visited:
                    continue
                if adj:
                    dfs(nei)

        # For each node u in initial, dfs to find
        # 'visited': all nodes not in initial that it can reach.
        # infected_by = {v: [] for v in clean}
        infected_by = collections.defaultdict(list)
        for node in initial:
            visited = set()
            dfs(node)

            # For each node v that was visited, u infects v.
            for nei in visited:
                infected_by[nei].append(node)

        # For each node u in initial, for every v not in initial
        # that is uniquely infected by u, add 1 to the contribution for u.
        # v是all clean nodes， nei是initial的nodes， 如果v正好只被一个nei影响，说明可以
        contribution = collections.defaultdict(int)
        for v, nei in infected_by.items():
            if len(nei) == 1:
                contribution[nei[0]] += 1

        # Take the best answer.
        maxi = -1
        res = min(initial)
        for node, score in contribution.items():
            if score > maxi or (score == maxi and node < res):
                maxi = score
                res = node
        return res




