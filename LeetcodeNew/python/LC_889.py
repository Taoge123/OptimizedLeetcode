
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        print(pre, post)
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root


class Solution2:
    preIndex, posIndex = 0, 0
    def constructFromPrePost(self, pre, post):
        print(self.preIndex, self.posIndex)
        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        if (root.val != post[self.posIndex]):
            root.left = self.constructFromPrePost(pre, post)
        if (root.val != post[self.posIndex]):
            root.right = self.constructFromPrePost(pre, post)
        self.posIndex += 1
        return root

pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

a = Solution2()
print(a.constructFromPrePost(pre, post))


