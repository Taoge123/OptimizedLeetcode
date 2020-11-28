
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        self.index = 0
        return self.dfs(s, 0)

    def dfs(self, s, depth):
        if self.index == len(s):
            return
        for i in range(depth):
            if s[self.index + i] != '-':
                return
        self.index += depth
        curr = 0
        while self.index < len(s) and s[self.index].isdigit():
            curr = curr * 10 + int(s[self.index])
            self.index += 1
        node = TreeNode(curr)
        node.left = self.dfs(s, depth + 1)
        node.right = self.dfs(s, depth + 1)
        return node

"""
Explanation
We save the construction path in a stack.
In each loop,
we get the number level of '-'
we get the value val of node to add.

If the size of stack is bigger than the level of node,
we pop the stack until it's not.

Finally we return the first element in the stack, as it's root of our tree.

Complexity
Time O(S), Space O(N)"""


class Solution2:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        i = 0
        while i < len(S):
            level = 0
            val = ""
            while i < len(S) and S[i] == '-':
                level += 1
                i += 1
            while i < len(S) and S[i] != '-':
                val += S[i]
                i += 1

            while len(stack) > level:
                stack.pop()

            node = TreeNode(val)
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]



S = "1-2--3---4-5--6---7"
a = Solution2()
print(a.recoverFromPreorder(S))




