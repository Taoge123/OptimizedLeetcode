
"""

https://segmentfault.com/u/ethannnli/articles?page=8&sort=vote
https://segmentfault.com/a/1190000003874375

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

http://www.cnblogs.com/grandyang/p/5327635.html
https://segmentfault.com/a/1190000003874375

    10
   /  \
  5    12
 / \
2   6
同样是看这个例子，我们序列是[10, 5, 2, 6, 12]，如果用栈的话，遍历序列到第n个数时，栈中的情况是这样的：

1 | 10
2 | 10 5
3 | 10 5 2
4 | 10 6
5 | 12
可见我们栈的大小是不会超过我们当前遍历的数的位置的，所以我们大可以用该序列的之前遍历过的部分来当做我们的栈。
这里用一个i指针标记栈顶。

后续 Follow Up
Q：如何验证中序序列？
A：中序序列是有序的，只要验证其是否升序的就行了。

Q：如何验证后序序列？
A：后序序列的顺序是left - right - root，而先序的顺序是root - left - right。
我们同样可以用本题的方法解，不过是从数组的后面向前面遍历，因为root在后面了。
而且因为从后往前看是先遇到right再遇到left，所以我们要记录的是限定的最大值，而不再是最小值，
栈pop的条件也变成pop所有比当前数大得数。栈的增长方向也是从高向低了。


Kinda simulate the traversal, keeping a stack of nodes (just their values)
of which we're still in the left subtree.
If the next number is smaller than the last stack value,
then we're still in the left subtree of all stack nodes,
so just push the new one onto the stack. But before that,
pop all smaller ancestor values, as we must now be in their right subtrees (or even further,
in the right subtree of an ancestor). Also, use the popped values as a lower bound,
since being in their right subtree means we must never come across a smaller number anymore.

https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/68149/Python-solution-with-detailed-explanation


这道题让给了我们一个一维数组，让我们验证其是否为一个二叉搜索树的先序遍历出的顺序，
我们都知道二叉搜索树的性质是左<根<右，如果用中序遍历得到的结果就是有序数组，而先序遍历的结果就不是有序数组了，
但是难道一点规律都没有了吗，其实规律还是有的，根据二叉搜索树的性质，当前节点的值一定大于其左子树中任何一个节点值，
而且其右子树中的任何一个节点值都不能小于当前节点值，那么我们可以用这个性质来验证，举个例子，比如下面这棵二叉搜索树：


public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        Stack<Integer> stk = new Stack<Integer>();
        // 初始化最小值为最小整数
        int min = Integer.MIN_VALUE;
        for(int num : preorder){
            // 违反最小值限定则是无效的
            if(num < min) return false;
            // 将路径中所有小于当前的数pop出来并更新最小值
            while(!stk.isEmpty() && num > stk.peek()){
                min = stk.pop();
            }
            // 将当前值push进去
            stk.push(num);
        }
        return true;
    }
}

"""



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






