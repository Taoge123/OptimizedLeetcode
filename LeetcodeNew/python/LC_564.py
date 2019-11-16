
"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""


class Solution:
    def nearestPalindromic(self, n):

        if int(n) <= 10:
            return str(int(n) - 1)

        elif len(n) == 2:
            if n == '99':
                return '101'
            elif n == '11':
                return '9'
            else:
                options = [n[0] * 2, str(int(n[0]) - 1) * 2, str(int(n[0]) + 1) * 2]
                output = filter(lambda x: x != n, options)
                diff = [abs(int(x) - int(n)) for x in output]
                output = filter(lambda x: abs(int(x) - int(n)) == min(diff), options)
                return output[0]
        else:
            m = n[len(n) / 2 - 1:len(n) / 2 + 2] if len(n) % 2 != 0 else n[len(n) / 2 - 2:len(n) / 2 + 2]
            front = n[:(len(n) - len(m)) / 2]
            end = front[::-1]

            l1 = list(m)
            if l1[1] == '9':
                l1[1] = '0'
                l1[0] = str(int(l1[0]) + 1)
            else:
                l1[1] = str(int(l1[1]) + 1)
            m1 = ''.join(l1)

            l2 = list(m)
            if l2[1] == '0':
                l2[1] = '9'
                l2[0] = str(int(l2[0]) - 1) if l2[0] != '0' else '0'
            else:
                l2[1] = str(int(l2[1]) - 1)
            m2 = ''.join(l2)

            options = [x[:len(x) / 2] + x[::-1][len(x) / 2:] for x in [m, m1, m2]]
            p = [front + x + end for x in options]
            p.append('9' * (len(n) - 1))
            p.append('1' + '0' * (len(n) - 1) + '1')

            output = filter(lambda x: x != n, p)
            diff = [abs(int(x) - int(n)) for x in output]
            output = filter(lambda x: abs(int(x) - int(n)) == min(diff), output)
            output = map(lambda x: int(x), output)
            output.sort()
            return str(output[0])





