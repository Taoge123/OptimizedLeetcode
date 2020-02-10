#
#
# def solution(parentheses, index):
#     # Type your solution here
#     stack = []
#     for i in range(index, len(parentheses)):
#         if parentheses[i] == "(":
#             stack.append((parentheses[i], i))
#         else:
#             if not stack:
#                 return -1
#             stack.pop()
#             if not stack:
#                 return i
#
# parentheses = "((()())())"
# index = 2
# print(solution(parentheses, index))
#
#

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

dummy = curr = ListNode(-1)
# curr = ListNode(-1)
curr.val = 3
print(dummy.val)

