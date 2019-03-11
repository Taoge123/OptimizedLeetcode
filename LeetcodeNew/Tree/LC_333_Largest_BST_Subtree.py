

"""

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?


http://www.cnblogs.com/grandyang/p/5188938.html
https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/
https://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/
http://www.cnblogs.com/grandyang/p/5188938.html
https://blog.csdn.net/qq508618087/article/details/51731417


My dfs returns four values:

    - N is the size of the largest BST in the tree.
    - If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
    - If the tree is a BST, then min and max are the minimum/maximum value in the tree.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SubTree:
    def __init__(self, largest, n, min, max):
        self.largest = largest  # largest BST
        self.n = n  # number of nodes in this ST
        self.min = min  # min val in this ST
        self.max = max  # max val in this ST


class Solution(object):
    def largestBSTSubtree(self, root):
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.max and root.val < right.min:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')

        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))


class SolutionStefan:
    def largestBSTSubtree(self, root):
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)

        return dfs(root)[0]


class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


INT_MIN = -2147483648
INT_MAX = 2147483647


# Helper function that allocates a new
# node with the given data and None left
# and right pointers.
class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns Information about subtree. The
# Information also includes size of largest
# subtree which is a BST
def largestBSTBT(root):
    # Base cases : When tree is empty or it has
    # one child.
    if (root == None):
        return 0, INT_MIN, INT_MAX, 0, True
    if (root.left == None and root.right == None):
        return 1, root.data, root.data, 1, True

    # Recur for left subtree and right subtrees
    l = largestBSTBT(root.left)
    r = largestBSTBT(root.right)

    # Create a return variable and initialize its
    # size.
    ret = [0, 0, 0, 0, 0]
    ret[0] = (1 + l[0] + r[0])

    # If whole tree rooted under current root is
    # BST.
    if (l[4] and r[4] and l[1] < root.data and r[2] > root.data):
        ret[2] = min(l[2], min(r[2], root.data))
        ret[1] = max(r[1], max(l[1], root.data))

        # Update answer for tree rooted under
        # current 'root'
        ret[3] = ret[0]
        ret[4] = True

        return ret

        # If whole tree is not BST, return maximum
    # of left and right subtrees
    ret[3] = max(l[3], r[3])
    ret[4] = False

    return ret


# Driver Code
if __name__ == '__main__':
    """Let us construct the following Tree 
        60  
        / \  
        65 70  
    /  
    50 """
    root = newNode(60)
    root.left = newNode(65)
    root.right = newNode(70)
    root.left.left = newNode(50)
    print("Size of the largest BST is", largestBSTBT(root)[3])


