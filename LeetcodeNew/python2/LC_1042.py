

class Solution:
    def gardenNoAdj(self, N, paths):
        res = [0] * N
        graph = [[] for i in range(N)]

        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        for i in range(N):
            # Use 5 instead of 4 so we can easily use 1-based indexing of the garden colors
            colors = [0] * 5
            for nei in graph[i]:
                # Mark the color as used if neighbor has used it before.
                colors[res[nei]] = 1

            # Now just use a color that has not been used yet
            for c in range(4, 0, -1):
                # //colors[c] == 0 => the color has not been used yet,
                if not colors[c]:
                    # so let's use that one
                    res[i] = c

        return res


