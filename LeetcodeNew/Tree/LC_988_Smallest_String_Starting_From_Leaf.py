

"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/233886/O(n)-solution-implemented-with-Python


Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.)

Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"
"""


"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/244205/Divide-and-conquer-technique-doesn't-work-for-this-problem

Many people have solved this problem with the basic idea of divide and conquer, where the key strategy is something like this:

answer(root) = min(answer(left) + root.val, answer(right) + root.val)
which is incorrect. Surprisingly, these solutions got accepted.
Let me explain this by this case:
[25, 1, null, 0, 0, 1, null, null, null, 0].

The expected answer is "ababz", while by divide-and-conqure we would get "abz".
The problem here is

string X < string Y
doesn't guarantee

X + a < Y + a
where a is a character. e.g.:

"ab" < "abab", but "abz" > "ababz"
So maybe the only correct way is a full DFS with backtracking.
(Still working on my solution, perhaps post later.)

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SolutionIncorrect:
    def smallestFromLeaf(self, node: 'TreeNode') -> 'str':
        if not node: return ''
        left = self.smallestFromLeaf(node.left)
        right = self.smallestFromLeaf(node.right)
        return (left if right == '' or (left != '' and left < right) else right) + chr(97 + node.val)


"""
We have to do a dfs and build all paths, to get the right solution

"""

class Soultion2:
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if not node:
                return
            path.append(chr(ord('a') + node.val))

            if not node.left and not node.right:
                res[0] = min(res[0], ''.join(path)[::-1])

            else:
                dfs(node.left, path)
                dfs(node.right, path)
            del path[-1]

        res = [str(chr(ord('z') + 1))]
        dfs(root, [])
        return res[0]



class Solution3:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        def dfs(node):
            if not node:
                return
            left, right = dfs(node.left), dfs(node.right)
            curr = chr(node.val + ord('a'))
            if not left and not right:
                return chr(node.val + ord('a'))
            if not left:
                return right + curr
            if not right:
                return left + curr
            return min(left + curr, right + curr)
        return dfs(root)

