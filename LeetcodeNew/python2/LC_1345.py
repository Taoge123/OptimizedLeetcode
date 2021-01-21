
import collections


class Solution:
    def minJumps(self, arr) -> int:

        table = collections.defaultdict(list)
        n = len(arr)

        for i, num in enumerate(arr):
            # optimization 1
            if (i > 0) and (i < n - 1) and (num == arr[i - 1] == arr[i + 1]):
                continue

            table[num].append(i)

        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == n - 1:
                    return step

                for pos in [node - 1, node + 1] + table[arr[node]]:
                    if pos in visited:
                        continue
                    if pos < 0 or pos >= n:
                        continue
                    queue.append(pos)
                    visited.add(pos)
                del table[arr[node]]
            step += 1

        return 0


class SolutionTony:
    def minJumps(self, arr) -> int:
        table = collections.defaultdict(list)
        n = len(arr)
        for i, num in enumerate(arr):
            if (i > 0) and (i < n - 1) and (num == arr[i - 1] == arr[i + 1]):
                continue
            table[num].append(i)

        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        step = 0
        while queue:

            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == n - 1:
                    return step

                for pos in [node - 1, node + 1] + table[arr[node]]:
                    if pos in visited:
                        continue

                    if 0 <= pos <= len(arr) - 1:
                        visited.add(pos)
                        queue.append(pos)
            step += 1
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







