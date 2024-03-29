import collections

class SolutionTony:
    def canReach(self, arr, start):
        def dfs(node):
            if node < 0 or node >= len(arr):
                return False
            if arr[node] == 0:
                return True
            if node in visited:
                return False
            visited.add(node)
            prev = node - arr[node]
            nxt = node + arr[node]
            return dfs(prev) or dfs(nxt)

        visited = set()
        return dfs(start)




class SolutionDFS:
    def canReach(self, arr, start: int) -> bool:
        self.visited = [0] * 50001
        return self.dfs(arr, start)

    def dfs(self, arr, pos):
        if pos < 0 or pos >= len(arr):
            return False
        if arr[pos] == 0:
            return True
        if self.visited[pos] == 1:
            return False

        self.visited[pos] = 1
        if self.dfs(arr, pos - arr[pos]):
            return True
        if self.dfs(arr, pos + arr[pos]):
            return True

        return False




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

