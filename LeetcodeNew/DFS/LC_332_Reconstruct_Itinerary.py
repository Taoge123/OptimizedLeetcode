
"""
Explanation

First keep going forward until you get stuck. That's a good main path already.
Remaining tickets form cycles which are found on the way back and get merged into that main path.
By writing down the path backwards when retreating from recursion,
merging the cycles into the main path is easy - the end part of the path has already been written,
the start part of the path hasn't been written yet, so just write down the cycle now
and then keep backwards-writing the path.


Example:

enter image description here

From JFK we first visit JFK -> A -> C -> D -> A. There we're stuck,
so we write down A as the end of the route and retreat back to D.
There we see the unused ticket to B and follow it: D -> B -> C -> JFK -> D.
Then we're stuck again, retreat and write down the airports while doing so:
Write down D before the already written A, then JFK before the D, etc.
When we're back from our cycle at D, the written route is D -> B -> C -> JFK -> D -> A.
Then we retreat further along the original path, prepending C, A and finally JFK to the route,
ending up with the route JFK -> A -> C -> D -> B -> C -> JFK -> D -> A.
"""

import collections
import heapq

class Solution:
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)
        for flight in tickets:
            d[flight[0]] += flight[1],
        self.route = ["JFK"]

        def dfs(start='JFK'):
            myDsts = sorted(d[start])
            for dst in myDsts:
                d[start].remove(dst)
                self.route += dst,
                dfs(dst)
                if len(self.route) == len(tickets) + 1:
                    return self.route
                self.route.pop()
                d[start] += dst,

        return dfs()


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = collections.defaultdict(list)
        for u, v in tickets: G[u].append(v)
        for u in G: G[u].sort()

        route = []

        def dfs(at):
            while G[at]:
                to = G[at].pop(0)
                dfs(to)
            route.append(at)

        dfs("JFK")
        return route[::-1]



class Solution:
    def findItinerary(self, tickets):
        graph, stack, reached = collections.defaultdict(list), ["JFK"], []
        for a, b in tickets: heapq.heappush(graph[a], b)
        while stack:
            if graph[stack[-1]]: stack.append(heapq.heappop(graph[stack[-1]]))
            else: reached.append(stack.pop())
        return reached[::-1]










