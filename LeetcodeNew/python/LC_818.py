
import collections


class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque()
        queue.append([0, 1])
        visited = set()
        visited.add((0, 1))
        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                pos, speed = queue.popleft()
                if pos == target:
                    return res

                nxt1 = [pos + speed, speed << 1]
                state1 = tuple(nxt1)
                if nxt1[0] >= 0 and state1 not in visited:
                    queue.append(nxt1)
                    visited.add(state1)

                if speed > 0:
                    nxt2 = [pos, -1]
                else:
                    nxt2 = [pos, 1]

                state2 = tuple(nxt2)
                if nxt2[0] >= 0 and state2 not in visited:
                    queue.append(nxt2)
                    visited.add(state2)
            res += 1
        return -1


