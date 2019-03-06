

"""
https://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/
http://www.cnblogs.com/grandyang/p/5188938.html
https://blog.csdn.net/qq508618087/article/details/51731417


My dfs returns four values:

    - N is the size of the largest BST in the tree.
    - If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
    - If the tree is a BST, then min and max are the minimum/maximum value in the tree.

"""


class SubTree(object):
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


# Returns size of the largest BST subtree
# in a Binary Tree (efficient version).
def largestBST(node):
    # Set the initial values for calling
    # largestBSTUtil()
    Min = [999999999999]  # For minimum value in
    # right subtree
    Max = [-999999999999]  # For maximum value in
    # left subtree

    max_size = [0]  # For size of the largest BST
    is_bst = [0]

    largestBSTUtil(node, Min, Max, max_size, is_bst)

    return max_size[0]


# largestBSTUtil() updates max_size_ref[0]
# for the size of the largest BST subtree.
# Also, if the tree rooted with node is
# non-empty and a BST, then returns size of
# the tree. Otherwise returns 0.
def largestBSTUtil(node, min_ref, max_ref, max_size_ref, is_bst_ref):
    # Base Case
    if node == None:
        is_bst_ref[0] = 1  # An empty tree is BST
        return 0  # Size of the BST is 0

    Min = 999999999999

    # A flag variable for left subtree property
    # i.e., max(root.left) < root.data
    left_flag = False

    # A flag variable for right subtree property
    # i.e., min(root.right) > root.data
    right_flag = False

    ls, rs = 0, 0  # To store sizes of left and
    # right subtrees

    # Following tasks are done by recursive
    # call for left subtree
    # a) Get the maximum value in left subtree
    #   (Stored in max_ref[0])
    # b) Check whether Left Subtree is BST or
    #    not (Stored in is_bst_ref[0])
    # c) Get the size of maximum size BST in
    #    left subtree (updates max_size[0])
    max_ref[0] = -999999999999
    ls = largestBSTUtil(node.left, min_ref, max_ref, max_size_ref, is_bst_ref)
    if is_bst_ref[0] == 1 and node.data > max_ref[0]: left_flag = True

    # Before updating min_ref[0], store the min
    # value in left subtree. So that we have the
    # correct minimum value for this subtree
    Min = min_ref[0]

    # The following recursive call does similar
    # (similar to left subtree) task for right subtree
    min_ref[0] = 999999999999
    rs = largestBSTUtil(node.right, min_ref, max_ref, max_size_ref, is_bst_ref)
    if is_bst_ref[0] == 1 and node.data < min_ref[0]:
        right_flag = True

    # Update min and max values for the
    # parent recursive calls
    if Min < min_ref[0]:
        min_ref[0] = Min
    if node.data < min_ref[0]:  # For leaf nodes
        min_ref[0] = node.data
    if node.data > max_ref[0]:
        max_ref[0] = node.data

        # If both left and right subtrees are BST.
    # And left and right subtree properties hold
    # for this node, then this tree is BST.
    # So return the size of this tree
    if left_flag and right_flag:
        if ls + rs + 1 > max_size_ref[0]:
            max_size_ref[0] = ls + rs + 1
        return ls + rs + 1
    else:

        # Since this subtree is not BST, set is_bst
        # flag for parent calls is_bst_ref[0] = 0;
        return 0


# Driver Code
if __name__ == '__main__':
    # Let us construct the following Tree
    #     50
    # /     \
    # 10     60
    # / \     / \
    # 5 20 55 70
    #         /     / \
    #     45     65 80
    root = newNode(50)
    root.left = newNode(10)
    root.right = newNode(60)
    root.left.left = newNode(5)
    root.left.right = newNode(20)
    root.right.left = newNode(55)
    root.right.left.left = newNode(45)
    root.right.right = newNode(70)
    root.right.right.left = newNode(65)
    root.right.right.right = newNode(80)

# The complete tree is not BST as 45 is in
# right subtree of 50. The following subtree
# is the largest BST
#     60
# / \
# 55     70
# /     / \
# 45     65 80

print("Size of the largest BST is", largestBST(root))

