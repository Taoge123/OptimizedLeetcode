
"""

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced,
could you solve it in less than O(n) runtime (where n = total nodes)?


https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70556/Simple-DFS-%2B-Priority-Queue-Python-Solution

https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70573/Clear-Python-O(klogn)-Solution-with-Two-Stacks


Step 1. Binary search for target until node==None or node.val == target, record path
Step 2. For path node, if node.val>=target, add to stack Pred; otherwise(node.val<=target) add to stack Succ
Step 3. Stack tops are possible nearest element
Step 4. Compare both stack for nearest element and then "iterate" the stack

一开始思路非常不明确，看了不少discuss也不明白为什么。在午饭时间从头仔细想了一下，
像Closest Binary Search Tree Value I一样，追求O(logn)的解法可能比较困难，
但O(n)的解法应该不难实现。我们可以使用in-order的原理，从最左边的元素开始，
维护一个Deque或者doubly linked list，将这个元素的值从后端加入到Deque中，然后继续遍历下一个元素。
当Deque的大小为k时， 比较当前元素和队首元素与target的差来尝试更新deque。
循环结束条件是队首元素与target的差更小或者遍历完全部元素。这样的话时间复杂度是O(n)， 空间复杂度应该是O(k)。

Time Complexity - O(n)， Space Complexity - O(k)


"""
import heapq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        res = collections.deque([])
        self.dfs(root, target, res, k)
        return res

    def dfs(self, root, target, res, k):
        if not root:
            return

        self.dfs(root.left, target, res, k)
        if len(res) == k:
            if abs(root.val - target) < abs(res[0] - target):
                res.popleft()
            else:
                return
        res.append(root.val)
        self.dfs(root.right, target, res, k)


