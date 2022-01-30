
import collections


class SolutionTonyDFS:
    def numOfMinutes(self, n, headID, manager, informTime):

        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)

        self.res = 0
        def dfs(node, time):
            self.res = max(self.res, time)
            for nei in graph[node]:
                dfs(nei, time + informTime[node])

        dfs(headID, 0)
        return self.res



class SolutionTony:
    def numOfMinutes(self, n: int, headID: int, manager, informTime):

        self.res = 0
        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)

        queue = collections.deque()
        queue.append([headID, 0])
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node, time = queue.popleft()
                res = max(time, res)
                for nei in graph[node]:
                    queue.append([nei, time + informTime[node]])

        return res




class SolutionDFS:
    def numOfMinutes(self, n: int, headID: int, manager, informTime):
        # hashmap --> { manager: empoyees }
        self.res = 0
        graph = collections.defaultdict(list)

        for i in range(n):
            graph[manager[i]].append(i)

        self.res = 0
        self.dfs(graph, informTime, headID, 0)
        return self.res

    def dfs(self, graph, informTime, node, time):
        self.res = max(self.res, time)
        for nei in graph[node]:
            self.dfs(graph, informTime, nei, time + informTime[node])





