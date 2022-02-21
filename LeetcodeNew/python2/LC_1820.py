"""
https://www.youtube.com/watch?v=beVpSBo7FZk&t=268s

https://leetcode.com/problems/maximum-number-of-accepted-invitations/discuss/1700939/Python-Hungarian-algorithm
https://leetcode.com/problems/maximum-number-of-accepted-invitations/discuss/1149870/C%2B%2B-Hungrian-algorithm-(DFS-version)-w-introduction
https://leetcode.com/problems/maximum-number-of-accepted-invitations/discuss/1148032/Python-A-very-simple-Hungarian-implementation
An agumenting path is a path starting from a unpaired node on the left, ending at a unpaired node on the right, and consists of several unused edges and used edges alternatively (i.e. unused edge->used edge->unused edge->...). Note that the number of unsed edges is always larger than the number of used edges by 1.

For a certain unpaired left node A, we use DFS to find one augmenting path. Then along this path, we flip the used edges to be unused, and the unused edges to be used. There would be the following consequences:

No invalidity would be introduced, which means no node would be paired with two other nodes simutaneously.
The number of used edges must be more than the number of unused edges by 1. It means we improved our objective (have one more node pair).
The starting point A has now been paired.
If we are not able to find such an augmenting path for this starting point A , it means there is no way to get A paird with others while making the overal objective better.


"""


import collections


class SolutionTony:
    def maximumInvitations(self, grid):
        m, n = len(grid), len(grid[0])
        girls = [-1] * n

        def dfs(u, visited):
            for v in range(n):
                if grid[u][v] == 0 or v in visited:
                    continue
                visited.add(v)
                if girls[v] < 0 or dfs(girls[v], visited):
                    girls[v] = u
                    return True
            return False

        count = 0
        for u in range(m):
            visited = set()
            if dfs(u, visited):
                count += 1
        return count




class SolutionHungarian1:
    def maximumInvitations(self, grid):

        m, n = len(grid), len(grid[0])
        matched = [-1] * (m+n)
        graph = collections.defaultdict(list)

        for boy in range(m):
            for girl in range(n):
                if grid[boy][girl]:
                    graph[boy].append(m+girl)
                    graph[m+girl].append(boy)

        def dfs(node, visited):
            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                if matched[nei] < 0 or dfs(matched[nei], visited):
                    matched[nei] = node
                    matched[node] = nei
                    return True
            return False

        res = 0
        for node in range(m+n):
            if matched[node] < 0 and dfs(node, set()):
                res += 1
        return res


class SolutionHungarian2:
    def maximumInvitations(self, grid):
        m, n = len(grid), len(grid[0])
        matching = [-1] * n  # girls' mate

        def dfs(node, visited):
            # ask each girl
            for nei in range(n):
                # a potential mate; the girl has not been asked before
                if grid[node][nei] and not visited[nei]:
                    # mark her as asked
                    visited[nei] = True
                    # if the girl does not have a mate or her mate can be matched to someone else
                    if matching[nei] == -1 or dfs(matching[nei], visited):
                        # we match her to the boy "node"
                        matching[nei] = node
                        return True
            return False

        res = 0
        for i in range(m):
            visited = [False] * n
            if dfs(i, visited):
                res += 1

        return res


