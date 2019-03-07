"""
Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7


Steps:

1. Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
2. Once the node is found, have to handle the below 4 cases
    - node doesn't have left or right - return null
    - node only has left subtree- return the left subtree
    - node only has right subtree- return the right subtree
    - node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        if not root:  # if root doesn't exist, just return it
            return root
        if root.val > key:  # if key value is less than root value, find the node in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:  # if key value is greater than root value, find the node in right subtree
            root.right = self.deleteNode(root.right, key)
        else:  # if we found the node (root.value == key), start to delete it
            if not root.right:  # if it doesn't have right children, we delete the node then new root would be root.left
                return root.left
            if not root.left:  # if it has no left children, we delete the node then new root would be root.right
                return root.right
            # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini  # replace value
            root.right = self.deleteNode(root.right, root.val)  # delete the minimum node in right subtree
        return root









