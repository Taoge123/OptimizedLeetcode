"""

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

import collections


class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to print all path from root to leaf in binary tree
def printPaths(root):
    # list to store path
    path = []
    printPathsRec(root, path, 0)


# Helper function to print path from root  to leaf in binary tree
def printPathsRec(root, path, pathLen):
    # Base condition - if binary tree is empty return
    if root is None:
        return

    # add current root's data into  path_ar list

    # if length of list is gre
    if (len(path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append(root.data)

        # increment pathLen by 1
    pathLen = pathLen + 1

    if root.left is None and root.right is None:

        # leaf node then print the list
        printArray(path, pathLen)
    else:
        # try for left and right subtree
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)

    # Helper function to print list in which


# root-to-leaf path is stored
def printArray(ints, len):
    for i in ints[0: len]:
        print(i, " ", end="")
    print()


# Driver program to test above function
""" 
Constructed binary tree is  
            10 
        / \ 
        8     2 
    / \ / 
    3 5 2 
"""
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
printPaths(root)



class TreeNode():  # 定义一个二叉树结构
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans + str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()

class Solution:
    def binaryTreePathSum(self, root):

        def dfs(root, path):
            if root:
                path += str(root.val)  # 添加一个节点
                if not root.left and not root.right:  # 如果是叶子节点，输出
                    res.append(path)
                else:
                    path += '->'
                    dfs(root.left, path)  # 左递归
                    dfs(root.right, path)  # 右递归

        res = []  # 用于记录所有路径
        dfs(root, '')
        return res
if __name__ == '__main__':
    solu = Solution()
    tree = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(5)
    tree.left = tree2
    tree.right = tree3
    tree2.right = tree4
    print(solu.binaryTreePathSum(tree))

# ---------------------
# 作者：GorillaNotes
# 来源：CSDN
# 原文：https://blog.csdn.net/XX_123_1_RJ/article/details/86720936
# 版权声明：本文为博主原创文章，转载请附上博文链接！

class TreeNode():  # 定义一个二叉树结构
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePathSum(self, root):

        def dfs(root, paths):
            if root:
                paths += root.val  # 路径相加
                if not root.left and not root.right:  # 叶子节点，输出
                    res.append(paths)
                else:
                    dfs(root.left, paths)  # 左递归
                    dfs(root.right, paths)  # 右递归

        res = []
        dfs(root, 0)
        return res


if __name__ == '__main__':
    solu = Solution()
    tree = TreeNode(5)
    tree2 = TreeNode(4)
    tree3 = TreeNode(8)
    tree.left = tree2
    tree.right = tree3
    print(solu.binaryTreePathSum(tree))
# ---------------------
# 作者：GorillaNotes
# 来源：CSDN
# 原文：https://blog.csdn.net/XX_123_1_RJ/article/details/86720936
# 版权声明：本文为博主原创文章，转载请附上博文链接！
class Solution:
    # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res

    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, ls + str(node.val) + "->"))
        return res

    # dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val) + "->", res)
        if root.right:
            self.dfs(root.right, ls + str(root.val) + "->", res)


class Solution2:
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        treepaths = [str(root.val)+'->'+path for path in self.binaryTreePaths(root.left)]
        treepaths += [str(root.val)+'->'+path for path in self.binaryTreePaths(root.right)]
        return treepaths



class Solution3:

    def __init__(self):
        self.result = []

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.find_paths(root, [])
        return self.result

    def is_leaf(self, node):
        return not node.left and not node.right


    def find_paths(self, node, current_path):
        if node:
            current_path.append(node.val)

            if self.is_leaf(node):
                # If we would have needed to add the path without formatting
                # it would have been append(list(current_path) because later
                # the current_path would have changed. Luckily we need to
                # format it anyway
                self.result.append("->".join([str(x) for x in current_path]))
            else:
                self.find_paths(node.left, current_path)
                self.find_paths(node.right, current_path)

            # Once weve finished with our node regardless if it's a leaf or
            # not, we need to remove the node's value (which is the last)
            # from the current_path. Without this part the current_path
            # will continue to have the nodes value for other paths as well
            current_path.pop()





