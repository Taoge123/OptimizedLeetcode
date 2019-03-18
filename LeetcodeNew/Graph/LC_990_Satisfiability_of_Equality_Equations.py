
"""
Given an array equations of strings that represent relationships between variables,
each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.



Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied,
but not the second.  There is no way to assign the variables to satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:

Input: ["a==b","b==c","a==c"]
Output: true
Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false
Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true

"""


"""
Intuition:
We have 26 nodes in the graph.
All "==" equations actually represent the connection in the graph.
The connected nodes should be in the same color/union/set.

Then we check all inequations.
Two inequal nodes should be in the different color/union/set.

Explanation
We can solve this problem by DFS or Union Find.

Firt pass all "==" equations.
Union equal letters together
Now we know which letters must equal to the others.

Second pass all "!=" inequations,
Check if there are any contradict happens.

Time Complexity:
Union Find Operation, amortized O(1)
First pass all equations, O(N)
Second pass all inequations, O(N)

Overall O(N)
"""

import string
import collections


class Solution:
    def equationsPossible(self, equations):
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in string.lowercase}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)

class Union_find:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1

    def same_group(self, x, y):
        return self.find(x) == self.find(y)


class Solution2:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        same_group = [(eq[0], eq[3]) for eq in equations if eq[1] == '=']
        diff_group = [(eq[0], eq[3]) for eq in equations if eq[1] == '!']
        uniq = set()
        for g in same_group:
            uniq.add(g[0])
            uniq.add(g[1])
        m = {val: idx for idx, val in enumerate(list(uniq))}
        uf = Union_find(len(uniq))
        for x, y in same_group:
            uf.union(m[x], m[y])

        for x, y in diff_group:
            if x == y: return False
            if x not in m or y not in m:
                continue
            if uf.same_group(m[x], m[y]):
                return False
        return True



class SolutionDFS:
    def equationsPossible(self, equations):
        graph = [[] for _ in range(26)]

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [None] * 26
        t = 0
        for start in range(26):
            if color[start] is None:
                t += 1
                stack = [start]
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if color[nei] is None:
                            color[nei] = t
                            stack.append(nei)

        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                if x == y: return False # lee
                if color[x] is not None and color[x] == color[y]:
                    return False
        return True

"""
Bascially we are making a graph.
If a == b we will have two edges: a->b and b->a.
After we construct the graph, we check all the x != y
and make sure they are not able to visit each other.
"""


class Solution3:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        graph = collections.defaultdict(set)
        notEquals = []

        def canMeet(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for v in graph[u]:
                if v in visited:
                    continue
                if canMeet(v, target, visited):
                    return True
            return False

        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq.split('!=')
                notEquals.append((a, b))
                continue
            u, v = eq.split('==')
            graph[u].add(v)
            graph[v].add(u)

        for u, v in notEquals:
            if canMeet(u, v, set()):
                return False
        return True



