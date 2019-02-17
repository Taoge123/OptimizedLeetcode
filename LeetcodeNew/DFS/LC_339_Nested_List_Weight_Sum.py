

class Solution1:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        def scanList(curr_list, depth):
            return sum(depth * x.getInteger() if x.isInteger() else scanList(x.getList(), depth + 1) for x in curr_list)

        return scanList(nestedList, 1)


class Solution2:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

    def depthPartialSum(self, List, depth=1):
        sum = 0
        for i in List:
            if i.isInteger():
                sum += i.getInteger() * depth
            else:
                sum += self.depthPartialSum(i.getList(), depth + 1)
        return sum




















