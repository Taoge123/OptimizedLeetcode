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


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = formula + ' '
        table = {}
        m = [1]
        digit = ''
        lower = ''

        for i in range(len(formula) - 2, -1, -1):
            element = formula[i] + lower
            if element.isdigit():
                digit = element + digit
                continue
            elif element.islower():
                lower = element + lower
                continue
            elif element == ')':
                m.append(m[-1] * int(digit))
                digit = ''
                continue
            elif element == '(':
                m.pop()
                continue
            table[element] = table.get(element, 0) + m[-1] * int(digit or 1)
            digit = ''
            lower = ''

        res = ''
        for key, value in sorted(table.items()):
            if value == 1:
                value = ''
            res = res + key + str(value)
        return res




