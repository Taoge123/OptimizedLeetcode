import collections
#
# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         "K4(ON(SO3)2)2"
#
#         formula = formula[::-1]
#         stack = []
#         curr = 0
#         summ = 1
#         table = collections.defaultdict(int)
#         res = collections.defaultdict(int)
#         charStack = []
#
#         for i, char in enumerate(formula):
#             if char.isdigit() and formula[i+1] == ')':
#                 stack.append(int(char))
#                 summ = int(char) if summ == 1 else summ * int(char)
#
#
#             elif char.isdigit() and formula[i+1].isalpha():
#                 table[formula[i+1]] += int(char)
#                 charStack = [formula[i+1]]
#
#             elif char.isalpha() and formula[i-1].isalpha():
#                 table[char] = 1
#
#             elif char == '(':
#
#                 while stack:
#
#                     node = stack.pop()
#                     table[node] = table[node] * summ
#
#
#         print(table)
#
#
#
#
# """
# 2)2)3OS(NO(4K
# """
#
#
# formula = "K4(ON(SO3)2)2"
# a = Solution()
# print(a.countOfAtoms(formula))
#
#

class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        self.table = collections.defaultdict(list)

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        temp = 0
        if not self.stack:
            self.table = collections.defaultdict(list)
            return -1
        else:
            for k, val in self.table.items():
                if len(self.stack) <= k:
                    temp += sum(val)
                    self.table[k-1].extend(val)
                    del self.table[k]


            return self.stack.pop() + temp

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        self.table[k].append(val)

"""
["CustomStack","push","pop","increment","pop","increment","push","pop","push","increment","increment","increment"]
[[2],[34],[],[8,100],[],[9,91],[63],[],[84],[10,93],[6,45],[10,4]]


"""

a = CustomStack(2)
print(a.push(34))
print(a.pop())
print(a.increment(8, 100))
print(a.pop())
print(a.increment(9, 91))
print(a.push(63))
print(a.pop())
print(a.push(84))
print(a.increment(10, 93))
print(a.increment(6, 45))
print(a.increment(10, 4))





