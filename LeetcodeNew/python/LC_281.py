"""
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""


from collections import deque
class ZigzagIterator:

    def __init__(self, v1, v2):
        self.queue = deque([i for i in (deque(v1), deque(v2)) if i])

    def next(self):
        leftList = self.queue.popleft()
        res = leftList.popleft()
        if leftList:
            self.queue.append(leftList)
        return res

    def hasNext(self):
        return len(self.queue) > 0



v1 = [1,2]
v2 = [3,4,5,6]

a = ZigzagIterator(v1, v2)
print(a.next())
print(a.next())
print(a.next())
print(a.next())


"""
0 = {deque: 2} deque([1, 2])
1 = {deque: 4} deque([3, 4, 5, 6])

"""