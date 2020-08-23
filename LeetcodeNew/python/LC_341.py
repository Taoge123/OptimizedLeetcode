
"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import collections

class NestedInteger:
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

"""
仔细分析数据结构的定义。vector<NestedInteger>包含的是元素是NestedInteger类型. 
当对元素做.getInteger()操作后得到的才是整形；做.getList()操作后得到的是vector<NestedInteger>类型。

设计一个stack<NestedInteger>Stack的堆栈。

hasNext()的目的，就是将Stack的栈顶元素不断展开（如果对应的是List数据的话），直至栈顶元素isInteger()为止。
则下一步的next()就是读取栈顶元素并抽取整形数据，同时退栈。
"""


class NestedIteratorBetter:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        res = self.stack.pop().getInteger()
        return res

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            temp = self.stack.pop().getList()
            for i in range(len(temp) - 1, -1, -1):
                self.stack.append(temp[i])

        if not self.stack:
            return False
        return True




class NestedIterator:
    def __init__(self, nestedList):
        self.queue = collections.deque()
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.queue.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



