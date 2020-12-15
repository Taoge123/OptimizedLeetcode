

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

