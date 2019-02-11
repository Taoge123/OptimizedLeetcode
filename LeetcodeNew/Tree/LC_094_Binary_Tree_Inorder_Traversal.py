"""
Usually when we do DFS, we pop a node from stack and push back its left
and right child. But we lose the information of the order.
To keep track of the order, we can push back into stack right-child,
current node, and left-child, so when we are done with left child (sub-tree),
we know who's its father. To avoid process the same node twice,
we push the VALUE of the current node to stack, instead of the node itself.
This way, every time we saw a number in the stack,
we know we are done with a left sub-tree and this number is what's in order.

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionBest:
    def inorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            if isinstance(node, int):
                ans.append(node)
                continue

            if node.right:  # if has right node, push into stack
                stack.append(node.right)

            stack.append(node.val)  # Push VALUE into stack, in between left and right

            if node.left:  # if has left node, push into stack
                stack.append(node.left)

        return ans



class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        cur=root
        while len(stack)>0 or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res

class Solution3:
    # iteratively
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right



class Solution2:
    # recursively
    def inorderTraversal1(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


class Solution3:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        cur = root
        while cur or stack:
          while cur: # travel to each node's left child, till reach the left leaf
            stack.append(cur)
            cur = cur.left
          cur = stack.pop() # this node has no left child
          res.append(cur.val) # so let's append the node value
          cur = cur.right # visit its right child --> if it has left child ? append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
        return res
