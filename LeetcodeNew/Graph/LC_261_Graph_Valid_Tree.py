
"""

http://www.cnblogs.com/grandyang/p/5257919.html
https://www.geeksforgeeks.org/topological-sorting/
https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/


Given n nodes labeled from 0 to n-1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check
whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.


"""
"""
Step-1: Compute in-degree (number of incoming edges) 
for each of the vertex present in the DAG and initialize the count of visited nodes as 0.

Step-2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)

Step-3: Remove a vertex from the queue (Dequeue operation) and then.

    - Increment count of visited nodes by 1.
    - Decrease in-degree by 1 for all its neighboring nodes.
    - If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.

Step 4: Repeat Step 3 until the queue is empty.

Step 5: If count of visited nodes is not equal to the number of nodes in the graph then the topological sort is not possible for the given graph.

How to find in-degree of each node?
There are 2 ways to calculate in-degree of every vertex:
Take an in-degree array which will keep track of
1) Traverse the array of edges and simply increase the counter of the destination node by 1.

for each node in Nodes
    indegree[node] = 0;
for each edge(src,dest) in Edges
    indegree[dest]++

Time Complexity: O(V+E)


2) Traverse the list for every node and then increment the in-degree of all the nodes connected to it by 1.

    for each node in Nodes
        If (list[node].size()!=0) then
        for each dest in list
            indegree[dest]++;



"""

"""
This solution looks like topological-sort, which iteratively removes the nodes with degree of 1.
The base condition is that a single node with no edges is a tree. 
By induction, if the graph is a tree, with the leaves removed, 
the rest part of it is still a tree.

下面我们来看BFS的解法，思路很相近，需要用queue来辅助遍历，
这里我们没有用一维向量来标记节点是否访问过，而是用了一个set，如果遍历到一个节点，
在set中没有，则加入set，如果已经存在，则返回false，还有就是在遍历邻接链表的时候，
遍历完成后需要将节点删掉，参见代码如下：

"""


"""
这道题给了我们一个无向图，让我们来判断其是否为一棵树，我们知道如果是树的话，所有的节点必须是连接的，
也就是说必须是连通图，而且不能有环，所以我们的焦点就变成了验证是否是连通图和是否含有环。
我们首先用DFS来做，根据pair来建立一个图的结构，用邻接链表来表示，
还需要一个一位数组v来记录某个节点是否被访问过，然后我们用DFS来搜索节点0，遍历的思想是，
当DFS到某个节点，先看当前节点是否被访问过，如果已经被访问过，说明环存在，直接返回false，
如果未被访问过，我们现在将其状态标记为已访问过，然后我们到邻接链表里去找跟其相邻的节点继续递归遍历，
注意我们还需要一个变量pre来记录上一个节点，以免回到上一个节点，这样遍历结束后，
我们就把和节点0相邻的节点都标记为true，然后我们在看v里面是否还有没被访问过的节点，如果有，
则说明图不是完全连通的，返回false，反之返回true
"""


# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         graph = collections.defaultdict(list)
#         visited = set()
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)

#         return not self.dfs(graph, visited, 0, -1) and n == len(visited)


#     def dfs(self, graph, visited, node, parent):
#         visited.add(node)
#         for i in graph[node]:
#             if i != parent:
#                 if i in visited or self.dfs(graph, visited, i, node):
#                     return True
#         return False


class Solution:
    def validTree(self, n: int, edges) -> bool:
        nums = [-1] * n
        for u, v in edges:
            if not self.union(nums, u, v):
                return False
        return len(edges) == n - 1

    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])

    def union(self, nums, i, j):
        x, y = self.find(nums, i), self.find(nums, j)
        if x == y:
            return False
        else:
            nums[x] = y
            return True


n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

a = Solution()
print(a.validTree(n, edges))