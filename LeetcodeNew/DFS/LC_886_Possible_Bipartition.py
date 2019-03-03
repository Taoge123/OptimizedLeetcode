
"""
https://leetcode.com/problems/possible-bipartition/discuss/160371/Python-Decide-if-a-graph-is-bipartite-by-checking-the-existence-of-odd-cycles.
https://www.geeksforgeeks.org/bipartite-graph/

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

            0 ^ 0 = 0
            0 ^ 1 = 1
            1 ^ 0 = 1
            1 ^ 1 = 0

"""
import collections

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            #c ^ 1 check if its the same with 1,
            #Each node, for all its neighbors
            return all(dfs(nei, c ^ 1) for nei in graph[node])
        #For all nodes
        return all(dfs(node) for node in range(1, N+1) if node not in color)


class Solution2:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Create an undirected graph where vertices are "N" people and edges are
        # the dislikes between people.
        neighbor_list = [[] for _ in range(N)]
        for dislike in dislikes:
            # The vertex index starts from "0".
            neighbor_list[dislike[0] - 1].append(dislike[1] - 1)
            neighbor_list[dislike[1] - 1].append(dislike[0] - 1)

        # People can be partitioned into two groups if and only if the graph is
        # bipartite where:
        # (1) vertices can be partitioned into two groups;
        # (2) no edges are within each group and all edges connect two nodes in
        # different groups.
        # It can be shown that a graph is bipartite if and only if it contains no
        # odd cycles. The detailed proof can be found at:
        # https://proofwiki.org/wiki/Graph_is_Bipartite_iff_No_Odd_Cycles
        def isOddCyclic(curr, parent, path, path_len, visited):
            """Detects if the undirected graph has an odd cycle."""
            visited[curr] = True
            # path = the dict from the vertex to its index in the "path".
            path[curr] = path_len

            for neighbor in neighbor_list[curr]:
                if not visited[neighbor]:
                    # Recursively check if the neighbor has an odd cycle.
                    if isOddCyclic(neighbor, curr, path, path_len + 1, visited):
                        return True
                elif neighbor != parent:
                    # If we see a vertex other than the parent, we have found a cycle.
                    if neighbor in path and (path_len - path[neighbor]) % 2 == 0:
                        return True

            path.pop(curr)
            return False

        path = {}
        visited = [False] * N
        for i in range(N):
            if not visited[i] and isOddCyclic(i, -1, path, 0, visited):
                return False

        return True


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)
        color = [0] * N
        for i in range(N):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        bfs.append(e)
        return True
# ---------------------
# 作者：负雪明烛
# 来源：CSDN
# 原文：https://blog.csdn.net/fuxuemingzhu/article/details/82827177
# 版权声明：本文为博主原创文章，转载请附上博文链接！

