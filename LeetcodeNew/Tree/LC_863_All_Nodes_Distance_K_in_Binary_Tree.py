
"""
https://www.youtube.com/watch?v=nPtARJ2cYrg
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/232773/Python-solution-using-two-DFS-beat-100-without-reconstruct-a-graph


We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

"""
"""
A recursive dfs funciton connect help to build up a map conn.
The key of map is node's val and the value of map is node's connected nodes' vals.
Then we do N times bfs search loop to find all nodes of distance K

"""
import collections

class Solution:
    def distanceK(self, root, target, K):
        conn = collections.defaultdict(list)
        def connect(parent, child):

            #build graph
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen |= set(bfs)
        return bfs



class Solution2:
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], set()
        def dfs(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)
        dfs(root)
        def dfs2(node, d):
            if d < K:
                visited.add(node)
                for v in adj[node]:
                    if v not in visited:
                        dfs2(v, d + 1)
            else:
                res.append(node.val)
        dfs2(target, 0)
        return res







