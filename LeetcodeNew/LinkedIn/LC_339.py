


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth, ret = 1, 0
        while nestedList:
            ret += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
            depth += 1
        return ret

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        def scanList(curr_list, depth):
            return sum(depth * x.getInteger() if x.isInteger() else scanList(x.getList(), depth + 1) for x in curr_list)

        return scanList(nestedList, 1)




