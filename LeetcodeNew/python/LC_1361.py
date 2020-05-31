
"""
https://leetcode.com/problems/validate-binary-tree-nodes/discuss/518538/C%2B%2BPython-Simple-idea-beat-100-with-O(N)-TimeSpace-%2B-bonus-3-line

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









