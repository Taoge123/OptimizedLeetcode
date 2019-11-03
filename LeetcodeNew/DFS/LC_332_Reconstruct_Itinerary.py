
"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.




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

        graph = collections.defaultdict(list)

        for u, v in tickets:
            heapq.heappush(graph[u], v)
        start = 'JFK'
        res = []
        self.dfs(graph, start, res)
        return res[::-1]

    def dfs(self, graph, start, res):
        while graph[start]:
            node = heapq.heappop(graph[start])
            self.dfs(graph, node, res)
        res.append(start)



"""
defaultdict(<class 'list'>, {'EZE': ['AXA', 'TIA', 'JFK'], 'AUA': ['EZE'], 'JFK': ['ANU', 'ANU', 'AUA'], 'AXA': ['TIA'], 'TIA': ['AUA', 'JFK'], 'ANU': ['EZE', 'EZE']})
defaultdict(<class 'list'>, {'EZE': ['AXA', 'JFK', 'TIA'], 'AUA': ['EZE'], 'JFK': ['ANU', 'ANU', 'AUA'], 'AXA': ['TIA'], 'TIA': ['AUA', 'JFK'], 'ANU': ['EZE', 'EZE']})

"""

tickets = [["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]]

a = Solution()
print(a.findItinerary(tickets))



