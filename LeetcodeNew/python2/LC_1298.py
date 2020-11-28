
import collections


class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes) -> int:

        found = [0] * len(status)
        hasKeys = status
        queue = collections.deque()

        for box in initialBoxes:
            found[box] = 1
            if hasKeys[box]:
                queue.append(box)

        res = 0
        while queue:
            box = queue.popleft()
            res += candies[box]
            for t in containedBoxes[box]:
                found[t] = 1
                if hasKeys[t]:
                    queue.append(t)

            for t in keys[box]:
                if not hasKeys[t] and found[t]:
                    queue.append(t)
                hasKeys[t] = 1

        return res




class SolutionWisdom:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes) -> int:

        queue = collections.deque()
        for b in initialBoxes:
            queue.append(b)

        hasKeys = set()
        res = 0
        opened = 1

        while queue and opened == 1:
            n = len(queue)
            opened = 0
            for i in range(n):
                b = queue.popleft()
                # box is closed and no key, then we can't open it, throw it back to the queue and wait for next time
                if status[b] == 0 and b not in hasKeys:
                    queue.append(b)

                else:
                    opened = 1
                    res += candies[b]
                    for k in keys[b]:
                        hasKeys.add(k)
                    for newB in containedBoxes[b]:
                        queue.append(newB)
        return res
