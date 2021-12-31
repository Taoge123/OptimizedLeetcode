"""
https://leetcode.com/problems/validate-binary-tree-nodes/discuss/518538/C%2B%2BPython-Simple-idea-beat-100-with-O(N)-TimeSpace-%2B-bonus-3-line
https://leetcode.com/problems/validate-binary-tree-nodes/discuss/839149/Python-Topological-Sort-solution

Example 1:

    0
  /   \
 1     2
       /
	  3

Table 1:
Node   leftChild     rightChild
0           1            2
1          -1           -1
2           3           -1
3          -1           -1
Observation:

Node 0 does not appear as child, so it is root
Node 1, 2, 3 all apear once and only once, so these n-1 are all the necessary non-root nodes
1)+2) ensure Node 0~4 forms a valid tree.
Bonus:
If you watch closely, then you will find for a valid tree,
3) 0, 1, ~ (n-1) should appear only once as a child, i.e., appeaer in the last two columns of Table 1. The only node dose not appear is the root.
In another words, you should expect:
-1 appear (n+1) times
and
Out of the n number of: 0, 1, (n-1)
(n-1) numbers appear and only one is missing and we noted the missing one as root.
As a valid tree, the

P.S.:

A test case missing from OJ:
1
[-1]
[-1]

Intuition:
For a valid tree, each node can be child only once except the root, which can not be the child
Or equivalently,
A valid tree must have nodes with only one parent and exactly one node with no parent.
Or equivalently，
For a valid tree, the indgree of each node must be 1 except the root, whose indgree is 0

Complexity:
Time: O(N); Space:O(N)
"""

import collections


class SolutionDFS:
    def validateBinaryTreeNodes(self, n, left, right):
        visited = collections.defaultdict(int)
        indegree = collections.defaultdict(int)
        visited[-1] = 1

        def has_cycle(node):
            if visited[node] == 1:
                indegree[node] += 1
                return False
            if visited[node] == -1:
                return True
            visited[node] = -1
            if has_cycle(left[node]) or has_cycle(right[node]):
                return True
            visited[node] = 1
            return False

        # Return false if any cycles are detected
        if any(has_cycle(node) for node in range(n)):
            return False

        # Return true if there is exactly 1 root and all other nodes have exactly 1 parent
        count = 0
        for u in range(n):
            if indegree[u] > 1:
                return False
            if indegree[u] == 0:
                count += 1
        return count == 1




class SolutionTopo:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild):
        # Topological sort solution
        # step 1: compute indegree of each node
        indegree = [0] * n
        for num in leftChild + rightChild:
            if num != -1:
                indegree[num] += 1
        # step 2: find the root node (i.e.indegree == 0)
        indegree0 = []
        for num, d in enumerate(indegree):
            if d == 0:  # i.e. root node
                indegree0.append(num)
            if d > 1:  # i.e. the node have more than one parent
                return False

        if len(indegree0) > 1:  # i.e. more than one root
            return False

        # topological sort via BFS
        while indegree0:
            n -= len(indegree0)
            nxt = []
            for num in indegree0:
                l, r = leftChild[num], rightChild[num]
                if l != -1:
                    indegree[l] -= 1
                    if indegree[l] == 0:
                        nxt.append(l)
                if r != -1:
                    indegree[r] -= 1
                    if indegree[r] == 0:
                        nxt.append(r)
            indegree0 = nxt
        return n == 0




class Solution:
    def validateBinaryTreeNodes(self, n, left, right):
        visited = collections.defaultdict(int)
        indegree = collections.defaultdict(int)
        visited[-1] = 1

        # Return false if any cycles are detected
        if any(self.has_cycle(visited, indegree, left, right, node) for node in range(n)):
            return False

        # Return true if there is exactly 1 root and all other nodes have exactly 1 parent
        count = 0
        for u in range(n):
            if indegree[u] > 1:
                return False
            if indegree[u] == 0:
                count += 1
        return count == 1

    def has_cycle(self, visited, indegree, left, right, node):
        if visited[node] == 1:
            indegree[node] += 1
            return False
        if visited[node] == -1:
            return True
        visited[node] = -1
        if self.has_cycle(visited, indegree, left, right, left[node]) or self.has_cycle(visited, indegree, left, right,
                                                                                        right[node]):
            return True
        visited[node] = 1
        return False


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        table = {i for i in range(n)}
        inDegree = [0] * n
        for children in zip(leftChild, rightChild):
            for child in children:
                if child >= 0:
                    inDegree[child] += 1
                    if inDegree[child] > 1:
                        return False
                    table.discard(child)
        table = list(table)
        if len(table) > 0 and (leftChild[table[0]] == -1 and rightChild[table[0]] == -1) and table[0] != 0:  # condition
            return False

        return len(table) == 1


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find the root node, assume root is node(0) by default
        # a node without any parent would be a root node
        # note: if there are multiple root nodes => 2+ trees
        root = 0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i

        # keep track of visited nodes
        visited = set()
        # queue to keep track of in which order do we need to process nodes
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False

            # mark visited
            visited.add(node)

            # process node
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])

        # number of visited nodes == given number of nodes
        # if n != len(visited) => some nodes are unreachable/multiple different trees
        return len(visited) == n

