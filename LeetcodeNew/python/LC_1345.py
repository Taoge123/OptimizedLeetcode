
import collections

class Solution:
    def minJumps(self, arr) -> int:
        table = {}
        for i, num in enumerate(arr):
            if num not in table:
                table[num] = []
            table[num].append(i)

        queue = [0]
        visited = set([0])
        res = 0
        n = len(arr)

        while queue:
            newQueue = []
            size = len(queue)
            for i in range(size):
                node = queue.pop()
                if node == n-1:
                    return res
                for pos in table[arr[node]] + [node - 1, node + 1]:
                    if pos >= 0 and pos not in visited:
                        newQueue.append(pos)
                        visited.add(pos)

                table[arr[node]] = []
            res += 1
            queue = newQueue

        return -1



class Solution2:
    def minJumps(self, arr) -> int:
        table = collections.defaultdict(list)
        n = len(arr)
        for i, num in enumerate(arr):
            # - key optimization
            # - skip continous value, such as '77...77', only keep first and last 7
            if (i > 0) and (i < n - 1) and (num == arr[i - 1] == arr[i + 1]):
                continue
            table[num].append(i)

        visited = set([0])
        queue = [(0, 0)]
        step = 0
        while queue:
            node, step = queue.pop(0)

            # - check if touch the end
            if node == n - 1:
                return step

            for pos in [node - 1, node + 1] + table[arr[node]]:
                if pos in visited:
                    continue

                if 0 <= pos <= len(arr) - 1:
                    visited.add(pos)
                    queue.append((pos, step + 1))

        return 0


"""
step 1: queue = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ....}
step 2: queue = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ....}

"""


class SolutionWisdom:
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return 0

        queue = collections.deque()
        queue.append(0)
        visited = [0] * n
        visited[0] = 1

        table = collections.defaultdict(list)
        for i in range(n):
            table[arr[i]].append(i)

        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node + 1 < n and visited[node + 1] == 0:
                    queue.append(node + 1)
                    visited[node + 1] = 1

                if node - 1 >= 0 and visited[node - 1] == 0:
                    queue.append(node - 1)
                    visited[node - 1] = 1

                for nxt in table[arr[node]]:
                    if visited[nxt] == 0:
                        queue.append(nxt)
                        visited[nxt] = 1

                    # optimization
                    if nxt in table:
                        del table[nxt]

            step += 1
            if visited[n - 1] == 1:
                return step
        return -1







