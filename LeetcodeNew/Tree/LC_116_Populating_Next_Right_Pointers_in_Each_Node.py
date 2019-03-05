


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root and root.left:  # 如有root和左孩子
            root.left.next = root.right  # 左孩子指向右孩子
            if root.next:  # 如链表有右边，那么其右孩子指向右边节点左孩子
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect(root.left)
            self.connect(root.right)


class SolutionBFS:
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        if not root:
            return None
        cur = root
        next = root.left

        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left


class Solution:
    def connect1(self, root):
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

    # BFS
    def connect2(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)

    # DFS
    def connect(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)







