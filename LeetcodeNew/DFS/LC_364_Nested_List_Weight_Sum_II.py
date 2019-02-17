
"""
Two Pass Solution

In the first pass, get the maximum depth of the nested list.
The recursion is obvious - traverse the list and if there is any nestedList,
find its depth. The final depth is the maximum depth from any nestedList.
In the second pass, compute the sum using the same method as used in in the previous problem
https://leetcode.com/problems/nested-list-weight-sum/
"""


class Solution1:
    #Need the depth value in order to backward
    def depth(self, nestedList):
        curr_depth = 1
        for x in nestedList:
            if x.isInteger() == False:
                curr_depth = max(curr_depth, 1 + self.depth(x.getList()))
        return curr_depth

    def helper(self, nestedList, level, max_depth):
        for x in nestedList:
            if x.isInteger():
                self.d_sum = self.d_sum + x.getInteger() * (max_depth - level + 1)
            else:
                self.helper(x.getList(), level + 1, max_depth)
        return

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        max_depth = self.depth(nestedList)
        self.d_sum = 0
        self.helper(nestedList, 1, max_depth)
        return self.d_sum



"""
Single Pass Solution with Cache
Engineer the solution like Nested List Weight Sum I, 
but store the sum at each level without any weights.
Once completed, you will know the maximum level which will be the depth. 
Use that to do the computation for weighted sum.

"""
#OMG, this is amazing
from collections import defaultdict

class Solution2:
    def helper(self, nestedList, level, cache):
        self.max_level = max(self.max_level, level)
        for x in nestedList:
            if x.isInteger():
                cache[level] += x.getInteger()
            else:
                self.helper(x.getList(), level + 1, cache)
        return

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        cache, self.max_level = defaultdict(int), -1
        self.helper(nestedList, 1, cache)
        total_sum = 0
        for k, v in cache.items():
            total_sum = total_sum + v * (self.max_level - k + 1)
        return total_sum



"""
Single Pass Solution using a BFS like approach

Add all the integers at level to level_sum. 
Push all elements which are not interger (and are list type) into the list for next iteration. 
Make sure to flatten this list otherwise infinite loop.
Now we only initilaize level_sum once. And successive level's integers are added to it.
 nce a level finishes, we add to total_sum. This naturally implements the multiplication logic - 
 lower level sums are added multiple times to total sum.
https://discuss.leetcode.com/topic/49041/no-depth-variable-no-multiplication/2
"""

#BFS solution
class Solution3:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum







