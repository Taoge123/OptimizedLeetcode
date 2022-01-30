
"""
https://www.youtube.com/watch?v=mKUsbABiwBI
https://www.youtube.com/watch?v=kYcUIEQqL2Y
https://github.com/happygirlzt/algorithm-illustrations/blob/master/1192.%20Critical%20Connections%20in%20a%20Network.png

1. 找环， 一个环上面的任何一条边都不是critical connections
2。 如何O（n）找到所有的环
    1。DFS向前探索 ： 每个节点最多走一遍 （traversal）， 每走一步记录从远点走到当前节点的步数
    2。DFS探索返回 ： 返回当前节点所（间接） 接触到非父节点的最小步数的节点

"""



import collections


class SolutionDFS:
    def criticalConnections(self, n, connections):
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        jump = [-1] * n

        # starting from the current node, explore all the node connecting to this node except for its parent, and return the minimum value node
        def dfs(node, parent, step):

            jump[node] = step
            for nei in graph[node]:
                if nei == parent:
                    continue
                elif jump[nei] == -1:
                    jump[node] = min(jump[node], dfs(nei, node, step + 1))
                else:
                    jump[node] = min(jump[node], jump[nei])

            if jump[node] == step and node != 0:
                res.append([parent, node])

            return jump[node]

        res = []
        dfs(0, -1, 0)
        return res



class Solution:
    def criticalConnections(self, n: int, connections):

        graph = collections.defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        table = [float('inf')] * n

        res = []

        def dfs(node, parent, step):
            table[node] = step
            for child in graph[node]:
                if child == parent:
                    continue
                elif table[child] == float('inf'):
                    table[node] = min(table[node], dfs(child, node, step + 1))
                else:
                    table[node] = min(table[node], table[child])
            if table[node] == step and parent != -1:
                res.append([parent, node])
            return table[node]

        dfs(0, -1, 0)
        return res


