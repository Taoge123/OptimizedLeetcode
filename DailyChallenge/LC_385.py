
class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
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


class Solution:
    def deserialize(self, s):
        stack, num, last = [], "", None
        for c in s:
            if c.isdigit() or c == "-":
                num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            elif c == "[":
                elem = NestedInteger()
                if stack: stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                last = stack.pop()
        return last if last else NestedInteger(int(num))



