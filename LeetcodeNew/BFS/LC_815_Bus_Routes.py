"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

"""
"""
One difficulty is to efficiently decide whether two buses are connected by an edge. 
They are connected if they share at least one bus stop. 
Whether two lists share a common value can be done by set intersection (HashSet), 
or by sorting each list and using a two pointer approach.

To make our search easy, 
we will annotate the depth of each node: info[0] = node, info[1] = depth.
"""

import collections


"""
The first part loop on routes and record stop to routes mapping in to_route.
The second part is general bfs. Take a stop from queue and find all connected route.
The set seen record all stops visted and we won't check a stop for twice.
We can also use a set to record all routes visted , or just clear a route after visit.
"""

class SolutionLee:
    def numBusesToDestination(self, routes, S, T):
        graph = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                graph[j].add(i)
        bfs = [(S,0)]
        seen = set([S])
        for stop, depth in bfs:
            if stop == T:
                return depth
            for i in graph[stop]:
                for next in routes[i]:
                    if next not in seen:
                        bfs.append((next, depth+1))
                        seen.add(next)
                routes[i] = []
        return -1





class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        queue = collections.deque()
        graph = collections.defaultdict(set)
        routes = list(map(set, routes))
        seen, targets = set(), set()
        for i in range(len(routes)):
            if S in routes[i]:  # possible starting route number
                seen.add(i)
                queue.append((i, 1))  # enqueue
            if T in routes[i]:  # possible ending route number
                targets.add(i)
            for j in range(i+1, len(routes)):
                if routes[j] & routes[i]:  # set intersection to check if route_i and route_j are connected
                    graph[i].add(j)
                    graph[j].add(i)
        while queue:
            cur, count = queue.popleft()
            if cur in targets:
                return count
            for nei in graph[cur]:
                if nei not in seen:
                    queue.append((nei, count+1))
                    seen.add(nei)
        return -1





class Solution2:
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        routes = map(set, routes)
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1




