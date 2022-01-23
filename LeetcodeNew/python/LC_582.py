
"""
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
"""

import collections


class SolutionTony:
    def killProcess(self, pid, ppid, kill):
        graph = collections.defaultdict(list)
        for p, pp in zip(pid, ppid):
            graph[pp].append(p)
        res = []
        self.dfs(graph, kill, res)
        return res

    def dfs(self, graph, node, res):

        res.append(node)
        for nei in graph[node]:
            self.dfs(graph, nei, res)


class Solution:
    def killProcess(self, pid, ppid, kill):
        graph = collections.defaultdict(list)
        for u, v in zip(ppid, pid):
            graph[u].append(v)

        def dfs(node, res):
            res.append(node)
            for nei in graph[node]:
                dfs(nei, res)

        res = []
        dfs(kill, res)
        return res


class SolutionRika:
    def killProcess(self, pid, ppid, kill):
        # BFS
        n = len(pid)
        hashmap = collections.defaultdict(list)  # {parent:child}
        for i in range(n):
            hashmap[ppid[i]].append(pid[i])

        res = []
        queue = collections.deque()
        queue.append(kill)

        while queue:
            node = queue.popleft()
            res.append(node)

            if node in hashmap:
                for child in hashmap[node]:
                    queue.append(child)
        return res


class Solution:
    def killProcess(self, pid, ppid, kill):
        graph = collections.defaultdict(list)
        for i, j in zip(ppid, pid):
            graph[i].append(j)

        res = []
        self.dfs(graph, kill, res)
        return res

    def dfs(self, graph, node, res):
        res.append(node)
        for nei in graph[node]:
            self.dfs(graph, nei, res)




