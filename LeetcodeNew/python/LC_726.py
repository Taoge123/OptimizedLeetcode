"""
https://blog.csdn.net/fuxuemingzhu/article/details/82938164


1. We are starting from the last element.
2. When we find on our way any number, lowercase char, or parentheses, we do some additions and then continue
— If it was a number we want to know how much digits it has
— If it was a lowercase char we want to store it in variable lower and append it to the key = formula[i] + lower on the next cycle
— If it was a closing parenthesis we want to store it's multiplier in our stack m.append(digit * m[-1])
— If it was an opening parenthesis we should remove the last multiplier m.pop()
3. After that we add the key = element and value = m[-1] * int(digit or 1) to our dictionary (hashmap).

"""

import collections

class SolutionRika:
    def countOfAtoms(self, formula: str) -> str:

        hashmap = collections.defaultdict(int)
        stack = [1]
        num = ''
        lower = ''

        for i in range(len(formula) - 1, -1, -1):
            ch = formula[i] + lower

            if ch.isdigit():
                num = ch + num  # num is in str type
            elif ch.islower():
                lower = ch  # lower name after upper case
            elif ch == ')':
                stack.append(stack[-1] * int(num or 1))  # append factors
                num = ''
            elif ch == '(':
                stack.pop()
            else:  # uppercase char --> name
                hashmap[ch] += stack[-1] * int(num or 1)
                num = ''
                lower = ''
        res = ''
        for key, value in sorted(hashmap.items()):
            if value == 1:
                value = ''
            res += key + str(value)
        return res




class SolutionCheng:
    def countOfAtoms(self, formula: str) -> str:

        n = len(formula)
        stack = [collections.Counter()]
        i = 0

        while i < n:
            ch = formula[i]
            if ch == "(":
                stack.append(collections.Counter())
                i += 1
            elif ch == ")":
                cur_counter = stack.pop()

                # fint the multiplier after ')'
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1

                mutiplier = int(formula[start:i]) if formula[start:i] else 1

                # update the top counter in the stack
                for atom in cur_counter:
                    count = cur_counter[atom]
                    stack[-1][atom] += count * mutiplier

            else:
                # find atom:
                atom = ch
                i += 1
                start = i
                while i < n and formula[i].islower():
                    i += 1
                atom += formula[start:i]
                # find the number
                # fint the multiplier after ')'
                start = i
                while i < n and formula[i].isdigit():
                    i += 1

                count = int(formula[start:i]) if formula[start:i] else 1
                stack[-1][atom] += count

        res = ""
        counter = stack[-1]

        for atom in sorted(counter):
            res += atom
            if counter[atom] > 1:
                res += str(counter[atom])
        return res

