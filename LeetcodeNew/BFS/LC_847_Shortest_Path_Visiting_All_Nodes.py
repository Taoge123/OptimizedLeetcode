
"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/141666/10-lines-Python-Recursive-DP
https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/135736/python-DP-solution-with-detailed-explanation-example


An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node.
You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length

"""
import heapq
import collections

class SolutionHeapq:
    def shortestPathLength(self, graph):
        memo = set()
        final = (1 << len(graph)) - 1
        q = [(0, i, 1 << i) for i in range(len(graph))]

        while q:
            steps, node, state = heapq.heappop(q)
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    heapq.heappush(q, (steps + 1, v, state | 1 << v))
                    memo.add((state | 1 << v, v))



class SolutionBFS:
    def shortestPathLength(self, graph):
        memo, final, q, steps = set()
        final = (1 << len(graph)) - 1
        q = [(i, 1 << i) for i in range(len(graph))]
        steps = 0
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1




class SolutionDeque:
    def shortestPathLength(self, graph):
        memo, steps = set()
        final = (1 << len(graph)) - 1
        q = collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        steps = 0
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))



class Solution4:
    def shortestPathLength(self, g_list):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # If naive BFS, then we can't visit the visited node again, can't solve this issue
        # The key is to define the state of visited as (cur_node, visited_nodes)
        # If next to explore is the same node and same visisted then it is a loop, we then won't visit
        # in BFS algo
        graph = {}
        n = len(g_list)
        done = (1 << n) - 1
        for i, targets in enumerate(g_list):
            graph[i] = targets
        queue = collections.deque()
        # node => visited set mapping
        visited = collections.defaultdict(set)
        # Add all nodes to initial queue
        for i in range(n):
            # Use bit vector to represent visited nodes
            queue.appendleft((0, i, 1 << i))
        # BFS
        while queue:
            dist, cur_node, state = queue.pop()
            if state == done: return dist
            for next_node in graph[cur_node]:
                if state not in visited[next_node]:
                    visited[next_node].add(state)
                    queue.appendleft((dist+1, next_node, state | 1 << next_node))
        return -1

