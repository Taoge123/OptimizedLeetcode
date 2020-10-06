

class Solution:
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

