"""
https://leetcode.com/problems/find-all-people-with-secret/discuss/1606417/Simple-Python-DFS-solution

"""


import collections


class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson):

        visited = set()
        visited.add(0)
        visited.add(firstPerson)

        meetings.sort(key = lambda x : x[2])

        graph = {}
        for x, y, time in meetings:
            if time not in graph:
                graph[time] = collections.defaultdict(list)
            graph[time][x].append(y)
            graph[time][y].append(x)

        def dfs(mapping, node):
            visited.add(node)
            for nei in mapping[node]:
                if nei in visited:
                    continue
                dfs(mapping, nei)

        for time in graph:
            mapping = graph[time]
            for node in mapping:
                if node in visited:
                    dfs(mapping, node)

        return list(visited)




