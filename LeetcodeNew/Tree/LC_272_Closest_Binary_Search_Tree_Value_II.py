
"""
https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70556/Simple-DFS-%2B-Priority-Queue-Python-Solution

https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70573/Clear-Python-O(klogn)-Solution-with-Two-Stacks


Step 1. Binary search for target until node==None or node.val == target, record path
Step 2. For path node, if node.val>=target, add to stack Pred; otherwise(node.val<=target) add to stack Succ
Step 3. Stack tops are possible nearest element
Step 4. Compare both stack for nearest element and then "iterate" the stack

一开始思路非常不明确，看了不少discuss也不明白为什么。在午饭时间从头仔细想了一下，
像Closest Binary Search Tree Value I一样，追求O(logn)的解法可能比较困难，
但O(n)的解法应该不难实现。我们可以使用in-order的原理，从最左边的元素开始，
维护一个Deque或者doubly linked list，将这个元素的值从后端加入到Deque中，然后继续遍历下一个元素。
当Deque的大小为k时， 比较当前元素和队首元素与target的差来尝试更新deque。
循环结束条件是队首元素与target的差更小或者遍历完全部元素。这样的话时间复杂度是O(n)， 空间复杂度应该是O(k)。

Time Complexity - O(n)， Space Complexity - O(k)


"""
import heapq

class Solution(object):

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        def dfs(root, target, heap):
            if root is None:
                return

            dfs(root.left, target, heap)
            heapq.heappush(heap, (abs(root.val - target), root.val))
            dfs(root.right, target, heap)

        heap = []
        dfs(root, target, heap)

        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
        return output


class Solution2:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ans = []
        preStack = []
        sucStack = []

        while root:
            if root.val < target:
                preStack.append(root)
                root = root.right
            else:
                sucStack.append(root)
                root = root.left

        def getPredecessor(stack):
            if stack:
                pre = stack.pop()
                p = pre.left
                while p:
                    stack.append(p)
                    p = p.right
                return pre

        def getSuccessor(stack):
            if stack:
                suc = stack.pop()
                p = suc.right
                while p:
                    stack.append(p)
                    p = p.left
                return suc

        pre = getPredecessor(preStack)
        suc = getSuccessor(sucStack)

        while k:
            k -= 1
            if pre and not suc:
                ans.append(pre.val)
                pre = getPredecessor(preStack)
            elif not pre and suc:
                ans.append(suc.val)
                suc = getSuccessor(sucStack)
            elif pre and suc and abs(pre.val - target) <= abs(suc.val - target):
                ans.append(pre.val)
                pre = getPredecessor(preStack)
            elif pre and suc and abs(pre.val - target) >= abs(suc.val - target):
                ans.append(suc.val)
                suc = getSuccessor(sucStack)
        return ans


class Solution3:
    def closestKValues(self, root, target, k):
        d = []
        def dfs(node):
            if node:
                heapq.heappush(d, (abs(node.val - target), node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return [node for val, node in heapq.nsmallest(k, d)]



class Solution4:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        lst = []
        self.helper(root, target, k, lst)
        res = []
        for item in lst:
            res.append(item[1])
        return res

    def helper(self, root, target, k, lst):
        if not root:
            return
        if len(lst) < k:
            heapq.heappush(lst, (-abs(target - root.val), root.val))
        else:
            temp = heapq.heappop(lst)
            if abs(target - temp[1]) > abs(target - root.val):
                heapq.heappush(lst, (-abs(target - root.val), root.val))
            else:
                heapq.heappush(lst, temp)
        self.helper(root.left, target, k, lst)
        self.helper(root.right, target, k, lst)