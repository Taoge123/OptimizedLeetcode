
"""

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11



https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
https://leetcode.com/problems/path-sum-iii/discuss/170367/Python-solution
https://leetcode.com/problems/path-sum-iii/discuss/170367/Python-solution

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

1. Brute Force: O(nlogn) ~ O(n^2)
1.1 High level walk-through:
(Define return) Define a global var: self.numOfPaths in the main function.
(1st layer DFS) Use recursive traverse to go through each node (can be any order: pre, in, post all fine).
(2nd layer DFS) For each node, walk all paths. If a path sum equals to the target: self.numOfPaths += 1
Return result: return self.numOfPaths

"""

"""
2. Memorization of path sum: O(n)
2.1 High level walk through
    1. In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
    2. This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
    3. Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
    4. We just need to add the frequency of the oldPathSum to the result.
    5. During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
    6. Check the graph below for easy visualization.

"""



"""
Two Sum Method: Optimized Solution

- A more efficient implementation uses the Two Sum idea. It uses a hash table (extra memory of order N). With more space, it gives us an O(N) complexity.
- As we traverse down the tree, at an arbitrary node N, we store the sum until this node N (sum_so_far (prefix) + N.val). in hash-table. Note this sum is the sum from root to N.
- Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.We pass in our recursive routine.
- How do we know if we have a path of target sum which ends at this grand-child G? Say there are multiple such paths that end at G and say they start at A, B, C where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target. Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement at G as sum_so_far+G.val-target and look up the hash-table for the number of paths which had this sum
- Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.
"""
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def helper(self, root, target):
        if not root:
            return 0
        left = self.helper(root.left, target - root.val)
        right = self.helper(root.right, target - root.val)
        return left + right + int(root.val == target)



    def pathSum2(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        self.helper(root, cache, 0, sum)
        return self.result

    def helper(self, root, cache, curSum, sum):
        if not root:
            return

        curSum += root.val
        oldSum = curSum - sum
        self.result += cache[oldSum]
        cache[curSum] += 1
        self.helper(root.left, cache, curSum, sum)
        self.helper(root.right, cache, curSum, sum)
        cache[curSum] -= 1


tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right= TreeNode(-3)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(2)
tree.right.right = TreeNode(11)
tree.left.left.left = TreeNode(3)
tree.left.left.right = TreeNode(-2)

a = Solution2()
print(a.pathSum(tree, 8))


