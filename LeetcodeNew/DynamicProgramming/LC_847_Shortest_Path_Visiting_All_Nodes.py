
"""
https://www.youtube.com/watch?v=Vo3OEN2xgwk
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

"""

"""
解题方法
方法一：BFS
话说看到这个题的第一感觉就是BFS，因为我们要找到遍历所有节点的最少步数，这个正是BFS擅长的。
唯一不同的就是这个题允许从多个顶点出发，也就是说没有了固定的起点。那么需要对BFS稍微改变一点，即在初始化的时候，
把所有顶点都放进队列之中，这样，每次把队列的元素pop出来一遍之后就是新的一轮循环，也就可以认为所有的节点都是同时向前迈进了一步。

这个题使用了一个的技巧，位运算。一般的BFS过程都是只保存访问过的节点即可，因为每个节点只可以使用一次，
但是这个题的节点可以访问多次，那么就是说必须维护一个实时的访问了哪些节点的状态。
按道理说，如果不使用位运算而是使用字典等方式保存访问过了的状态也可以，但是，看了给出的图的顶点个数只有12个，
哪怕一个int都会有32个bit够用，所以可以直接使用和图中顶点数相等的位数来保存这个状态是否访问过。这个状态怎么理解？
从每个顶点出发到达，所有访问过的节点是状态。也就是说这个状态是全局唯一的，每个顶点都有2 * N个状态表示它访问的其他节点。
有2 ^ N个bit，每个位都代表对应的节点是否访问过。最终的状态是(1 << N) - 1，即全是1，表示所有节点都访问了。

这个visited是个二维数组，保存的是每个节点的所有状态，对于该题目的BFS，有可能有N * 2^Ｎ个状态，
使用visited保存每个节点已经访问的状态，对应状态位置是0/1。

时间复杂度是O(N * (2^N))，空间复杂度是O(N * 2^Ｎ)。
"""
import collections
import heapq
import sys
from math import inf


class Solution1:
    def shortestPathLength(self, graph):

        N = len(graph)
        queue = collections.deque()
        step = 0
        goal = (1 << N) - 1
        visited = [[0 for j in range(1 << N)] for i in range(N)]
        for i in range(N):
            queue.append((i, 1 << i))
        while queue:
            s = len(queue)
            for i in range(s):
                node, state = queue.popleft()
                if state == goal:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = 1
                for nextNode in graph[node]:
                    queue.append((nextNode, state | (1 << nextNode)))
            step += 1
        return step


"""
解题思路：
Floyd + 动态规划（Dynamic Programming）

时间复杂度 O(2^n * n^2）

利用Floyd求出每对顶点i, j之间的最短距离，记为dp[i][j]，代价为O(N^3)

利用status[s][i]记录：状态为s，当前所在节点为i时的最小路径长度

状态s是二进制，表示各节点是否被访问过，1表示已访问，0表示未访问

状态转移方程：

status[ns][j] = min(status[ns][j], status[s][i] + dp[i][j])

其中ns表示从状态s的i点出发到达j点时的新状态
"""
class Solution2:
    def shortestPathLength(self, graph):

        INF = 0x7FFFFFFF
        N = len(graph)
        dp = [[INF] * N for x in range(N)]
        for i, e in enumerate(graph):
            dp[i][i] = 0
            for j in e:
                dp[i][j] = dp[j][i] = 1
        for z in range(N):
            for x in range(N):
                for y in range(N):
                    dp[x][y] = min(dp[x][y], dp[x][z] + dp[z][y])

        status = {(0, i) : 0 for i in range(N)}
        for s in range(1 << N):
            for i in range(N):
                if (s, i) not in status: continue
                v = status[(s, i)]
                for j in range(N):
                    ns = s | (1 << j)
                    if status.get((ns, j), INF) > v + dp[i][j]:
                        status[(ns, j)] = v + dp[i][j]
        return min(status[((1 << N) - 1, i)] for i in range(N))


# Heapq Solution
class Solution3:
    def shortestPathLength(self, graph):
        memo, final, q = set(), (1 << len(graph)) - 1, [(0, i, 1 << i) for i in range(len(graph))]
        while q:
            steps, node, state = heapq.heappop(q)
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    heapq.heappush(q, (steps + 1, v, state | 1 << v))
                    memo.add((state | 1 << v, v))


# BFS Solution
class Solution4:
    def shortestPathLength(self, graph):
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
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


# Deque Solution
class Solution5:
    def shortestPathLength(self, graph):
        memo, final, q, steps = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))]), 0
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))



"""
dp[state][node] means current state is state, where each bit means whether a node is visited or not,
 node is the current node we are at, and the value is steps to arrive at this state.

I found some testcases given doesn't satisfy that: if j is in graph[i], then i is in graph[j]. 
I fix it first.

"""


class Solution6:
    def shortestPathLength(self, graph):
        N = len(graph)
        # new_g = [set() for _ in range(N)]
        # for i in range(N):
        #     for j in graph[i]:
        #         new_g[i].add(j)
        #         new_g[j].add(i)
        # graph = new_g

        # M contains all states
        M = (1 << N)
        dp = [[sys.maxsize] * N for _ in range(M)]

        q = []
        for i in range(N):
            # initial states contains all nodes and related states with only one node visited.
            dp[1 << i][i] = 0
            q.append((i, 1 << i))

        # Do BFS
        while q:
            node, state = q.pop(0)
            steps = dp[state][node]
            for x in graph[node]:
                new_state = state | (1 << x)

                # Since all edges have equal distance, BFS is already optimal, so never overwrite
                if dp[new_state][x] == sys.maxsize:
                    dp[new_state][x] = steps + 1
                    q.append((x, new_state))

        # Return minimal steps in state 0b111111...1111
        return min(dp[-1])


class Solution7:
    def shortestPathLength(self, graph):
        # 1 <= graph.length <= 12
        # 0 <= graph[i].length < graph.length

        nodeCount = len(graph)

        # NOTE
        # We are using BFS here because it's better suited for 'shortest path'
        # types of problems. DFS solution is also viable though.

        # Thoughts:
        # 1. start at each node, do BFS to try reaching all other nodes.
        # 2. Must keep track of visited nodes, else infinite loop may happen.
        # 3. But each node may have to be visited multiple times, as described in the problem
        #    statement. So we cannot be too strict in limiting searches
        # 4. We must describe the state during a search, we need:
        #    - The current node we are on
        #    - Nodes we have visited (Notice the order does not matter in this case, that's a key)

        # each search is described by (currentNode, visited)
        # same search does have to be repeated, since if re-visited with
        # the same state, it would yield the same result.
        # NOTE this does not prevent revisiting the same node again,
        # it just prevents revisiting it with the same STATE!

        # Since the input size is restricted, we can use a number to encode
        # which nodes have been visited -- the i-th bit is on iff node i has been visited

        # conceptually masks[k] indicates that only node k has been visited
        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = collections.deque([(i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] iff
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            count = len(queue)

            while count:
                currentNode, visited = queue.popleft()
                if visited == allVisited:
                    return steps

                # start bfs from each neighbor
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_visited == allVisited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        # no path which explores every node
        return inf

class Solution9:
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


