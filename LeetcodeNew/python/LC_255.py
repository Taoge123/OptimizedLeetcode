"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree:

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?

for every pair {a, b} and a < b, we need a < c for every c after b

a_max < b => c

"""


class SolutionRika:
    def verifyPreorder(self, preorder) -> bool:
        # BST --> node.val in in between (min, max)

        self.pos = 0
        return self.dfs(preorder, float('-inf'), float('inf'))

    def dfs(self, preorder, minn, maxx):
        if self.pos >= len(preorder):
            return True

        if preorder[self.pos] < minn or preorder[self.pos] > maxx:
            return False

        value = preorder[self.pos]
        self.pos += 1
        left = self.dfs(preorder, minn, value)
        right = self.dfs(preorder, value, maxx)

        return left or right



class Solution:
    def verifyPreorder(self, preorder) -> bool:

        stack, mini = [], float('-inf')

        for num in preorder:
            if num < mini:
                return False

            while stack and num > stack[-1]:
                mini = stack.pop()

            stack.append(num)

        return True



"""

a [XXXXXXXXXXXX]    [YYYYYYYYYYY]
  b[XXXXX][YYYYYY]


"""

class SolutionTLE:
    def verifyPreorder(self, preorder) -> bool:
        return self.dfs(preorder, 0, len(preorder) - 1)

    def dfs(self, preorder, start, end):
        if start >= end:
            return True

        root = preorder[start]
        i = start + 1
        while i <= end and preorder[i] < root:
            i += 1

        for j in range(i, end + 1):
            if preorder[j] < root:
                return False
        return self.dfs(preorder, start + 1, i - 1) and self.dfs(preorder, i, end)




preorder = [5,2,6,1,3]
a = Solution()
print(a.verifyPreorder(preorder))

