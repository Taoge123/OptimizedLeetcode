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
