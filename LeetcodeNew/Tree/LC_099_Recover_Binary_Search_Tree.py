"""

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?


Use a tree example: [100, 50, 200, 25, 75, 99, 400]
Sorted Order: 25,50,75,100,150,200,400
You can have out of order 50 and 200: 25,200,75,100,150,50,400.
Notice in this case we have 2 out of order pairs: (200,75) and (150,50).
Simply swap 200 and 50.
What if 25/50 or 200/400 are swapped? In that case we will have just one out of order element.
3 and 4 give us our algorithm.

"""

import sys


class Solution:
    def recoverTree(self, root):
        if not root:
            return

        self.prev, self.first, self.second = None, None, None
        self.helper(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)
        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.helper(root.right)






