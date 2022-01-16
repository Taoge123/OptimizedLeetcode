import collections


class SolutionTony:
    def countSubTrees(self, n: int, edges, labels: str):
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            count = collections.defaultdict(int)
            for nei in graph[node]:
                if nei == parent:
                    continue
                nxt = dfs(nei, node)
                for k in nxt:
                    count[k] += nxt[k]
            count[labels[node]] += 1
            res[node] = count[labels[node]]
            return count

        res = [0] * n
        dfs(0, None)
        return res



class SolutionCounter:
    def countSubTrees(self, n: int, edges, labels: str):

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int):
            count = collections.Counter()
            for child in graph[node]:
                if child == parent: continue
                count += dfs(child, node)
            count[labels[node]] += 1
            result[node] = count[labels[node]]
            return count

        result = [0] * n
        dfs(0, None)
        return result



class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        graph = collections.defaultdict(list)
        res = [0] * n
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.dfs(graph, labels, 0, visited, res)
        return res

    def dfs(self, graph, labels, node, visited, res):
        count = collections.Counter()
        if node not in visited:
            count[labels[node]] += 1
            visited.add(node)
            for child in graph[node]:
                count += self.dfs(graph, labels, child, visited, res)
            res[node] = count[labels[node]]
        return count


