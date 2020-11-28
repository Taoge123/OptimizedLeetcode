
class Solution:
    def earliestAcq(self, logs, N: int) -> int:
        parent = [i for i in range(N)]
        logs = sorted(logs)

        for time, i, j in logs:
            if self.union(i, j, parent):
                N -= 1
            if N == 1:
                return time
        return -1

    def find(self, i, parent):
        if i == parent[i]:
            return parent[i]
        return self.find(parent[i], parent)

    def union(self, i, j, parent):
        x = self.find(i, parent)
        y = self.find(j, parent)
        if x == y:
            return False
        else:
            parent[x] = y
            return True


        