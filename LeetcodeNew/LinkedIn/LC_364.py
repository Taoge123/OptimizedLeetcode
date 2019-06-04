class Solution(object):
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


