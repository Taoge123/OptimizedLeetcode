import collections


class SolutionBFS:
    def canReach(self, arr, start: int) -> bool:

        n = len(arr)
        queue = collections.deque()
        queue.append(start)
        visited = set()
        visited.add(start)

        while queue:
            node = queue.popleft()

            if arr[node] == 0:
                return True

            left = node - arr[node]
            right = node + arr[node]
            if 0 <= left < n and left not in visited:
                queue.append(left)
                visited.add(left)

            if 0 <= right < n and right not in visited:
                queue.append(right)
                visited.add(right)
        return False


