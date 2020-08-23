
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head):
        stack = []
        res = []

        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            # stack will store the index and value
            stack.append([len(res), head.val])
            res.append(0)

            head = head.next
        return res


class SolutionTony:
    def nextLargerNodes(self, head: ListNode):
        stack = []
        dummy = head
        n = 0
        while dummy:
            n += 1
            dummy = dummy.next

        res = [0] * n
        index = 0
        while head:
            if not stack:
                stack.append([index, head.val])
            else:
                while stack and stack[-1][1] < head.val:
                    res[stack.pop()[0]] = head.val
                stack.append([index, head.val])
            index += 1
            head = head.next
        return res

