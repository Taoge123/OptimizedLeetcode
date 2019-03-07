
"""
Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5

I have used a hash-map ctr to count the sum occurrence.

I have wrote a sub function countSubtreeSum to travel through a tree and return the sum of the tree.

In countSubtreeSum, I will travel through the left node and the right node,
calculate the sum of the tree, increment the counter ctr, and return the sum.


"""
import collections

class Solution:
    def findFrequentTreeSum(self, root):
        if root == None: return []

        def getSum(node):
            if node == None: return 0
            s = node.val + getSum(node.left) + getSum(node.right)
            c[s] += 1
            return s

        c = collections.Counter()
        getSum(root)
        frequent = max(c.values())
        return [s for s in c if c[s] == frequent]


class SolutionSameIdea:
    def findFrequentTreeSum(self, rt):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not rt: return []

        ctr = collections.defaultdict(int)

        def traverse(root):
            if not root: return 0
            left = traverse(root.left)
            right = traverse(root.right)
            root.val = root.val + left + right
            ctr[root.val] += 1
            return root.val

        traverse(rt)

        mc = max(ctr.values())
        return [k for k, v in ctr.items() if v == mc]


"""
like others solutions,
computing the left subtree, then right and updating the current node ,
used an auxiliary hashmap that counts

h[s] = u
sum s has been reached u times
given a node and its (at most 2 subtrees), once the sum "sumleft" and "sumright" of the subtrees have been computed

then the current sum of the tree is node.val + "sumleft" + "sumright"
before returning it, update (increment) the hashmap



-----------


The idea is very simple:

Traverse structure using post order
Calculate sum of sub trees on every step
Store frequence of occurence of calculated sum into map/dict
Maintain max of frequence of occurence on every step. Letter we will use it to filter out result
Traverse map/dict and filter output based on max of frequence of occurence
Java implementation:
"""










