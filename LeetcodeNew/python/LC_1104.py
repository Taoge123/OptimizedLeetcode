"""
First of all, ignore the fact that the binary tree is a zegzag labelled binary Tree.
Simply assuming it's a sequentially labelled binary tree. Then the path could be easily calculated.

The only difference between our assumption and the fact is that there are several different items.
The key abservation is that we could easily find the complement of those different items, given the height of our item:
complement = 2**(height+1) + 2**height - item

"""


class Solution:
    def pathInZigZagTree(self, label: int):
        return self.helper(label, 0)

    def helper(self, x, s):
        if x == 1:
            return [1]

        parent = x // 2
        if s == 0:
            s = 1
            while s < x:
                s = s * 2 + 1
            s = s + s // 2 + 1

        return self.helper(s // 2 - parent, s // 2) + [x]



class Solution2:
    def pathInZigZagTree(self, label):
        res = []
        while label:
            res.append(label)
            label /= 2
        res = res[::-1]
        for i in range(len(res)-2, 0, -2):
            res[i] = 2**(i+1)-1 + 2**i - res[i]
        return res




"""
Step by Step Explanation
With the thought in mind that in an ordered binary tree that goes from 1 to n:

Normally Ordered Binary Tree:
             1
           /   \
         2       3
       /  \     /  \
     4     5   6     7
   / |    /|   |\    | \
 8   9  10 11 12 13  14  15
Thought 1) You can easily determine the parent by dividing by 2 with a normally ordered (non-zigzag) binary tree
For example the parent of 9 can be calculated via int(9/2) which is 4

Thought 2) So we now how how to trace from the input label to the root node. So lets start with label In our example, we will use 14. To determine the parent of 14, notice that in the same spot in a normally ordered binary tree that it is 9. So you just need to calculate how to get from 14 to 9.

Zig Zag Binary Tree:
             1
           /   \
         3       2  <- 3+2-3 = 2/2 = 1
       /  \     /  \
     4     5   6     7   <- 7+4-4 = 7/2 = 3
   / |    /|   |\    | \
 15 14  13 12 11 10  9  8   <- 15+8-14 = 9/2 = 4
inversion formula: (max number of current level + min number of current level) - current number
For example to find the inversion of 14: 15 + 8 - 14 = 9
From here you just divide 9 by 2 to find the parent 4

Thought 3) You have to run the inversion formula at every level because at every level the row is inverted relative to the previous row

Time Complexity:
O(3 log n). 3 are needed as commented in the code.

Space Complexity:
If including the space required for the return res object counts as space then we need
O(log n) because we need to store the path from the root to the label.
"""

class Solution3:
    def pathInZigZagTree(self, label):
        res = [] # O(log n) space
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count*2: # O(log n) time
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0: # O(log n) time
            res.append(label)
            level_max = 2**(level) - 1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label)/2)
            level -= 1
        return res[::-1] # O(n) ti

