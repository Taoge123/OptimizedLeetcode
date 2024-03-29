import collections


class SolutionRika:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        # build graph --> {bus_stop: bus_id}
        valid = False
        stop_to_bus = collections.defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                if stop == target:
                    valid = True
                stop_to_bus[stop].append(i)
        if not valid:
            return -1

        queue = collections.deque()
        queue.append(source)
        step = 0
        visited = set()
        visited.add(source)

        while queue:
            size = len(queue)
            for _ in range(size):
                cur_stop = queue.popleft()

                if cur_stop == target:
                    return step

                for nxt_bus in stop_to_bus[cur_stop]:
                    for nxt_stop in routes[nxt_bus]:
                        if nxt_stop not in visited:
                            queue.append(nxt_stop)
                            visited.add(nxt_stop)
            step += 1
        return -1




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


class SolutionCs:
    def numBusesToDestination(self, routes, S: int, T: int) -> int:

        if S == T:
            return 0

        table = collections.defaultdict(list)

        for i in range(len(routes)):
            for j in range(len(routes[i])):
                buses = table[routes[i][j]]
                buses.append(i)
                table[routes[i][j]] = buses
        visited = set()
        queue = collections.deque()
        queue.append(S)

        res = 0
        while queue:
            res += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                buses = table[node]
                for bus in buses:
                    if bus in visited:
                        continue
                    visited.add(bus)
                    for j in range(len(routes[bus])):
                        if routes[bus][j] == T:
                            return res
                        queue.append(routes[bus][j])
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


