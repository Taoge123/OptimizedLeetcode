
"""
https://www.cnblogs.com/ZhaoxiCheung/p/LeetCode-SumofDistancesinTree.html

https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)
https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130574/Simple-recursive-python-solution
https://leetcode.com/problems/sum-of-distances-in-tree/solution/
https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130567/Two-traversals-O(N)-python-solution-with-Explanation
https://leetcode.com/problems/sum-of-distances-in-tree/discuss/132133/Intuition-of-O(n)-solution-based-on-%22undirected%22-tree
https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130654/Clean-Python-O(N)-solution-with-explanation
https://leetcode.com/problems/sum-of-distances-in-tree/discuss/161975/My-DFS-sulotion-two-passes


Intuition:
What if given a tree, with a certain root 0?
In O(N) we can find sum of distances in tree from root and all other nodes.
Now for all N nodes?
Of course, we can do it N times and solve it in O(N^2).
C++ and Java may get accepted luckly, but it's not what we want.

When we move our root from one node to its connected node,
one part of nodes get closer, one the other part get further.
If we know exactly hom many nodes in both parts, we can solve this problem.

With one single traversal in tree, we should get enough information for it
and don't need to do it again and again.

Explanation:
0. Let's solve it with node 0 as root.

Initial an array of hashset tree, tree[i] contains all connected nodes to i.
Initial an array count, count[i] counts all nodes in the subtree i.
Initial an array of res, res[i] counts sum of distance in subtree i.

Post order dfs traversal, update count and res:
count[root] = sum(count[i]) + 1
res[root] = sum(res[i]) + sum(count[i])

Pre order dfs traversal, update res:
When we move our root from parent to its child i,
count[i] points get 1 closer to root, n - count[i] nodes get 1 futhur to root.
res[i] = res[root] - count[i] + N - count[i]

return res, done.

"""

import collections

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans


class Solution2:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [0] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def sumDistancesToRoot(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    sumDistancesToRoot(i, seen)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
            count[root] += 1

        def otherSumsBasedOnRoot(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    res[i] = res[root] - count[i] + N - count[i]
                    otherSumsBasedOnRoot(i, seen)
        sumDistancesToRoot()
        otherSumsBasedOnRoot()
        return res













