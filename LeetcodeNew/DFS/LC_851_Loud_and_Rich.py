"""
Explanation:
The description is not easy to understand.
In fact it's a basic dfs traversal problem.
For every people, call a sub function dfs to compare the quiet with others,
who is richer than him.
Also we will note this answer to avoid repeated calculation.
Sub function dfs traverse every people only once,
and every richer is traversed only one once.
"""
import collections

class Solution:

    def loudAndRich(self, richer, quiet):
        m = collections.defaultdict(list)
        for i, j in richer:
            m[j].append(i)
        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] >= 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]:
                    res[i] = res[j]
            return res[i]

        for i in range(len(quiet)): dfs(i)
        return res

class Solution2:
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in range(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return map(dfs, range(N))












