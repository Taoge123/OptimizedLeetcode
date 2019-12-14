"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i, graph, visited):
                return False
        return True

    def dfs(self, i, graph, visited):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(j, graph, visited):
                return False
        visited[i] = 1
        return True


class Solution2:
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
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return len(visited) == numCourses





