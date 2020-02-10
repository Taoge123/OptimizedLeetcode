
"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

"""


"""
I see a lot of solution saying O(N), but actually not.
If it takes already O(N) time to find left part and right right, it could not be O(N).
If it is recursive solution, it should use a hashmap to reduce complexity, 
otherwise in most cases it has at least average O(NlogN).

Here I share my iterative solution.
We will preorder generate TreeNodes, push them to stack and postorder pop them out.

Loop on pre array and construct node one by one.
stack save the current path of tree.
node = new TreeNode(pre[i]), if not left child, add node to the left. otherwise add it to the right.
If we meet a same value in the pre and post, 
it means we complete the construction for current subtree. We pop it from stack.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionLee:
    def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]



class Solution2:
    def constructFromPrePost(self, pre, post):
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(post) == 1: return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1: idx], post[:(idx - 1)])
        root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1):-1])
        return root



class Solution3:
    def constructFromPrePost(self, pre, post):
        if pre:
            root = TreeNode(pre.pop(0))
            post.pop()
            if pre:
                if pre[0] == post[-1]:
                    root.left = self.constructFromPrePost(pre, post)
                else:
                    l, r = post.index(pre[0]), pre.index(post[-1])
                    root.left = self.constructFromPrePost(pre[:r], post[:l + 1])
                    root.right = self.constructFromPrePost(pre[r:], post[l + 1:])
            return root

class Solution4:
    def constructFromPrePost(self, pre, post):

        if not pre:
            return
        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]
        if not pre:
            return root
        i = post.index(pre[0])
        root.left = self.constructFromPrePost(pre[:i+1], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+1:], post[i+1:])
        return root

