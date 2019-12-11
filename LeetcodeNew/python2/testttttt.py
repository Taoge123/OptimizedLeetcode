import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        "K4(ON(SO3)2)2"

        formula = formula[::-1]
        stack = []
        curr = 0
        summ = 1
        table = collections.defaultdict(int)
        res = collections.defaultdict(int)
        charStack = []

        for i, char in enumerate(formula):
            if char.isdigit() and formula[i+1] == ')':
                stack.append(int(char))
                summ = int(char) if summ == 1 else summ * int(char)


            elif char.isdigit() and formula[i+1].isalpha():
                table[formula[i+1]] += int(char)
                charStack = [formula[i+1]]

            elif char.isalpha() and formula[i-1].isalpha():
                table[char] = 1

            elif char == '(':

                while stack:

                    node = stack.pop()
                    table[node] = table[node] * summ


        print(table)




"""
2)2)3OS(NO(4K
"""


formula = "K4(ON(SO3)2)2"
a = Solution()
print(a.countOfAtoms(formula))






