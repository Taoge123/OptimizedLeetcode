import collections


class Solution:
    def numBusesToDestination(self, routes, S: int, T: int) -> int:
        if S == T:
            return 0
        stopToBus = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                stopToBus[j].append(i)

        queue = collections.deque()
        queue.append(S)
        step = -1
        visitedStop = {S}
        visitedBus = set()

        while queue:
            size = len(queue)
            step += 1
            for i in range(size):
                stop = queue.popleft()

                # routs is bus to stop, we need stop to bus
                for bus in stopToBus[stop]:
                    if bus in visitedBus:
                        continue
                    visitedBus.add(bus)
                    for nextStop in routes[bus]:
                        if nextStop in visitedStop:
                            continue
                        if nextStop == T:
                            return step + 1

                        queue.append(nextStop)
                        visitedStop.add(nextStop)

        return -1





class SolutionTLE:
    def numBusesToDestination(self, routes, S: int, T: int) -> int:
        if S == T:
            return 0
        stopToBus = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                stopToBus[j].append(i)

        queue = collections.deque()
        queue.append(S)
        step = -1
        visited = set()
        visited.add(S)

        while queue:
            size = len(queue)
            step += 1
            for i in range(size):
                stop = queue.popleft()

                # routs is bus to stop, we need stop to bus
                for bus in stopToBus[stop]:
                    for nextStop in routes[bus]:
                        if nextStop in visited:
                            continue
                        if nextStop == T:
                            return step + 1

                        queue.append(nextStop)
                        visited.add(nextStop)

        return -1




"""
Explanation:
The first part loop on routes and record stop to routes mapping in to_route.
The second part is general bfs. Take a stop from queue and find all connected route.
The hashset seen record all visited stops and we won't check a stop for twice.
We can also use a hashset to record all visited routes, or just clear a route after visit.

"""

class SolutionLee:
    def numBusesToDestination(self, routes, S, T):
        stopToBus = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                stopToBus[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T:
                return bus
            for i in stopToBus[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # seen route
        return -1


