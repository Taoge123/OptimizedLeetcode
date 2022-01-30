
import collections






class SolutionDFS2:
    def gardenNoAdj(self, n, paths):
        graph = collections.defaultdict(list)
        for i, j in paths:
            graph[i].append(j)
            graph[j].append(i)

        colors = [0] * (n + 1)

        def dfs(node):
            visited = set()
            # add non-zero color into visited
            for nei in graph[node]:
                if colors[nei] == 0:
                    continue
                visited.add(colors[nei])

            for color in range(1, 5):
                if color not in visited:
                    colors[node] = color
                    break

            for nei in graph[node]:
                if graph[nei] == 0:
                    dfs(nei)

        for i in range(1, n + 1):
            if colors[i] == 0:
                dfs(i)
        return colors[1:]




class SolutionDFS222:
    def gardenNoAdj(self, n, paths):

        graph = collections.defaultdict(list)
        for i, j in paths:
            graph[i].append(j)
            graph[j].append(i)

        flower = [0 for i in range(n + 1)]

        def dfs(node):
            visited = set()
            for nei in graph[node]:
                if flower[nei] != 0:
                    visited.add(flower[nei])

            for color in range(1, 5):
                if color not in visited:
                    flower[node] = color

        for i in range(1, n + 1):
            dfs(i)
        return flower[1:]



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


