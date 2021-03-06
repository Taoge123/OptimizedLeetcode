
"""
https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/


Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5

https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation

empty
[integer]
[integer] ( [tree] )
[integer] ( [tree] ) ( [tree] )

There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

When there is no '(', we are in one of the first two cases and proceed appropriately.
Else, we find the index "jx" of the ')' character that marks the end of the first tree.
We do this by keeping a tally of how many left brackets minus right brackets we've seen.
When we've seen 0, we must be at the end of the first tree.
The second tree is going to be the expression S[jx + 2: -1],
which might be empty if we are in case #3.


"""


"""
这道题让我们根据一个字符串来创建一个二叉树，其中结点与其左右子树是用括号隔开，
每个括号中又是数字后面的跟括号的模式，这种模型就很有递归的感觉，所以我们当然可以使用递归来做。
首先我们要做的是先找出根结点值，我们找第一个左括号的位置，如果找不到，说明当前字符串都是数字，
直接转化为整型，然后新建结点返回即可。否则的话从当前位置开始遍历，因为当前位置是一个左括号，
我们的目标是找到与之对应的右括号的位置，但是由于中间还会遇到左右括号，
所以我们需要用一个变量cnt来记录左括号的个数，如果遇到左括号，cnt自增1，
如果遇到右括号，cnt自减1，这样当某个时刻cnt为0的时候，我们就确定了一个完整的子树的位置，
那么问题来了，这个子树到底是左子树还是右子树呢，我们需要一个辅助变量start，
当最开始找到第一个左括号的位置时，将start赋值为该位置，那么当cnt为0时，如果start还是原来的位置，
说明这个是左子树，我们对其调用递归函数，注意此时更新start的位置，这样就能区分左右子树了

下面这种解法使用迭代来做的，借助栈stack来实现。遍历字符串s，用变量j记录当前位置i，
然后看当前遍历到的字符是什么，如果遇到的是左括号，什么也不做继续遍历；如果遇到的是数字或者负号，
那么我们将连续的数字都找出来，然后转为整型并新建结点，此时我们看stack中是否有结点，如果有的话，
当前结点就是栈顶结点的子结点，如果栈顶结点没有左子结点，那么此结点就是其左子结点，反之则为其右子结点。
之后要将此结点压入栈中。如果我们遍历到的是右括号，说明栈顶元素的子结点已经处理完了，将其移除栈

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation
# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/300543/Python-stack-solution-with-comment-beats-95-on-time-and-space


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        stack = []
        num = ''
        root = None

        for idx, char in enumerate(s):
            if char == '(':
                pass
            elif char == ')':
                stack.pop()
            else:
                num += char
                if idx + 1 >= len(s) or not s[idx + 1].isdigit():
                    curr = TreeNode(int(num))
                    num = ''
                    if not stack:
                        root = curr
                    else:
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = curr
                        else:
                            parent.right = curr

                    stack.append(curr)

        return root


